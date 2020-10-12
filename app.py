import os

from flask import Flask, render_template, request, flash, redirect, session, g
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from crisis.program import crisis, Crisis_Program
from crisis.models import crisis_db, crisis_connect_db, Mental_Health_Center, County, Zip_Code
from users.models import social_db, social_connect_db, User, Follows, Post
from forms import UserAddForm, LoginForm, CountyReferralForm, ZipReferralForm, PostAddForm, UserEditForm


from depression.depression import depression_bp
from users.users import users_bp
from auth.auth import auth_bp
from crisis.crisis import crisis_bp

CURR_USER_KEY = "curr_user"

app = Flask(__name__)


app.register_blueprint(depression_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)
app.register_blueprint(crisis_bp)

# Get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres:///capstone1')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")

crisis_connect_db(app)
social_connect_db(app)
program = Crisis_Program
mhc = Mental_Health_Center()




@app.route('/cheer-me-up')
def show_cheer_me_up():

    return render_template('cheer-me-up.html')
       

