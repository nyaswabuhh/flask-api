import unittest

from main import app
from dbservice import app

class FlaskAPITest(unittest.TestCase):
    token = ""
    headers={}
    def setUp(self):
        self.app=app.test_client()
        self.app.testing=True

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code,200)
        self.assertEqual(response.get_json(), {"Flask-API Special Development -register":"1.0"})

    def test_login(self):
       
        response=self.app.post('api/login', json={
            'email': 'ken@example.com',
            'password': 'ken123'
        })
        self.assertEqual(response.status_code,200)
        self.token=response.get_json()['token']
        print(self.token)
        self.headers={"Authorization": "Bearer " + self.token, "Content-Type":"application/json"}
       
       





if __name__ == '__main__':
    unittest.main()
