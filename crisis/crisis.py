from flask import Flask, render_template, request, flash, redirect, session, g, Blueprint
from crisis.models import crisis_db, crisis_connect_db, Mental_Health_Center, County, Zip_Code
from crisis.program import crisis, Crisis_Program
from forms import CountyReferralForm, ZipReferralForm


crisis_bp = Blueprint('crisis_bp', __name__, template_folder='templates')
program = Crisis_Program
crisis = crisis


@crisis_bp.route('/crisis/start', methods=["GET"])
def crisis_program_page():

    return render_template("/crisis/start.html")


@crisis_bp.route('/crisis/start', methods=["POST"])
def start_crisis_program():

    session["responses"] = []

    return redirect(f"/crisis/questions/{len(session['responses'])}")


@crisis_bp.route('/crisis/questions/<int:question_num>')
def crisis_questions(question_num):

    if len(session["responses"]) is None:
        return redirect("/crisis/start")

    if len(session["responses"]) != question_num:
        flash("Question Error, Returned to Current Question")
        return redirect(f"/crisis/questions/{len(session['responses'])}")

    question = crisis.questions[question_num].question
    choices = crisis.questions[question_num].choices

    return render_template("/crisis/questions.html", question=question, choices=choices, question_num=question_num)


@crisis_bp.route('/crisis/answers', methods=["POST"])
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


@crisis_bp.route('/crisis/referrals')
def crisis_referral_page():
    """Displays National Referrals and allows search by county and zip"""

    county_form = CountyReferralForm()
    zip_form = ZipReferralForm()

    counties = [(c.id, c.name) for c in County.query.all()]
    county_form.county.choices = counties
    return render_template("/crisis/referrals.html", zip_form=zip_form, county_form=county_form)


@crisis_bp.route('/crisis/referrals/county')
def crisis_handle_county():
    county_name = request.args.get("county")
    county = County.query.filter(County.name.like(f"%{county_name}%")).first()

    county_form = CountyReferralForm()
    zip_form = ZipReferralForm()

    counties = [(c.id, c.name) for c in County.query.all()]
    county_form.county.choices = counties

    return render_template("/crisis/referrals.html", zip_form=zip_form, county_form=county_form, county=county)


@crisis_bp.route('/crisis/referrals/zip')
def crisis_handle_zip():
    zip_code = request.args.get("zip")
    zip = Zip_Code.query.filter(Zip_Code.name == zip_code).first()

    county_form = CountyReferralForm()
    zip_form = ZipReferralForm()

    counties = [(c.id, c.name) for c in County.query.all()]
    county_form.county.choices = counties

    return render_template("/crisis/referrals.html", zip_form=zip_form, county_form=county_form, zip=zip)


@crisis_bp.route('/crisis/coping')
def crisis_coping_skills():
    """Displays coping skills for crisis situations"""
    return render_template("/crisis/coping.html")
