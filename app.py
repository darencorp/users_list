from flask import Flask
from flask_cors import CORS

from src.v1.routes import api_v1

app = Flask(__name__)
cors = CORS(app, resources={'*': {'origins': '*'}})

app.register_blueprint(api_v1, url_prefix='/v1')
