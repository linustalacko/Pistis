from ensurepip import bootstrap
import os


from flask import app
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    db_name="emailist"
    SQLALCHEMY_DATABASE_URI = 'sqlite:///dbdir.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = True
