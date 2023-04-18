from flask import Flask 
app = Flask(__name__)
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)

app.config['SQLAL_DATABASE_URI'] = 'sqlite:///data.db'

app.route('/drinks')
def get_drinks():
    return ("book": "book data")