from app import create_app, db
from app.models import User, Snippet

app = create_app()

@app.shell_context_processor
def make_shell_context():
    """Creates the shell context for the app when using flask shell command"""
    return{'db':db, 'User': User, 'Snippet': Snippet}
    