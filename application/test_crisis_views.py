"""User View tests."""

# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_message_views.py


import os
from unittest import TestCase

from crisis_models import db, crisis_connect_db, Mental_Health_Center, County, Zip_Code

# BEFORE we import our app, let's set an environmental variable
# to use a different database for tests (we need to do this
# before we import our app, since that will have already
# connected to the database

os.environ['DATABASE_URL'] = "postgresql:///capstone1-test"


# Now we can import app
from app import app, CURR_USER_KEY
# Create our tables (we do this here, so we only create the tables
# once for all tests --- in each test, we'll delete the data
# and create fresh new clean test data

db.create_all()

# Don't have WTForms use CSRF at all, since it's a pain to test

app.config['WTF_CSRF_ENABLED'] = False


class UserViewTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""

        db.drop_all()
        db.create_all()

        self.client = app.test_client()



    def test_crisis_start(self):
        with self.client as c:

            resp = c.get("/crisis/start")

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Crisis Program", str(resp.data))

    def test_crisis_referral(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess["responses"] = ['Yes', 'No', 'No']

            resp = c.post("/crisis/answers", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Local Referral Search", str(resp.data))

    def test_crisis_coping(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess["responses"] = ['No', 'No', 'No']

            resp = c.post("/crisis/answers", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("What is a crisis?", str(resp.data))
            self.assertIn("What to try?", str(resp.data))
            self.assertIn("Specific Skills", str(resp.data))

    def test_attempt_skip_question(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess["responses"] = ['No']

            resp = c.get("/crisis/questions/0", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Question Error", str(resp.data))

    def test_skip_with_no_answers(self):
        with self.client as c:
            

            resp = c.get("/crisis/questions/2", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Crisis Program", str(resp.data))
