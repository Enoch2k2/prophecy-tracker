from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData
from dotenv import load_dotenv
from flask_migrate import Migrate
from flask_restful import Api
from flask_cors import CORS

import os

load_dotenv()

convention = {
    'pk': 'pk_%(table_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'ix': 'ix_%(table_name)s_%(column_0_name)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
}

metadata = MetaData(naming_convention=convention)

app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET")
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app=app, metadata=metadata)

migrate = Migrate(app=app, db=db)


api = Api(app=app)

CORS(app=app)