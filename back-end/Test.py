import json
import unittest
import requests


class Location(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/bus/location"
        self.body = {"keywords": "华南师范大学"}
        self.headers = {"Content-Type": "application/json"}
        self.r = requests.post(self.url, data=json.dumps(self.body), headers=self.headers)

    def test_location(self):
        print(self.r.json())
        self.assertIsNone(self.r.json()["error"])


class Route(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/bus/route"
        self.body = {"startPointName": "xxxxx",
                     "startPointSign": "xxxxxxx=",
                     "endPointName": "xxxxx",
                     "endPointSign": "xxxxxx="}
        self.headers = {"Content-Type": "application/json"}
        self.r = requests.post(self.url, data=json.dumps(self.body), headers=self.headers)

    def test_route(self):
        self.assertIsNone(self.r.json()["error"])


class Login(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/user/login"
        self.body = {"username": "xxx",
                     "password": "xxx"}
        self.headers = {"Content-Type": "application/json"}
        self.r = requests.post(self.url, data=json.dumps(self.body), headers=self.headers)

    def test_login(self):
        self.assertEqual("SUCCEED", self.r.json()["status"])


class Register(unittest.TestCase):
    def setUp(self):
        self.url = "http://127.0.0.1:8000/api/user/register"
        self.body = {"username": "xxx", "password": "xxx", "mail": "xxx"}
        self.headers = {"Content-Type": "application/json"}
        self.r = requests.post(self.url, data=json.dumps(self.body), headers=self.headers)

    def test_register(self):
        self.assertEqual("SUCCEED", self.r.json()["status"])
