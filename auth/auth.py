from flask import Flask, render_template, request, flash, redirect, session, g, Blueprint
from users.models import social_db, social_connect_db, User, Follows, Post
from forms import UserAddForm, LoginForm
from sqlalchemy.exc import IntegrityError

auth_bp = Blueprint('auth_bp', __name__,
                          template_folder='templates')

CURR_USER_KEY = "curr_user"

@auth_bp.before_request
def add_user_to_g():
    """If we're logged in, add curr user to Flask global."""

    if CURR_USER_KEY in session:
        g.user = User.query.get(session[CURR_USER_KEY])

    else:
        g.user = None


def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@auth_bp.route('/signup', methods=["GET", "POST"])
def signup():
    """Handle user signup.

    Create new user and add to DB. Redirect to home page.

    If form not valid, present form.

    If there already is a user with that username: flash message
    and re-present form.
    """
    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]
    form = UserAddForm()

    if form.validate_on_submit():
        try:
            user = User.signup(
                username=form.username.data,
                password=form.password.data
            )

            social_db.session.commit()

        except IntegrityError as e:
            flash("Username already taken", 'danger')
            return render_template('auth/signup.html', form=form)

        do_login(user)

        return redirect("/users")

    else:
        return render_template('auth/signup.html', form=form)


@auth_bp.route('/login', methods=["GET", "POST"])
def login():
    """Handle user login."""

    form = LoginForm()

    if form.validate_on_submit():
        user = User.authenticate(form.username.data,
                                 form.password.data)

        if user:
            do_login(user)
            flash(f"Hello, {user.username}!", "success")
            return redirect("/users")

        flash("Invalid credentials.", 'danger')

    return render_template('/auth/login.html', form=form)


@auth_bp.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()

    flash("You have successfully logged out.", 'success')
    return redirect("/login")


@auth_bp.route('/')
def welcome_page():
    return render_template('welcome.html')
