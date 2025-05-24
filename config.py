import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///follower_tracker.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False