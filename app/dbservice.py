from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS
from flask_jwt_extended import JWTManager, create_access_token
import os

app= Flask (__name__)
CORS(app)
app.config["JWT_SECRET_KEY"]="sirikuu"
app.config["JWT_TOKEN_LOCATION"] = ["headers"]
jwt=JWTManager(app)


# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:simbapos%402019@localhost:5432/flask_api'
# app.config['SQLALCHEMY_DATABASE_URI']='sqlite://database/flask_api.db'

# app = Flask(__name__)

basedir = os.path.abspath(os.path.dirname(__file__))
print("basedir ------", basedir)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database', 'flask_api.db')

db = SQLAlchemy(app)


class Product(db.Model):
    __tablename__='products'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False)
    bp=db.Column(db.Float,nullable=False)
    sp=db.Column(db.Float, nullable=False)

    sales=db.relationship("Sale", backref="product")

class Sale(db.Model):
    __tablename__="sales"
    id=db.Column(db.Integer, primary_key=True)
    pid=db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)
    quantity=db.Column(db.Integer, nullable=False)
    created_at=db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

  


class User(db.Model):
    __tablename__="users"
    id=db.Column(db.Integer, primary_key=True)
    full_name=db.Column(db.String, nullable=False)
    email=db.Column(db.String, nullable=False)
    password=db.Column(db.String, nullable=False)


    

class Payment(db.Model):
    __tablename__="payments"
    id=db.Column(db.Integer, primary_key=True)
    sale_id=db.Column(db.Integer, nullable=True)
    trans_code=db.Column(db.String, nullable=True)
    mrid=db.Column(db.String, nullable=False)
    crid=db.Column(db.String, nullable=False)
    amount=db.Column(db.Integer, nullable=True)
    created_at=db.Column(db.DateTime, default=datetime.utcnow)