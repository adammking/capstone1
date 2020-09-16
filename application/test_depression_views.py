"""Depression View tests."""


import os
from unittest import TestCase


os.environ['DATABASE_URL'] = "postgresql:///capstone1-test"


from app import app, CURR_USER_KEY


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
            
