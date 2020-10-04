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
CURR_USER_KEY = "curr_user"

app = Flask(__name__)

# Get DB_URI from environ variable (useful for production/testing) or,
# if not set there, use development local db.
app.register_blueprint(depression_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(users_bp)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'postgres:///capstone1')

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = False
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', "it's a secret")

crisis_connect_db(app)
social_connect_db(app)
program = Crisis_Program
mhc = Mental_Health_Center()
########################## Login/logout/register routes ###############################




######################################### User profile/community routes #############################





######################################## Depression info routes #######################################



######################################## Cheer me up routes ################################################

@app.route('/cheer-me-up')
def show_cheer_me_up():

    return render_template('cheer-me-up.html')
       
   



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
    """Displays National Referrals and allows search by county and zip"""


    county_form = CountyReferralForm()
    zip_form = ZipReferralForm()

    counties = [(c.id, c.name) for c in County.query.all()]
    county_form.county.choices = counties
    return render_template("/crisis/referrals.html", zip_form=zip_form, county_form=county_form)



@app.route('/crisis/referrals/county')
def crisis_handle_county():
    county_name = request.args.get("county")
    county = County.query.filter(County.name.like(f"%{county_name}%")).first()

    county_form = CountyReferralForm()
    zip_form = ZipReferralForm()

    counties = [(c.id, c.name) for c in County.query.all()]
    county_form.county.choices = counties


    return render_template("/crisis/referrals.html", zip_form=zip_form, county_form=county_form, county=county)


@app.route('/crisis/referrals/zip')
def crisis_handle_zip():
    zip_code = request.args.get("zip")
    zip = Zip_Code.query.filter(Zip_Code.name == zip_code).first()

    county_form = CountyReferralForm()
    zip_form = ZipReferralForm()

    counties = [(c.id, c.name) for c in County.query.all()]
    county_form.county.choices = counties

    return render_template("/crisis/referrals.html", zip_form=zip_form, county_form=county_form, zip=zip)
    
 
   
@app.route('/crisis/coping')
def crisis_coping_skills():
    """Displays coping skills for crisis situations"""
    return render_template("/crisis/coping.html")
