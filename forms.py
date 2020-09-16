from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import DataRequired, Length, Optional


class UserAddForm(FlaskForm):
    """Form for adding users."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])
    
    

class LoginForm(FlaskForm):
    """Login form."""

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[Length(min=6)])


class CountyReferralForm(FlaskForm):
    """Form for looking up local referrals by county"""

    county = SelectField('County', validators=[Optional()])


class ZipReferralForm(FlaskForm):
    """Form for looking up local referrals by zipcode"""

    zip_code = StringField('Zip Code', validators=[Length(max=5), Optional()])


class PostAddForm(FlaskForm):
    """Form for adding posts."""

    title = StringField('Title', validators=[DataRequired()])
    body = TextAreaField('Body', validators=[DataRequired()])
    

class UserEditForm(FlaskForm):
    """Form for editings users."""

    username = StringField('Username', validators=[DataRequired()])
