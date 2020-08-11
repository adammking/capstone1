import os

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension

from crisis_models import db, crisis_connect_db
from social_models import db, social_connect_db

CURR_USER_KEY = "curr_user"

app = Flask(__name__)

# Get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.
app.config['SQLALCHEMY_DATABASE_URI'] = (
    os.environ.get('DATABASE_URL', 'postgres:///capstone1'))

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = True
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")
toolbar = DebugToolbarExtension(app)

crisis_connect_db(app)
social_connect_db(app)

########################## Login/logout/register routes ###############################

@app.before_request
def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
        return True
    
    return False

@app.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If the there already is a user with that username: flash message
    and re-present form.
    """

    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data,
            )
            db.session.commit()

        except IntegrityError:
            flash("Username already taken", 'danger')
            return render_template('users/signup.html', form=form)

        do_login(user)

        return redirect("/")

    else:
        return render_template('users/signup.html', form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/")

        flash("Invalid credentials.", 'danger')

    return render_template('users/login.html', form=form)


@app.route('/logout')
def logout():
    """Handle logout of user."""

    # IMPLEMENT THIS
    if do_logout():
        flash(f"Log Out Successful!", "success")
        return redirect("/login")

    
    return redirect("/")

######################################### User profile/community routes #############################

@app.route('/users')

@app.route('/users/<user_id>')

@app.route('/user/posts')


######################################## Depression info routes #######################################

@app.route('/depression')
def show_depr_info():
    return render_template('/depression/info.html')#need to make  
@app.route('/depression/referrals')
def show_depr_referrals():
    return render_template('/depression/referrals.html')#need to make  

@app.route('/depression/treatment')
def show_depr_treatments():
    return render_template('/depression/treatment.html')#need to make  


######################################## Cheer me up routes ################################################

@app.route('/cheer-me-up')
def show_cheer_me_up():
    if CURR_USER_KEY in session:
        return render_template('cheer-me-up.html')#need to make  

    else:
        flash(f"Please login or register to use Cheer-me-up", "danger")
        return redirect('/')



######################################## Crisis program routes ############################################

"""@app.route('/crisis/self')

@app.route('/crisis/others')

@app.route('/crisis/internal')

@app.route('/crisis/substance')

@app.route('/crisis/referrals')"""