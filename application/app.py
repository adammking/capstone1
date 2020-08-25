import os

from flask import Flask, render_template, request, flash, redirect, session
from flask_debugtoolbar import DebugToolbarExtension
from sqlalchemy.exc import IntegrityError

from crisis_program import crisis, Crisis_Program
from crisis_models import db, crisis_connect_db, Mental_Health_Center, County, Zip_Code
from social_models import db, social_connect_db, User, Likes 
from forms import UserAddForm, LoginForm, CountyReferralForm, ZipReferralForm

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
program = Crisis_Program
mhc = Mental_Health_Center()
########################## Login/logout/register routes ###############################

def do_login(user):
    """Log in user."""

    session[CURR_USER_KEY] = user.id


def do_logout():
    """Logout user."""

    if CURR_USER_KEY in session:
        del session[CURR_USER_KEY]


@app.route('/signup', methods=["GET", "POST"])
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

            db.session.commit()

        except IntegrityError as e:
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
            return redirect("/users")

        flash("Invalid credentials.", 'danger')

    return render_template('/users/login.html', form=form)



@app.route('/logout')
def logout():
    """Handle logout of user."""

    do_logout()

    flash("You have successfully logged out.", 'success')
    return redirect("/login")


@app.route('/')
def welcome_page():
    return render_template('welcome.html')

######################################### User profile/community routes #############################


@app.route('/users')
def list_users():
    if CURR_USER_KEY in session:
        users = User.query.all()

        return render_template('/users/index.html', users=users)

    return redirect("/login")


@app.route('/users/<user_id>')
def show_user_profile():
    if CURR_USER_KEY in session:

        return render_template('/users/index.html')

    return redirect("/login")



@app.route('/users/posts')
def show_user_posts():
    if CURR_USER_KEY in session:

        return render_template('/users/index.html')

    return redirect("/login")




######################################## Depression info routes #######################################

@app.route('/depression')
def show_depr_info():

    return render_template('/depression/info.html')#need to make  

@app.route('/depression/referrals')
def show_depr_referrals():

    return render_template('/depression/referrals.html')#need to make  

@app.route('/depression/treatments')
def show_depr_treatments():

    return render_template('/depression/treatments.html')#need to make  


######################################## Cheer me up routes ################################################

@app.route('/cheer-me-up')
def show_cheer_me_up():

    return render_template('cheer-me-up.html')#need to make  
       
   



######################################## Crisis program routes ############################################

@app.route('/crisis/start', methods=["GET"])
def crisis_program_page():    
    

    return render_template("/crisis/start.html")


@app.route('/crisis/start', methods=["POST"])
def start_crisis_program():

    session["responses"] = []

    return redirect(f"/crisis/questions/{len(session['responses'])}")

@app.route('/crisis/questions/<int:question_num>')
def crisis_questions(question_num):


    if len(session["responses"]) is None:
        return redirect("/crisis/start")
        

    if len(session["responses"]) != question_num:
        flash("Question Error, Returned to Current Question")
        return redirect(f"/crisis/questions/{len(session['responses'])}")

    question = crisis.questions[question_num].question
    choices = crisis.questions[question_num].choices

    return render_template("/crisis/questions.html", question=question, choices=choices, question_num=question_num)



@app.route('/crisis/answers', methods=["POST"])
def track_crisis_answers():

    answer = request.form.get("answer")

    responses = session["responses"]
    responses.append(answer)
    session["responses"] = responses

    if len(session["responses"]) == len(crisis.questions):
        crisis_score = program.calculate_score(responses)
        if crisis_score == 0:
            return redirect("/crisis/coping")
        else:
            return redirect("/crisis/referrals") 
                   
    return redirect(f"/crisis/questions/{len(session['responses'])}")


@app.route('/crisis/referrals')
def crisis_referral_page():
    """Needs work"""


    county_form = CountyReferralForm()
    zip_form = ZipReferralForm()

    counties = [(c.id, c.name) for c in County.query.all()]
    county_form.county.choices = counties
    return render_template("/crisis/referrals.html", zip_form=zip_form, county_form=county_form)



@app.route('/crisis/referrals/<int:county_id>)')
def crisis_handle_county(county_id):
    county = County.query.get(county_id)

    county_form = CountyReferralForm()
    zip_form = ZipReferralForm()

    counties = [(c.id, c.name) for c in County.query.all()]
    county_form.county.choices = counties


    return render_template("/crisis/referrals.html", zip_form=zip_form, county_form=county_form, county=county)


@app.route('/crisis/referrals/<int:zip_code>)')
def crisis_handle_zip(zip_code):
    zip = Zip_Code.query.filter(Zip_Code.name == zip_code).one()

    county_form = CountyReferralForm()
    zip_form = ZipReferralForm()

    counties = [(c.id, c.name) for c in County.query.all()]
    county_form.county.choices = counties

    return render_template("/crisis/referrals.html", zip_form=zip_form, county_form=county_form, zip=zip)
    
 
   
@app.route('/crisis/coping')
def crisis_coping_skills():

    return render_template("/crisis/coping.html")
