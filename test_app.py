import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setup_db
from app import create_app


assistance_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjI2Qm9uRHEzcnl6YnA0WERwQUJyUCJ9.eyJpc3MiOiJodHRwczovL2Rldi01dmtxdXd4Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjExM2VlZmViMTUxY2UwMDY4NWU4MGM3IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzE0NzIwNDMsImV4cCI6MTYzMTU1ODQ0MywiYXpwIjoiNmRHY3V4NlhIY3lMMXRPNU5WWVR5S3dEcTJTOWNyb00iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbIkdFVDphY3RvcnMiLCJHRVQ6bW92aWVzIl19.ioXS2QBSahTQwyKiPyov6oC0tiwDEpiD9ClSNo2IP-p3IpUUME5D6lE2GGXwvWacjcnXI9NRfowCgLdgZShG1zc70DB8akaIlm9rmFUxh63LM5ji26EaFKOGE1pxo-vZZTsyNYtvrqoX_dqRy5bsxdg_8fCgYd26IIsSSzz_bEel6tyTvyu_pRhByVNgJ8LS9FRNlJvqLiuGNL3BauyQuMfsm2086Rn8yjT2AcwVi1xLT_xUmcDjb6XrSSPvoW_CF54H01eYa1bqu01de-XCi2WkI8HTuu-cBtdd9dETuiHazRUxnGzx3yVOUpN650gBgas4ZBdc7I47wZxDKpdfGw'

director_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjI2Qm9uRHEzcnl6YnA0WERwQUJyUCJ9.eyJpc3MiOiJodHRwczovL2Rldi01dmtxdXd4Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjEzZDExYjA2MWJkMWUwMDY4MDJlMzBjIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzE0NTkxMDAsImV4cCI6MTYzMTU0NTUwMCwiYXpwIjoiNmRHY3V4NlhIY3lMMXRPNU5WWVR5S3dEcTJTOWNyb00iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbIkRFTEVURTphY3RvcnMiLCJHRVQ6YWN0b3JzIiwiR0VUOm1vdmllcyIsIlBBVENIOm1vdmllcyIsIlBPU1Q6YWN0b3JzIl19.N3SLe6_2qKW2fQLQzNEoeQ0514oz1x8iWDmMYSLLFtjA0aDOjCBDtiYTIenq9MJk22IlTU3bVCLLZ6K4FxO0phq4-oJjqtivnmunkMdFh6OsrmGOOptDH5gQ6MJLSxxxMjIpVrpzfjeXG1ptAOBC3qZKpM9MvN1xmeEbekT6nmSSh6h0hCVSZAOinfabkYLdHIj49C9_ZrU0iTGqqBFcfjn6_J8bXNs5m9oKYiq2j8P3_OpIp6pOzUNCLuVZWLX7xLyXkKN0F8LIU3LdZAmfazbnThjUF2JMB984IVjlOB1Ik25h_z_1l8zfILRc65LIm3i0s47UohgqMIaen6jIQQ'

producer_token = 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjI2Qm9uRHEzcnl6YnA0WERwQUJyUCJ9.eyJpc3MiOiJodHRwczovL2Rldi01dmtxdXd4Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjExMzBkNzA4ZTMxZDUwMDY5ZjhjODVjIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzE0ODE5NDAsImV4cCI6MTYzMTU2ODM0MCwiYXpwIjoiNmRHY3V4NlhIY3lMMXRPNU5WWVR5S3dEcTJTOWNyb00iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbIkRFTEVURTphY3RvcnMiLCJERUxFVEU6bW92aWVzIiwiR0VUOmFjdG9ycyIsIkdFVDptb3ZpZXMiLCJQQVRDSDphY3RvcnMiLCJQQVRDSDptb3ZpZXMiLCJQT1NUOmFjdG9ycyIsIlBPU1Q6bW92aWVzIl19.bMqiXOmuJl2HtQSmduvHflbVI2ZvhVVaL1PeqCDIYeCDFFKATHJ1VVQvb4n39mxiBWoROqb3GWtt24CUJsEzmBb3lIqOCu7mqQkCl0sOz7AzDcomYu9yOW26C1Obfez2hx_V5LSPCVTJ7-iQZ29vd9Yejs5F5upZ35GJICNBk8oV3fudh2IC4YR_ozwwg6J4NRz9IvsD0Zr8VruY-w2oTN4N9ZgLS-BulcBIMQ5FxO8Z7IU6JcDodugWMloDx7J76pCZMide1rrN9k6bpLKCX1fAQviJN-wx6zsc-N5LCjoQmbfYYJyjWNBw2k60yp0ekNVMiCLWAQWjjYbpuQg8oA'



