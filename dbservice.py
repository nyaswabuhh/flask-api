from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS

app= Flask (__name__)
CORS(app)

app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:simbapos%402019@localhost:5432/flask_api'


app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False


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


    

