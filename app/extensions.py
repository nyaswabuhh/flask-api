from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:simbapos%402019@localhost:5432/flask_api'
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite://database/flask_api.db'

# app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://myduka_user:simbapos2019@172.17.0.1:5432/myduka_api'
# CREATE USER myduka_user WITH PASSWORD 'Zdfdgdg#'
# GRANT CONNECT ON DATABASE myduka_api TO myduka_user;

# basedir = os.path.abspath(os.path.dirname(__file__))
# print("basedir ------", basedir)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database', 'flask_api.db')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_ECHO'] = True

db = SQLAlchemy(app)

app.config["JWT_SECRET_KEY"]= "sirikuu"
app.config["JWT_TOKEN_LOCATION"] = ["headers"]
CORS(app, resources={r"/*": {"origins": "*"}})