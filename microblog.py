from app import app

from app import app, db
from app.models import Email

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Email': Email}