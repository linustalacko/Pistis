
from app import app
from flask import render_template

from app.forms import Email
from app.models import db, LoginForm
from sqlalchemy import desc


@app.route('/')
def landing_page():
    return render_template('landing.html')

@app.route('/more/', methods = ['GET', 'POST'])
def learn_more():
    form = Email()
    if form.validate_on_submit():
        bot = LoginForm(username=form.username.data)
        db.session.add(bot)
        db.session.commit()
    else:
        print("Sorry! This email has already subscribed!")
    return render_template('more.html', form=form)
 
@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

@app.route('/hugo')
def hugo():
    return "Hugo is an idiot"