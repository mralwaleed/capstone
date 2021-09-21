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
curl --location --request GET 'https://mralwaleed.herokuapp.com/movies' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6IjI2Qm9uRHEzcnl6YnA0WERwQUJyUCJ9.eyJpc3MiOiJodHRwczovL2Rldi01dmtxdXd4Ni51cy5hdXRoMC5jb20vIiwic3ViIjoiYXV0aDB8NjExM2VlZmViMTUxY2UwMDY4NWU4MGM3IiwiYXVkIjoiY2Fwc3RvbmUiLCJpYXQiOjE2MzIxNzc0NjgsImV4cCI6MTYzMjI2Mzg2OCwiYXpwIjoiNmRHY3V4NlhIY3lMMXRPNU5WWVR5S3dEcTJTOWNyb00iLCJzY29wZSI6IiIsInBlcm1pc3Npb25zIjpbIkdFVDphY3RvcnMiLCJHRVQ6bW92aWVzIl19.IfFLWNX2SSkAFvILsvmh6w3uWnRfIUSULvL5-1VcMBvN_DeCPk4l2WsG6Srt-8XCn6fEkb9ylXT5ygpVLJwUqcj50dVVMpfMPEuehp9260vphr2fWf8i7CKmos_RVtn1nHVqY84HinUL2PiUyDGTaSFRyBcNSlfOC5mIBCl4dpCWUh-MBAGO1mbk-PRUHCU84VSJn6abbn3u2KbJOdAILk3g9hU1rjZY3dRfMphum3tjL44dpRedj9YIvsIxe7Vc_fGIik75tG-VVZmIK67_hHxBtkJkaul4GFObFBjOkz2PwdEQuEjKiK1MEa5eMn7uaNZCqbw3TOcI4c8MNjANGg'
```
```bash
{
    "movies": [
        {
            "id": 8,
            "release date": "Thu, 21 Dec 2023 12:00:00 GMT",
            "title": "The Last Man Standing"
        },
        {
            "id": 9,
            "release date": "Thu, 21 Dec 2023 12:00:00 GMT",
            "title": "My ex wife"
        },
        {
            "id": 12,
            "release date": "Thu, 21 Dec 2023 12:00:00 GMT",
            "title": "The last ship"
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
curl --location --request GET 'https://castingagencyfsnd.herokuapp.com/actors' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGQ0NmQwNDdjOTBjYzU3MjZiNGIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5OTE2NTgzLCJleHAiOjE1OTAwMDI5ODIsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJnZXQ6YWN0b3JzIiwiZ2V0Om1vdmllcyJdfQ.gkuByEJFJPO8_8DoRukebvaislj1fpf0--nbmGz6SIQkilOh5UzjSsCoTMUz1w2C6jVOgVZrIqraHQyvWyVorhmiG5EKLpBsm2R3UEzlDs84hjoyYT0-AFAqb2Q2uXpqjPUpsl2-DljPxSeeQkG6Jntn8kTfAwwhqWtBNXeV9-sF4-32nu5zXtsh8CQepDWVv-CBlQ3Cv8A8yBrAd1JX3TiZS3AX5_iHg5XPaZQ2gX5sRBQMLtLsFMWVTkxBUvjQfDNjmzDYfFGzfmQB1xKNJ0wVMwhJyoFXy84XgqZVr5rv4AfPcFw8Jh5bzBh3YmVODVIyyJJYlJFeRnWJN5vayw'
```
```bash
{
    "actors": [
        {
            "age": 21,
            "gender": "Female",
            "id": 6,
            "name": "Elsa Montanha"
        },
        {
            "age": 21,
            "gender": "Male",
            "id": 12,
            "name": "Onnys Menete"
        }
    ],
    "success": true
}
```

POST '/movies'
- Post a movie and persist it to the database
- Request Arguments: A JSON with title, release_date  ```eg:{ "title":"X-Man", "release_date": "12-21-23 12:00 pm"}```
- Authentication: Only the executive Executive Producer
- Returns : A JSON with success value and the id of the posted movie
```bash
curl --location --request POST 'https://castingagencyfsnd.herokuapp.com/movies' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGY2YzZhMzA1NDBjZDk4NGUxY2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5OTE5MTU1LCJleHAiOjE1OTAwMDU1NTQsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Mxu-gON7l678IWTtIIjG9n2i842VdiSYz0IQ_ouEBXm0MipLvpM33A8Dmi-rJklgTBjPmaUPq_6h8mt2Kxa4LQiGlhKofWBdV2RBQ7znkRWVGGIczv21MdbcFdhvDcm7Wtsg_sMEbJq5oMF7BGml7O-2UG8s2HwIx1Z8HafNRHg0YiCumuFWaWIpi8BSn9B07du8Vf4JryXml_jTdicTwO3pnV0sZfNILBDM8D5M9Ohre_AP4CZ6viMEc3UNRhaqOMmoCOf3R6sTsfl7vnQBGKdaq2YsFjWVIuk8-GKisS3270BTDeXIitYpdumxEQ2_QPp64770czF7iXQHmclAFw' \
--header 'Content-Type: application/json' \
--data-raw '{ "title":"X-Man", "release_date": "12-21-23 12:00 pm"}'
```
```bash
{
    "movie id": 13,
    "success": true
}
```
POST '/actors'
- Post actor and persist it to the database
- Request Arguments: A JSON with name, age and gender  ```eg:{"name":"Lazaro Neto","age": 21,
"gender":"M"}```
- Authentication: Casting Director and  Executive Producer 
- Returns : A JSON with success value and the id of the posted actor
```bash
curl --location --request POST 'https://castingagencyfsnd.herokuapp.com/actors' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGUxYzZhMzA1NDBjZDk4NGRiNmIiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5OTE5NzIwLCJleHAiOjE1OTAwMDYxMTksImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZ2V0OmFjdG9ycyIsImdldDptb3ZpZXMiLCJwYXRjaDphY3RvcnMiLCJwYXRjaDptb3ZpZXMiLCJwb3N0OmFjdG9ycyJdfQ.IopxGPMinZW1r_cjsmGIoTNxKXjUUwHpyU5VdOwRhsVYShULI7LufJfIB1AwdXPdZZsmKQG1-sHbLIRf3Tx3BngI90wiYX6lF34hbi75IXAd7VwKnbqpe-nfY08YNtxwpflNnblLSw3EKhdB-Lngjzx04NwO8LfK8bLJIP8GaHj2NJW8z8umuif9CJgdzSFgUpCKZq2bXnMM36dQpyBdr6Jast7lBED_7cMRRslli8vZCc3W4cplDtqVZIWDQOcrW73ZDppJplIOa__Ju_diOFhvcMqb3xGzNdB0PqUAd7WGYwnr01LvLHqPGGXiz_NPZ9YaU5gqm4puceSSDf3IDg' \
--header 'Content-Type: application/json' \
--data-raw '{"name":"Lazaro Neto","age": 21,
"gender":"Male"}'
```
```
{
    "actor id": 13,
    "success": true
}
```
PATCH '/movies/<int:movie_id>'
- Updates a movie data based on the id 
- Request Arguments: A JSON with title and a release_date ```eg: { "title":"The Movie", "release_date": "12-21-25 12:00 pm"}```
- Authentication: Casting Director and  Executive Producer 
- Returns : A JSON with success value and the id of the updated movie
```bash
curl --location --request PATCH 'https://castingagencyfsnd.herokuapp.com/movies/2' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGY2YzZhMzA1NDBjZDk4NGUxY2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5OTE5MTU1LCJleHAiOjE1OTAwMDU1NTQsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Mxu-gON7l678IWTtIIjG9n2i842VdiSYz0IQ_ouEBXm0MipLvpM33A8Dmi-rJklgTBjPmaUPq_6h8mt2Kxa4LQiGlhKofWBdV2RBQ7znkRWVGGIczv21MdbcFdhvDcm7Wtsg_sMEbJq5oMF7BGml7O-2UG8s2HwIx1Z8HafNRHg0YiCumuFWaWIpi8BSn9B07du8Vf4JryXml_jTdicTwO3pnV0sZfNILBDM8D5M9Ohre_AP4CZ6viMEc3UNRhaqOMmoCOf3R6sTsfl7vnQBGKdaq2YsFjWVIuk8-GKisS3270BTDeXIitYpdumxEQ2_QPp64770czF7iXQHmclAFw' \
--header 'Content-Type: application/json' \
--data-raw '{ "title":"The Movie", "release_date": "12-21-25 12:00 pm"}'
```
```
{
    "movie_id": 2,
    "success": true
}
```
PATCH '/actors/<int:actor_id>'
- Updates an actor data based on the id 
- Request Arguments: A JSON with name, age and gender ```eg:{"name":"Alex Jordan","age": 21,
 "gender":"Female"}```
- Authentication: Casting Director and  Executive Producer 
- Returns : A JSON with success value and the id of the updated actor
```bash
curl --location --request PATCH 'https://castingagencyfsnd.herokuapp.com/actors/2' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGY2YzZhMzA1NDBjZDk4NGUxY2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5OTE5MTU1LCJleHAiOjE1OTAwMDU1NTQsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Mxu-gON7l678IWTtIIjG9n2i842VdiSYz0IQ_ouEBXm0MipLvpM33A8Dmi-rJklgTBjPmaUPq_6h8mt2Kxa4LQiGlhKofWBdV2RBQ7znkRWVGGIczv21MdbcFdhvDcm7Wtsg_sMEbJq5oMF7BGml7O-2UG8s2HwIx1Z8HafNRHg0YiCumuFWaWIpi8BSn9B07du8Vf4JryXml_jTdicTwO3pnV0sZfNILBDM8D5M9Ohre_AP4CZ6viMEc3UNRhaqOMmoCOf3R6sTsfl7vnQBGKdaq2YsFjWVIuk8-GKisS3270BTDeXIitYpdumxEQ2_QPp64770czF7iXQHmclAFw' \
--header 'Content-Type: application/json' \
--data-raw '{"name":"Alex Jordan","age": 21,
 "gender":"Female"}'
```
```
{
    "actor id": 2,
    "success": true
}
```

DELETE '/movies/<int:movie_id>'
- Remove persistentle a movie from the database based on id 
- Request Arguments: id of the movie eg:'/movies/1'
- Returns: A JSON with success value and the id of the deleted movie
```bash
curl --location --request DELETE 'https://castingagencyfsnd.herokuapp.com/movies/2' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGY2YzZhMzA1NDBjZDk4NGUxY2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5OTE5MTU1LCJleHAiOjE1OTAwMDU1NTQsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Mxu-gON7l678IWTtIIjG9n2i842VdiSYz0IQ_ouEBXm0MipLvpM33A8Dmi-rJklgTBjPmaUPq_6h8mt2Kxa4LQiGlhKofWBdV2RBQ7znkRWVGGIczv21MdbcFdhvDcm7Wtsg_sMEbJq5oMF7BGml7O-2UG8s2HwIx1Z8HafNRHg0YiCumuFWaWIpi8BSn9B07du8Vf4JryXml_jTdicTwO3pnV0sZfNILBDM8D5M9Ohre_AP4CZ6viMEc3UNRhaqOMmoCOf3R6sTsfl7vnQBGKdaq2YsFjWVIuk8-GKisS3270BTDeXIitYpdumxEQ2_QPp64770czF7iXQHmclAFw' \
--data-raw ''
```
```
{
    "id": 2,
    "success": true
}
```
DELETE '/actors/<int:actor_id>'
- Remove persistentle an actor from the database based on id 
- Request Arguments: id of the actor eg:'/actors/1'
- Returns: A JSON with success value and the id of the deleted actror 
```bash
curl --location --request DELETE 'https://castingagencyfsnd.herokuapp.com/actors/12' \
--header 'Authorization: Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCIsImtpZCI6InNwVTk1eGZkR0hXWkZ2RDVvRzU0TSJ9.eyJpc3MiOiJodHRwczovL3Byb2plY3Rmc25kLmF1dGgwLmNvbS8iLCJzdWIiOiJhdXRoMHw1ZWMyZGY2YzZhMzA1NDBjZDk4NGUxY2MiLCJhdWQiOiJjYXN0aW5nIiwiaWF0IjoxNTg5OTE5MTU1LCJleHAiOjE1OTAwMDU1NTQsImF6cCI6IkYwOWQ3Nm1IVlhFczZnME05VG12cUZEN1VBNXV2QjJFIiwic2NvcGUiOiIiLCJwZXJtaXNzaW9ucyI6WyJkZWxldGU6YWN0b3JzIiwiZGVsZXRlOm1vdmllcyIsImdldDphY3RvcnMiLCJnZXQ6bW92aWVzIiwicGF0Y2g6YWN0b3JzIiwicGF0Y2g6bW92aWVzIiwicG9zdDphY3RvcnMiLCJwb3N0Om1vdmllcyJdfQ.Mxu-gON7l678IWTtIIjG9n2i842VdiSYz0IQ_ouEBXm0MipLvpM33A8Dmi-rJklgTBjPmaUPq_6h8mt2Kxa4LQiGlhKofWBdV2RBQ7znkRWVGGIczv21MdbcFdhvDcm7Wtsg_sMEbJq5oMF7BGml7O-2UG8s2HwIx1Z8HafNRHg0YiCumuFWaWIpi8BSn9B07du8Vf4JryXml_jTdicTwO3pnV0sZfNILBDM8D5M9Ohre_AP4CZ6viMEc3UNRhaqOMmoCOf3R6sTsfl7vnQBGKdaq2YsFjWVIuk8-GKisS3270BTDeXIitYpdumxEQ2_QPp64770czF7iXQHmclAFw' \
--data-raw ''
```
```
{
    "id": 12,
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

The application is hosted by heroku under the url: ['heroku app'](https://mralwaleed.herokuapp.com/)
In the `test_app.py` you can find a convenient script to get the need access token. 

