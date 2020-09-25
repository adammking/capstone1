from flask import Blueprint, render_template

depression_bp = Blueprint('depression_bp', __name__, template_folder='templates')


@depression_bp.route('/depression')
def show_depr_info():

    return render_template('/depression/info.html')  # need to make


@depression_bp.route('/depression/referrals')
def show_depr_referrals():

    return render_template('/depression/referrals.html')  # need to make


@depression_bp.route('/depression/treatments')
def show_depr_treatments():

    return render_template('/depression/treatments.html')  # need to make
