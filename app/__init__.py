from flask import Flask
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__, template_folder='../templates')
app.config['SECRET_KEY'] = 'your_secret_key'
csrf = CSRFProtect(app)

from app import routes
