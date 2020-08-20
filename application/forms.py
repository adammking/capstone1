from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField
from wtforms.validators import DataRequired, Length, Optional


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
    first_name = StringField('First Name', validators=[Optional()])
    last_name = StringField('Last Name', validators=[Optional()])
    

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class CountyReferralForm(FlaskForm):
    """Form for looking up local referrals"""

    county = SelectField('County', validators=[Optional()])


class ZipReferralForm(FlaskForm):
    """Form for looking up local referrals"""

    zip_code = StringField('Zip Code', validators=[Length(max=5), Optional()])
