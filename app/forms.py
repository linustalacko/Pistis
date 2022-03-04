from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from flask import request

class Email(FlaskForm):
    username = StringField("username", validators=[DataRequired()], render_kw={"placeholder": "Email..."})
    submit = SubmitField('Remind Me')

