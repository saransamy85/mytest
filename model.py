from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import sqlalchemy

app=Flask(__name__)

db=SQLAlchemy(app)

class User(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String())