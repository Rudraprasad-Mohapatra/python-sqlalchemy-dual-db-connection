from flask import Flask

from .config import config_by_name

def create_app(env_name='development'):
    app = Flask(__name__)
    app.config.from_object(config_by_name[env_name])
    
    return app