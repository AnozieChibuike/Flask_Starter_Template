from flask import Flask
from config import Config
from flask_migrate import Migrate # type: ignore[import-untyped]
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flasksqlalchemybasemodel import db

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate = Migrate(app,db)
jwt = JWTManager(app)

from app import routes
from app import models
