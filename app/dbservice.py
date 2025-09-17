from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from datetime import datetime
import os
from extensions import db

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