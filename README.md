# capstone
The motivation of this project is to practice the skills learned during the Udacity FullStack NanoDegree program. The basis of the app for companys who is responsible for creating movies and managing and assigning actors, executive producer can post movies and actors for casting director and casting assistant.

* Link to course click [here](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd0044)

* Link to course syllabus, click [here](https://bertelsmann-university.com/fileadmin/user_upload/Full_Stack_ND_Syllabus.pdf) 

## Content

1.  Motivation
2.  Getting Started
3.  Roles and Permissions
4.  API Documentation
5.  END Point Documentation
6.  Running tests
7.  Hosting

## Motivation

0. Python 3
1.  Database with  **postgres**  and  **sqlalchemy**  (`models.py`)
2.  API  with  **Flask**  (`app.py`)
3.  TDD  **Unittest**  (`test_app.py`)
4.  Authorization &  Authentification **Auth0**  (`auth.py`)
5.  Deployment on  **`Heroku`**



## Getting Started
**Requirements**

Install the necessary requirmenets by running:

``` bash
    pip install -r requirements.txt
```

**Running on local machine**
1. Open a terminal and cd to the project directory and install requirements:
``` bash
    cd ~/capstone
    # Then
    pip install -r requirements.txt
```
2. Set up your DATABASE_URL variable depending on OS:

``` bash
    export DATABASE_URL="{DATABASE_URL}"

    For Windows use:

    $env:DATABASE_URL="{DATABASE_URL}"
```

3. Run ALL three migration commands **ONLY** on you first set up:

``` bash
# Run the init command once
    python manage.py db init
    python manage.py db migrate
    python manage.py db upgrade

# Run the last 2 commands if/when you make changes to database structure
```


4. Set up FLASK_APP variable depending on OS:
``` bash
    export FLASK_APP=app.py

    For Windows use:

    $env:FLASK_APP="app.py"
```

5. To run the app use:
``` bash
    flask run
```


* By default, the app will run on http://127.0.0.1:5000/ 


## Roles and Permissions:
- Casting Assistant
    - Can view actors and movies
        - 'get:movies'
        - 'get:actors'    
 
- Casting Director
    - All permissions a Casting Assistant has and…
    - Add or delete an actor from the database
        - 'post:actors'
        - 'delete: actors'
    - Modify actors or movies
        - 'patch:actors'
        - 'patch:movies'


- Executive Producer
   - All permissions a Casting Director has and…
   - Add or delete a movie from the database
        - 'post:movies'
        - 'delete:movie'

## API Documentation


> **GET** '/movies'

 - Retrieves all the movies in the database and represents them as JSON.

> **GET** '/actors'

 - Gets all the actors in the database and presents them as JSON.

> **POST** '/movies/create'

 - Will produce a new movie in the database based on the JSON that is in the body of the request.

> **POST** '/actors/create'

  - Create a new actor in the database based on the JSON.

> **DELETE** '/movies/delete/int:movie_id'

 - Deletes the movie that compares to the Movie ID that is given into the URL.

> **DELETE** '/actors/delete/int:actor_id'

 - Deletes the actor that corresponds to the Actor ID that is passed into the URL.

> **UPDATE** '/actors/patch/int:actor_id'

 - Updates the actor that matches to the Actor ID that is given into the URL.

> **UPDATE** '/movies/patch/int:movie_id'

  - Updates the movie that matches to the movie ID that is given into the URL.


## Endpoints
- GET '/movies'
- GET '/actors'
- POST '/movies'
- POST '/actors'
- PATCH '/movies/<int:movie_id>'
- PATCH '/actors/<int:actor_id>'
- DELETE '/movies/<int:movie_id>'
- DELETE '/actors/<int:actor_id>'


GET '/movies'
- Fetches a dictionary of movies 
- Request Arguments: None
- Authentication: the roles that can acess are Casting Assistant, Casting Director and Executive Producer
- Returns: A JSON with list of movies objects, success value.

```bash
curl --location --request GET 'https://mralwaleed1.herokuapp.com/movies' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjI2Qm9uRHEzcnl6YnA0WERwQUJyUCJ9.eyJpc3MiOiJodHRwczovL2Rldi01dmtxdXd4Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjExM2VlZmViMTUxY2UwMDY4NWU4MGM3IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzIxNzc0NjgsImV4cCI6MTYzMjI2Mzg2OCwiYXpwIjoiNmRHY3V4NlhIY3lMMXRPNU5WWVR5S3dEcTJTOWNyb00iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbIkdFVDphY3RvcnMiLCJHRVQ6bW92aWVzIl19.IfFLWNX2SSkAFvILsvmh6w3uWnRfIUSULvL5-1VcMBvN_DeCPk4l2WsG6Srt-8XCn6fEkb9ylXT5ygpVLJwUqcj50dVVMpfMPEuehp9260vphr2fWf8i7CKmos_RVtn1nHVqY84HinUL2PiUyDGTaSFRyBcNSlfOC5mIBCl4dpCWUh-MBAGO1mbk-PRUHCU84VSJn6abbn3u2KbJOdAILk3g9hU1rjZY3dRfMphum3tjL44dpRedj9YIvsIxe7Vc_fGIik75tG-VVZmIK67_hHxBtkJkaul4GFObFBjOkz2PwdEQuEjKiK1MEa5eMn7uaNZCqbw3TOcI4c8MNjANGg'
```
```bash
{
    "movies": [
        {
            "id": 2,
            "release_date": "Sat, 05 Feb 1994 00:00:00 GMT",
            "title": "The Shawshank Redemption "
        },
        {
            "id": 3,
            "release_date": "Mon, 06 Nov 1972 00:00:00 GMT",
            "title": "The Godfather"
        },
        {
            "id": 4,
            "release_date": "Fri, 15 Mar 1957 00:00:00 GMT",
            "title": "12 Angry Men"
        }
    ],
    "success": true
}
```

GET '/actors'
- Fetches a dictionary of actors 
- Request Arguments: None
- Authentication: the roles that can acess are Casting Assistant, Casting Director and Executive Producer
- Returns: A JSON with list of actors objects, success value.
```bash
curl --location --request GET 'https://mralwaleed1.herokuapp.com/actors' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjI2Qm9uRHEzcnl6YnA0WERwQUJyUCJ9.eyJpc3MiOiJodHRwczovL2Rldi01dmtxdXd4Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjExM2VlZmViMTUxY2UwMDY4NWU4MGM3IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzIxNzc0NjgsImV4cCI6MTYzMjI2Mzg2OCwiYXpwIjoiNmRHY3V4NlhIY3lMMXRPNU5WWVR5S3dEcTJTOWNyb00iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbIkdFVDphY3RvcnMiLCJHRVQ6bW92aWVzIl19.IfFLWNX2SSkAFvILsvmh6w3uWnRfIUSULvL5-1VcMBvN_DeCPk4l2WsG6Srt-8XCn6fEkb9ylXT5ygpVLJwUqcj50dVVMpfMPEuehp9260vphr2fWf8i7CKmos_RVtn1nHVqY84HinUL2PiUyDGTaSFRyBcNSlfOC5mIBCl4dpCWUh-MBAGO1mbk-PRUHCU84VSJn6abbn3u2KbJOdAILk3g9hU1rjZY3dRfMphum3tjL44dpRedj9YIvsIxe7Vc_fGIik75tG-VVZmIK67_hHxBtkJkaul4GFObFBjOkz2PwdEQuEjKiK1MEa5eMn7uaNZCqbw3TOcI4c8MNjANGg'
```
```bash
{
    "actors": [
        {
            "age": 25,
            "gender": "male",
            "id": 1,
            "name": "Ali"
        },
        {
            "age": 28,
            "gender": "Female",
            "id": 2,
            "name": "sara"
        },
        {
            "age": 25,
            "gender": "male",
            "id": 3,
            "name": "Ali"
        },
        {
            "age": 24,
            "gender": "male",
            "id": 4,
            "name": "Khalid"
        },
        {
            "age": 23,
            "gender": "male",
            "id": 5,
            "name": "alwaleed"
        }
    ],
    "success": true
}
```

POST '/movies'
- Post a movie and persist it to the database
- Request Arguments: A JSON with title, release_date  ```{"title":"The Dark Knight", "release_date":"8/18/2008"}```
- Authentication: Only the executive Executive Producer
- Returns : A JSON with success value and the id of the posted movie
```bash
curl --location --request POST 'https://mralwaleed1.herokuapp.com/movies' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjI2Qm9uRHEzcnl6YnA0WERwQUJyUCJ9.eyJpc3MiOiJodHRwczovL2Rldi01dmtxdXd4Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjExMzBkNzA4ZTMxZDUwMDY5ZjhjODVjIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzIxNzUzMjMsImV4cCI6MTYzMjI2MTcyMywiYXpwIjoiNmRHY3V4NlhIY3lMMXRPNU5WWVR5S3dEcTJTOWNyb00iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbIkRFTEVURTphY3RvcnMiLCJERUxFVEU6bW92aWVzIiwiR0VUOmFjdG9ycyIsIkdFVDptb3ZpZXMiLCJQQVRDSDphY3RvcnMiLCJQQVRDSDptb3ZpZXMiLCJQT1NUOmFjdG9ycyIsIlBPU1Q6bW92aWVzIl19.Ce6_e2r49nlzmy0PV1N9hukRYoP9WweGTkySxDh4e2qjTFBI0DKSmvkLTHmbMC6L6ZinAjSjBb8i2b1SC7GOfV5qIPWXWmsPaNoHmxts-53QyZSmXtF4asRrPyFReolvEW1-BKdVJZ5K1LsfUzHHubOAK8TNX17OzBKB8416p0_ahPdSplS296HPECR2SHvjGiJKAlw8oD0p-eN8RBoMq2TD0XviHixCFN8l4D9NitB45bJ3b5oxO91vrczSMQyXVxSNFOrSo7w-BF9DZwp_Ep8LGKp7ZoT6cnfd0npfW9tH1Ng9mqOqDWw8xU_dB1v-vqWwyWNQEM8vCqKgiluG1Q' \
--header 'Content-Type: application/json' \
--data-raw '{"title":"The Dark Knight", "release_date":"8/18/2008"}'
```
```bash
{
    "created": 5,
    "success": true
}
```
POST '/actors'
- Post actor and persist it to the database
- Request Arguments: A JSON with name, age and gender  ```eg:{"name":"Saleh", "age":"43","gender":"male"}
- ```
- Authentication: Casting Director and  Executive Producer 
- Returns : A JSON with success value and the id of the posted actor
```bash
curl --location --request POST 'https://mralwaleed1.herokuapp.com/actors' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjI2Qm9uRHEzcnl6YnA0WERwQUJyUCJ9.eyJpc3MiOiJodHRwczovL2Rldi01dmtxdXd4Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjExMzBkNzA4ZTMxZDUwMDY5ZjhjODVjIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzIxNzUzMjMsImV4cCI6MTYzMjI2MTcyMywiYXpwIjoiNmRHY3V4NlhIY3lMMXRPNU5WWVR5S3dEcTJTOWNyb00iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbIkRFTEVURTphY3RvcnMiLCJERUxFVEU6bW92aWVzIiwiR0VUOmFjdG9ycyIsIkdFVDptb3ZpZXMiLCJQQVRDSDphY3RvcnMiLCJQQVRDSDptb3ZpZXMiLCJQT1NUOmFjdG9ycyIsIlBPU1Q6bW92aWVzIl19.Ce6_e2r49nlzmy0PV1N9hukRYoP9WweGTkySxDh4e2qjTFBI0DKSmvkLTHmbMC6L6ZinAjSjBb8i2b1SC7GOfV5qIPWXWmsPaNoHmxts-53QyZSmXtF4asRrPyFReolvEW1-BKdVJZ5K1LsfUzHHubOAK8TNX17OzBKB8416p0_ahPdSplS296HPECR2SHvjGiJKAlw8oD0p-eN8RBoMq2TD0XviHixCFN8l4D9NitB45bJ3b5oxO91vrczSMQyXVxSNFOrSo7w-BF9DZwp_Ep8LGKp7ZoT6cnfd0npfW9tH1Ng9mqOqDWw8xU_dB1v-vqWwyWNQEM8vCqKgiluG1Q' \
--header 'Content-Type: application/json' \
--data-raw '{"name":"Saleh", "age":"43","gender":"male"}'
```
```
{
    "created": 6,
    "success": true
}
```
PATCH '/movies/<int:movie_id>'
- Updates a movie data based on the id 
- Request Arguments: A JSON with title and a release_date ```eg: {"title":"Movies", "release_date": "11/24/2009"}``
- Authentication: Casting Director and  Executive Producer 
- Returns : A JSON with success value and the id of the updated movie
```bash
curl --location --request PATCH 'https://mralwaleed1.herokuapp.com/movies/2' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjI2Qm9uRHEzcnl6YnA0WERwQUJyUCJ9.eyJpc3MiOiJodHRwczovL2Rldi01dmtxdXd4Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjExMzBkNzA4ZTMxZDUwMDY5ZjhjODVjIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzIxNzUzMjMsImV4cCI6MTYzMjI2MTcyMywiYXpwIjoiNmRHY3V4NlhIY3lMMXRPNU5WWVR5S3dEcTJTOWNyb00iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbIkRFTEVURTphY3RvcnMiLCJERUxFVEU6bW92aWVzIiwiR0VUOmFjdG9ycyIsIkdFVDptb3ZpZXMiLCJQQVRDSDphY3RvcnMiLCJQQVRDSDptb3ZpZXMiLCJQT1NUOmFjdG9ycyIsIlBPU1Q6bW92aWVzIl19.Ce6_e2r49nlzmy0PV1N9hukRYoP9WweGTkySxDh4e2qjTFBI0DKSmvkLTHmbMC6L6ZinAjSjBb8i2b1SC7GOfV5qIPWXWmsPaNoHmxts-53QyZSmXtF4asRrPyFReolvEW1-BKdVJZ5K1LsfUzHHubOAK8TNX17OzBKB8416p0_ahPdSplS296HPECR2SHvjGiJKAlw8oD0p-eN8RBoMq2TD0XviHixCFN8l4D9NitB45bJ3b5oxO91vrczSMQyXVxSNFOrSo7w-BF9DZwp_Ep8LGKp7ZoT6cnfd0npfW9tH1Ng9mqOqDWw8xU_dB1v-vqWwyWNQEM8vCqKgiluG1Q' \
--header 'Content-Type: application/json' \
--data-raw '{ "title":"Movies", "release_date": "11/24/2009"}'
```
```
{
    "success": true
}
```
PATCH '/actors/<int:actor_id>'
- Updates an actor data based on the id 
- Request Arguments: A JSON with name and age ```eg:{"name":"Faisal", "age":"45"}```
- Authentication: Casting Director and  Executive Producer 
- Returns : A JSON with success value and the id of the updated actor
```bash
curl --location --request PATCH 'https://mralwaleed1.herokuapp.com/actors/1' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjI2Qm9uRHEzcnl6YnA0WERwQUJyUCJ9.eyJpc3MiOiJodHRwczovL2Rldi01dmtxdXd4Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjExMzBkNzA4ZTMxZDUwMDY5ZjhjODVjIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzIxNzUzMjMsImV4cCI6MTYzMjI2MTcyMywiYXpwIjoiNmRHY3V4NlhIY3lMMXRPNU5WWVR5S3dEcTJTOWNyb00iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbIkRFTEVURTphY3RvcnMiLCJERUxFVEU6bW92aWVzIiwiR0VUOmFjdG9ycyIsIkdFVDptb3ZpZXMiLCJQQVRDSDphY3RvcnMiLCJQQVRDSDptb3ZpZXMiLCJQT1NUOmFjdG9ycyIsIlBPU1Q6bW92aWVzIl19.Ce6_e2r49nlzmy0PV1N9hukRYoP9WweGTkySxDh4e2qjTFBI0DKSmvkLTHmbMC6L6ZinAjSjBb8i2b1SC7GOfV5qIPWXWmsPaNoHmxts-53QyZSmXtF4asRrPyFReolvEW1-BKdVJZ5K1LsfUzHHubOAK8TNX17OzBKB8416p0_ahPdSplS296HPECR2SHvjGiJKAlw8oD0p-eN8RBoMq2TD0XviHixCFN8l4D9NitB45bJ3b5oxO91vrczSMQyXVxSNFOrSo7w-BF9DZwp_Ep8LGKp7ZoT6cnfd0npfW9tH1Ng9mqOqDWw8xU_dB1v-vqWwyWNQEM8vCqKgiluG1Q' \
--header 'Content-Type: application/json' \
--data-raw '{"name":"Faisal", "age":"45"}'
```
```
{
    "success": true
}
```

DELETE '/movies/<int:movie_id>'
- Remove persistentle a movie from the database based on id 
- Request Arguments: id of the movie eg:'/movies/1'
- Returns: A JSON with success value and the id of the deleted movie
```bash
curl --location --request DELETE 'https://mralwaleed1.herokuapp.com/movies/2' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjI2Qm9uRHEzcnl6YnA0WERwQUJyUCJ9.eyJpc3MiOiJodHRwczovL2Rldi01dmtxdXd4Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjExMzBkNzA4ZTMxZDUwMDY5ZjhjODVjIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzIxNzUzMjMsImV4cCI6MTYzMjI2MTcyMywiYXpwIjoiNmRHY3V4NlhIY3lMMXRPNU5WWVR5S3dEcTJTOWNyb00iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbIkRFTEVURTphY3RvcnMiLCJERUxFVEU6bW92aWVzIiwiR0VUOmFjdG9ycyIsIkdFVDptb3ZpZXMiLCJQQVRDSDphY3RvcnMiLCJQQVRDSDptb3ZpZXMiLCJQT1NUOmFjdG9ycyIsIlBPU1Q6bW92aWVzIl19.Ce6_e2r49nlzmy0PV1N9hukRYoP9WweGTkySxDh4e2qjTFBI0DKSmvkLTHmbMC6L6ZinAjSjBb8i2b1SC7GOfV5qIPWXWmsPaNoHmxts-53QyZSmXtF4asRrPyFReolvEW1-BKdVJZ5K1LsfUzHHubOAK8TNX17OzBKB8416p0_ahPdSplS296HPECR2SHvjGiJKAlw8oD0p-eN8RBoMq2TD0XviHixCFN8l4D9NitB45bJ3b5oxO91vrczSMQyXVxSNFOrSo7w-BF9DZwp_Ep8LGKp7ZoT6cnfd0npfW9tH1Ng9mqOqDWw8xU_dB1v-vqWwyWNQEM8vCqKgiluG1Q' \
--data-raw ''
```
```
{
    "deleted": 1,
    "success": true
}
```
DELETE '/actors/<int:actor_id>'
- Remove persistentle an actor from the database based on id 
- Request Arguments: id of the actor eg:'/actors/1'
- Returns: A JSON with success value and the id of the deleted actror 
```bash
curl --location --request DELETE 'https://mralwaleed1.herokuapp.com/actors/12' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjI2Qm9uRHEzcnl6YnA0WERwQUJyUCJ9.eyJpc3MiOiJodHRwczovL2Rldi01dmtxdXd4Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjExMzBkNzA4ZTMxZDUwMDY5ZjhjODVjIiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzIxNzUzMjMsImV4cCI6MTYzMjI2MTcyMywiYXpwIjoiNmRHY3V4NlhIY3lMMXRPNU5WWVR5S3dEcTJTOWNyb00iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbIkRFTEVURTphY3RvcnMiLCJERUxFVEU6bW92aWVzIiwiR0VUOmFjdG9ycyIsIkdFVDptb3ZpZXMiLCJQQVRDSDphY3RvcnMiLCJQQVRDSDptb3ZpZXMiLCJQT1NUOmFjdG9ycyIsIlBPU1Q6bW92aWVzIl19.Ce6_e2r49nlzmy0PV1N9hukRYoP9WweGTkySxDh4e2qjTFBI0DKSmvkLTHmbMC6L6ZinAjSjBb8i2b1SC7GOfV5qIPWXWmsPaNoHmxts-53QyZSmXtF4asRrPyFReolvEW1-BKdVJZ5K1LsfUzHHubOAK8TNX17OzBKB8416p0_ahPdSplS296HPECR2SHvjGiJKAlw8oD0p-eN8RBoMq2TD0XviHixCFN8l4D9NitB45bJ3b5oxO91vrczSMQyXVxSNFOrSo7w-BF9DZwp_Ep8LGKp7ZoT6cnfd0npfW9tH1Ng9mqOqDWw8xU_dB1v-vqWwyWNQEM8vCqKgiluG1Q' \
--data-raw ''
```
```
{
    "deleted": 2,
    "success": true
}
```


## Running tests

Tests are prefixed with numbers to sort their test execution

Script for running tests:

```bash
dropdb capstone                                                      
createdb capstone
python test_app.py
```

## Hosting

The application is hosted by heroku under the url: ['heroku app'](https://mralwaleed1.herokuapp.com/)
In the `test_app.py` you can find a convenient script to get the need access token. 


