from flask_sqlalchemy import SQLAlchemy

crisis_db = SQLAlchemy()

def crisis_connect_db(app):
    """Connect to database."""

    crisis_db.app = app
    crisis_db.init_app(app)

class State(crisis_db.Model):
    """An individual state."""

    __tablename__ = 'states'

    id = crisis_db.Column(
        crisis_db.Integer,
        primary_key=True,
    )

    name = crisis_db.Column(
        crisis_db.Text,
        nullable=False,
    )



class County(crisis_db.Model):
    """An individual county."""

    __tablename__ = 'counties'

    id = crisis_db.Column(
        crisis_db.Integer,
        primary_key=True,
    )

    name = crisis_db.Column(
        crisis_db.Text,
        nullable=False,
    )

    state_id = crisis_db.Column(
        crisis_db.Integer,
        crisis_db.ForeignKey('states.id', ondelete='CASCADE'),
        nullable=False,
    )

    mhc_id = crisis_db.Column(
        crisis_db.Integer, 
        crisis_db.ForeignKey('mhcs.id', ondelete='CASCADE')
    )


class Mental_Health_Center(crisis_db.Model):
    """An individual mental health center (MHC)."""

    __tablename__ = 'mhcs'

    id = crisis_db.Column(
        crisis_db.Integer,
        primary_key=True
    )

    name = crisis_db.Column(
        crisis_db.Text,
        nullable=False
    )

    crisis_line = crisis_db.Column(
        crisis_db.Text,
        nullable=False
    )

    website = crisis_db.Column(
        crisis_db.Text,
        nullable=False
    )

    state_id = crisis_db.Column(
        crisis_db.Integer,
        crisis_db.ForeignKey('states.id', ondelete='CASCADE'),
        nullable=False
    )

    states = crisis_db.relationship('State', backref='mhcs')

    counties = crisis_db.relationship('County', backref='mhcs')

    zip_codes = crisis_db.relationship('Zip_Code', secondary="counties", backref='mhcs')
    



class Zip_Code(crisis_db.Model):
    """An individual zip code."""

    __tablename__ = 'zip_codes'

    id = crisis_db.Column(
        crisis_db.Integer,
        primary_key=True
    )

    name = crisis_db.Column(
        crisis_db.Text,
        nullable=False
    )

    county_id = crisis_db.Column(
        crisis_db.Integer,
        crisis_db.ForeignKey('counties.id', ondelete='CASCADE'),
        nullable=False
    )

    zip_counties = crisis_db.relationship('County', backref='zip_codes')

    
