from flask import Flask

# create function and initialize flask
def create_app():
    app = Flask(__name__)
    # secure the cookies in the session
    app.config['SECRET_KEY'] = 'dupsko'

    return app
