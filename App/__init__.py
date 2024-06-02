from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager
from .resources.example import ExampleResource 


def create_app():
    app = Flask(__name__)
    app.config['JWT_SECRET_KEY'] = 'your_secret_key'
    api = Api(app)
    jwt = JWTManager(app)

    api.add_resource(ExampleResource, '/example')
    # Import and add your resources here
    # from .resources.example import ExampleResource
    # api.add_resource(ExampleResource, '/example')

    return app