from app import create_app, db
from app.models import User, Snippet

app = create_app()

# Shell Context Processor in order to use flask shell command
@app.shell_context_processor
def make_shell_context():
    return{'db':db, 'User': User, 'Snippet': Snippet}
    