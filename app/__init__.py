from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bootstrap import Bootstrap

#setup/config
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'Heroku_Database_URL'
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
Bootstrap(app)



from app import routes