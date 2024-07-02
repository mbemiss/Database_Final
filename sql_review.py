from typing import Text
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app import db # Assuming your Flask app is in a file named app.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy() # Initialize SQLAlchemy instance

class Ebook(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(255), unique=True)
    content = Column(String(Text)) # Optional, adjust data type if needed
    reviews = relationship("Review", backref="ebook") # One-to-Many relationship

class Review(db.Model):
    id = Column(Integer, primary_key=True)
    ebook_id = Column(Integer, ForeignKey("ebooks.id"))
    user_id = Column(Integer) # Optional
    content = Column(String(Text))
    rating = Column(Integer)