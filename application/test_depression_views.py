"""Depression View tests."""

# run these tests like:
#
#    FLASK_ENV=production python -m unittest test_message_views.py
import os
from unittest import TestCase

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


# Don't have WTForms use CSRF at all, since it's a pain to test

app.config['WTF_CSRF_ENABLED'] = False


class DepressionViewTestCase(TestCase):
    """Test views for messages."""

    def setUp(self):
        """Create test client, add sample data."""
        self.client = app.test_client()




    def test_depression_info(self):
        with self.client as c:
            

            resp = c.get("/depression")

            self.assertEqual(resp.status_code, 200)
            self.assertIn("What is Depression?", str(resp.data))
            self.assertIn("Criteria", str(resp.data))

    def test_depression_referrals(self):
        with self.client as c:
        

            resp = c.get("/depression/referrals")

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Referrals", str(resp.data))
            self.assertIn("National Suicide", str(resp.data))

    def test_depression_treatments(self):
        with self.client as c:
            

            resp = c.get("/depression/treatments")

            self.assertEqual(resp.status_code, 200)
            self.assertIn("Counseling", str(resp.data))
            self.assertIn("Medication", str(resp.data))
            self.assertIn("Best Results", str(resp.data))
            
