import os

from flask import Flask 

from .extensions import db
from .routes import main

def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
    # postgres://moviesdb_1ose_user:ENKg2YBKjLKhnPf8cgiQZhmXUvgSF2Sl@dpg-cig4r3dgkuvojjfjdut0-a.oregon-postgres.render.com/moviesdb_1ose

    db.init_app(app)

    app.register_blueprint(main)

    return app