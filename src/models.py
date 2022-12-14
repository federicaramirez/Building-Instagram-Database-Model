import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    firstname = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    follower = relationship("Follower", uselist=False, backref="user")
    post = relationship("Post", uselist=False, backref="user")
    comment = relationship("Comment", uselist=False, backref="user")

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user_to_id = Column(Integer, ForeignKey('user.id'), nullable=False)

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'), nullable=False)
    media_id= Column(Integer, ForeignKey('user.id'), nullable=False)
    comment = relationship("Comment", uselist=False, backref='post')
    media = relationship("Media", uselist=False, backref='post')

class Comment(Base): 
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(250), nullable=False)

    autor_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    post_id =  Column(Integer, ForeignKey('post.id'), nullable=False)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type_media = Column(String, nullable=False)
    url = Column(String, nullable=False)
    
    post_id = Column(Integer, ForeignKey('post.id'), nullable=False)


try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e