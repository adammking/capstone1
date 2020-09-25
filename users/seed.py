from social_models import db, social_connect_db, User, Likes, Follows
from app import app


db.drop_all()
db.create_all()
