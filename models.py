from exts import db
from sqlalchemy import ForeignKey


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)


class Magazine(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    collected = db.Column(db.Boolean)


class Article(db.Model):
    id = db.Column(db.Integer, ForeignKey('magazine.id'), primary_key=True)
    index = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text)
    pageNum = db.Column(db.Integer)
