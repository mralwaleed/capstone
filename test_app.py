import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from models import setup_db
from app import create_app
from flask import request, _request_ctx_stack ,abort
from functools import wraps
from jose import jwt
from urllib.request import urlopen


assistance_token = os.environ.get("assistance_token")

director_token = os.environ.get('director_token')

producer_token =  os.environ.get('producer_token')



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
                "Authorization": 'bearer '+producer_token})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertTrue(data['success'])

    # create actor with unauthorized token
    def test_create_actor_with_invalid_token(self):
        res = self.client().post(
            '/actors',
            json=self.new_actor,
             headers=
             {"Authorization": 'bearer '+assistance_token})

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
                "Authorization": 'bearer '+producer_token})
        res = json.loads(response.data)

        self.assertEqual(response.status_code, 200)
        self.assertTrue(res['success'])

    # create movie with unauthorized token
    def test_create_movie_with_invalid_token(self):

        response = self.client().post(
            '/movies',
            json=self.new_movie,
            headers={
                "Authorization": 'bearer '+director_token})
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
            headers={"Authorization": 'bearer '+assistance_token})
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
            headers={"Authorization": 'bearer '+assistance_token})
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
                "Authorization": 'bearer '+producer_token})
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
                "Authorization": 'bearer '+assistance_token})
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
                "Authorization": 'bearer '+producer_token})
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
                "Authorization": 'bearer '+assistance_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    '''
    Test DELETE actors and movies
    '''

    ''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

    def test_delete_actor_with_valid_token(self):

        res = self.client().delete('/actors/6',
                                   headers={"Authorization": 'bearer '+producer_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_delete_actor_with_invalid_token(self):

        res = self.client().delete(
            '/actors/5',
            headers={
                "Authorization": 'bearer '+assistance_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)

    def test_delete_movie_with_valid_token(self):

        res = self.client().delete('/movies/9',
                                   headers={"Authorization": 'bearer '+producer_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertTrue(data["success"])

    def test_delete_movie_with_invalid_token(self):

        res = self.client().delete(
            '/movies/6',
            headers={
                "Authorization": 'bearer '+assistance_token})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)


if __name__ == "__main__":
    unittest.main()
