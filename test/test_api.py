import requests
import unittest
import ast, json, subprocess

class TestApiSimple(unittest.TestCase):

    def setUp(self):
        self.payload = {
            'username' : 'django',
            'password' : 'space',
        }

    def test_api_token(self):
        with requests.Session() as session:
            res = session.post(
                'https://0.0.0.0:8000/api/login/',
                data    = self.payload,
                verify  = False
            )
            # print(res.content)
            self.assertEqual(res.status_code, 200)
            token = ast.literal_eval(res.content.decode("UTF-8"))['token']
            res = session.get(
                'https://0.0.0.0:8000/api/home/',
                verify  = False,
                headers = {"Authorization":f"Token {token}"}
            )
            # print(res.status_code)
            self.assertEqual(res.status_code, 200)
            # print(res.content.decode("UTF-8"))
            res = session.post(
                'https://0.0.0.0:8000/api/logoutall/',
                verify  = False,
                headers = {"Authorization":f"Token {token}"}
            )
            # print(res.status_code)
            self.assertEqual(res.status_code, 204)

    def test_rfapi_token(self):
        with requests.Session() as session:
            res = session.post(
                'https://0.0.0.0:8000/api/rflogin/',
                data = self.payload,
                verify=False
            )
            self.assertEqual(res.status_code, 200)
            token = json.loads(res.content)['knoxToken']
            res = session.get(
                'https://0.0.0.0:8000/api/home/',
                verify=False,
                headers={"Authorization":f"Token {token}"}
            )
            self.assertEqual(res.status_code, 200)
            # print(res.status_code)
            # print(res.content.decode("UTF-8"))
            res = session.post(
                'https://0.0.0.0:8000/api/logoutall/',
                verify=False,
                headers={"Authorization":f"Token {token}"}
            )
            self.assertEqual(res.status_code, 204)
            # print(res.status_code)

if __name__ == '__main__':
    unittest.main()
