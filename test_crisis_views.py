"""Crisis View tests."""


import os
from unittest import TestCase
from flask import session
from crisis_models import db, crisis_connect_db, Mental_Health_Center, County, Zip_Code



os.environ['DATABASE_URL'] = "postgresql:///capstone1-test"

from app import app, CURR_USER_KEY


db.create_all()

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
                sess["responses"] = ['Yes', 'No']

            resp = c.post("/crisis/answers", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Local Referral Search", str(resp.data))

    def test_crisis_coping(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess["responses"] = ['No', 'No']

            resp = c.post("/crisis/answers", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("What is a crisis?", str(resp.data))
            self.assertIn("What to try?", str(resp.data))
            self.assertIn("Specific Skills", str(resp.data))

    def test_attempt_skip_question(self):
        with self.client as c:
            with c.session_transaction() as sess:
                sess["responses"] = ['No']

            resp = c.get("/crisis/questions/43", follow_redirects=True)

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Question Error", str(resp.data))

    
