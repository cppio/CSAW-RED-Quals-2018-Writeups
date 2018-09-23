import secrets
import time

import requests

BASE_URL = "http://web.chal.csaw.io:10106/"

s = requests.session()

username = secrets.token_urlsafe()
s.headers["Authorization"] = s.post(BASE_URL + "user/register", json={"username": username, "password": username}).json()["Authorization"]

s.post(BASE_URL + "clicker/purchase", json={"name": "base"})

for i in range(10):
    s.post(BASE_URL + "clicker/click", json={"name": "base"})
    time.sleep(0.5)

s.post(BASE_URL + "clicker/purchase", json={"name": "momo"})

for i in range(11):
    s.post(BASE_URL + "clicker/click", json={"name": "base"})
    time.sleep(0.5)

s.post(BASE_URL + "clicker/purchase", json={"name": "momo"})

print(s.get(BASE_URL + "default/money").json())
