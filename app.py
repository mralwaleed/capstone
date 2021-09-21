import os
from flask import Flask, request, abort, jsonify
from models import setup_db, Movies, Actors
from flask_cors import CORS
from auth.auth import requires_auth, AuthError


def create_app(test_config=None):

    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS')
        return response

    @app.route('/')
    def get_greeting():
        excited = os.environ.get('EXCITED')
        print(excited)
        greeting = "Hello"
        if excited == "true":
            greeting = greeting + "!!!!!"
        return greeting

    @app.route('/coolkids')
    def be_cool():
        return "Be cool, man, be coooool! You're almost a FSND grad!"

    @app.route('/actors', methods=['GET'])
    @requires_auth('GET:actors')
    def retrieve_actors(payload):

        all_actors = Actors.query.order_by(Actors.id).all()

        actors = [actor.format() for actor in all_actors]
  

        if len(all_actors) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'actors': actors
        })

    @app.route('/movies', methods=['GET'])
    @requires_auth('GET:movies')
    def retrieve_movies(payload):
        print("yesy")

        all_movie = Movies.query.order_by(Movies.id).all()

        movies =[movie.format() for movie in all_movie]
        
        if len(all_movie) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'movies': movies
        })

    @app.route('/actors', methods=['POST'])
    @requires_auth('POST:actors')
    def create_actors(payload):
        body = request.get_json()

        new_name = body.get('name', None)
        new_age = body.get('age', None)
        new_gender = body.get('gender', None)
        try:
            if not body:
                abort(400)

            actor = Actors(name=new_name, age=new_age, gender=new_gender)
            actor.insert()

            return jsonify({
                'success': True,
                'created': actor.id
            })

        except Exception as e:
            print(e)
            abort(422)

    @app.route('/movies', methods=['POST'])
    @requires_auth('POST:movies')
    def create_movies(payload):
        body = request.get_json()

        new_title = body.get('title', None)
        new_date = body.get('release_date', None)
        try:
            if not body:
                abort(400)

            movie = Movies(title=new_title, release_date=new_date)
            movie.insert()

            return jsonify({
                'success': True,
                'created': movie.id
            })

        except Exception as e:
            print(e)
            abort(422)

    @app.route('/movies/<int:Movies_id>', methods=['DELETE'])
    @requires_auth('DELETE:movies')
    def delete_movies(payload, Movies_id):
        try:
            movie = Movies.query.filter(
                Movies.id == Movies_id).one_or_none()

            if Movies is None:
                abort(404)

            movie.delete()

            return jsonify({
                'success': True,
                'deleted': Movies_id
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.route('/actors/<int:Actors_id>', methods=['DELETE'])
    @requires_auth('DELETE:actors')
    def delete_actors(payload, Actors_id):
        try:
            actor = Actors.query.filter(
                Actors.id == Actors_id).one_or_none()

            if actor is None:
                abort(404)

            actor.delete()

            return jsonify({
                'success': True,
                'deleted': Actors_id
            })
        except Exception as e:
            print(e)
            abort(422)

    @app.route('/actors/<int:Actors_id>', methods=['PATCH'])
    @requires_auth('PATCH:actors')
    def update_actor(payload, Actors_id):

        body = request.get_json()

        try:
            actor = Actors.query.filter(Actors.id == Actors_id).one_or_none()
            if actor is None:
                abort(404)

            if 'name' in body and 'age' in body:
                actor.name = body.get('name')
                actor.age = body.get('age')

            actor.update()

            return jsonify({
                'success': True,
            })
        except BaseException:
            abort(400)

    @app.route('/movies/<int:Movies_id>', methods=['PATCH'])
    @requires_auth('PATCH:movies')
    def update_movie(payload, Movies_id):

        body = request.get_json()

        try:
            movie = Movies.query.filter(Movies.id == Movies_id).one_or_none()
            if movie is None:
                abort(404)

            if 'title' in body and 'release_date' in body:
                movie.title = body.get('title')
                movie.release_date = body.get('release_date')

            movie.update()

            return jsonify({
                'success': True,
            })
        except BaseException:
            abort(400)

    # Error Handling

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "unprocessable"
        }), 422

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "resource not found"
        }), 404

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": 'Internal Server Error'
        }), 500

    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": 'Bad Request'
        }), 400

    @app.errorhandler(401)
    def unauthorized(error):
        return jsonify({
            "success": False,
            "error": 401,
            "message": 'Unathorized'
        }), 401

    @app.errorhandler(AuthError)
    def process_AuthError(error):
        response = jsonify(error.error)
        response.status_code = error.status_code
        return response

    return app


app = create_app()

if __name__ == '__main__':
    app.run()
