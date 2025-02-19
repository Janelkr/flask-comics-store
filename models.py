from flask_login import UserMixin
from . import db


class User(db.Model, UserMixin):
  id = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(200), unique=True)
  password = db.Column(db.String(200))
  first_name = db.Column(db.String(200))


class Product(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  product_name = db.Column(db.String(100))
  price = db.Column(db.Float)
  image_path = db.Column(db.String(100))