class CapstoneTest(unittest.TestCase):
   
    def setUp(self):

        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "capstone"
        self.database_path = "postgres://{}:{}@{}/{}".format(
            'postgres', '4952', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)
        self.new_movie = {
            'title': 'who i am ?',
            'release_date': '1/10/2010'
        }
        self.new_actor = {
            "name": "alwaleed",
            "age": "22",
            "gender": "male"
        }

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    '''
    Test POST actor and movie
    '''

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    # create actor with authorization token

    def test_create_actor_with_valid_token(self):

        res = self.client().post(
            '/actors',
            json=self.new_actor,
            headers={
                "Authorization": "Bearer {}".format(producer_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    # create actor with unauthorized token
    def test_create_actor_with_invalid_token(self):
        res = self.client().post(
            '/actors',
            json=self.new_actor,
            headers={
                "Authorization": "Bearer {}".format(assistance_token)})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['code'], "unauthorized")
        self.assertEqual(data['description'], "Permission not found.")

    # create movie with authorization token

    def test_create_movie_with_valid_token(self):

        response = self.client().post(
            '/movies',
            json=self.new_movie,
            headers={
                "Authorization": "Bearer {}".format(producer_token)})
        res = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(res['success'])

    # create movie with unauthorized token
    def test_create_movie_with_invalid_token(self):

        response = self.client().post(
            '/movies',
            json=self.new_movie,
            headers={
                "Authorization": "Bearer {}".format(director_token)})
        res = json.loads(response.data)

        self.assertEqual(response.status_code, 403)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    '''
    Test GET actors and moves
    '''

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_get_all_movies_with_valid_token(self):
        response = self.client().get(
            '/movies',
            headers={"Authorization": "Bearer {}".format(assistance_token)})
        res = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(res['success'])

    def test_get_all_movies_without_token(self):
        response = self.client().get('/movies')
        res = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    def test_get_all_actors_with_valid_token(self):
        response = self.client().get(
            '/actors',
            headers={"Authorization": "Bearer {}".format(assistance_token)})
        res = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(res['success'])

    def test_get_all_actors_without_token(self):
        response = self.client().get('/actors')
        res = json.loads(response.data)
        self.assertEqual(response.status_code, 401)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    '''
    Test PATCH actors and movies
    '''

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_update_actor_with_valid_token(self):

        request = {
            "name": "saleh", "age": 34
        }

        res = self.client().patch(
            '/actors/8',
            json=request,
            headers={
                "Authorization": "Bearer {}".format(producer_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_update_actor_with_invalid_token(self):

        request = {
            "name": "saleh", "age": 34
        }
        res = self.client().patch(
            '/actors/8',
            json=request,
            headers={
                "Authorization": "Bearer {}".format(assistance_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)

    def test_update_movies_with_valid_token(self):

        request = {
            "title": "inseption", "release_date": "11/2/2010"
        }

        res = self.client().patch(
            '/movies/8',
            json=request,
            headers={
                "Authorization": "Bearer {}".format(producer_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_update_movies_with_invalid_token(self):

        request = {
            "title": "inseption", "release_date": "11/2/2010"
        }

        res = self.client().patch(
            '/movies/8',
            json=request,
            headers={
                "Authorization": "Bearer {}".format(assistance_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    '''
    Test DELETE actors and movies
    '''

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_delete_actor_with_valid_token(self):

        res = self.client().delete('/actors/5',
                                   headers={"Authorization": "Bearer {}".format(producer_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_delete_actor_with_invalid_token(self):

        res = self.client().delete(
            '/actors/5',
            headers={
                "Authorization": "Bearer {}".format(assistance_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)

    def test_delete_movie_with_valid_token(self):

        res = self.client().delete('/movies/6',
                                   headers={"Authorization": "Bearer {}".format(producer_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_delete_movie_with_invalid_token(self):

        res = self.client().delete(
            '/movies/6',
            headers={
                "Authorization": "Bearer {}".format(assistance_token)})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)


if __name__ == "__main__":
    unittest.main()
