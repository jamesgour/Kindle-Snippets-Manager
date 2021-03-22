# Useful code snippets using cmd & python

# Start Flask
flask run

# Database Code Snippets

# Initialize database first time 
# (e.g. after deleting migrations & app.db to start over)
flask db init 

# After any change to models.py database schema
flask db migrate -m "users table"
flask db upgrade

# Instead of having to import everything and creation application context
flask shell

# Erase data from tables in db
flask shell
db.drop_all()
# Then, delete migrations folder
db.create_all()
# Exit flask shell
flask db init

