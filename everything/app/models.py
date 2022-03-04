from app import db
import os

class LoginForm(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)


if not os.path.exists("dbdir.db"):
    db.create_all()