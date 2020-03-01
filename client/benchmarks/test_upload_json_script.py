import json
import requests
import os

url = 'http://127.0.0.1:8000/upload/'
secret = 'e984c3017cd1a0dff0ef9f0c394a5c285e421411'
headers = {'Authorization': secret}
# headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': secret}
with open("/home/guo/PythonClass/results_script.json", 'r') as load_f:
    load_data = json.load(load_f)
    postdata = load_data
    # post = []
    # post.append(postdata)

files = {
     'json': (None, json.dumps(load_data), 'application/json'),
     'file': (os.path.basename('insert.sql'), open('../tmp/files/insert.sql', 'rb'), 'application/octet-stream')
}
# files = {'insert.sql': open('../tmp/files/insert.sql', 'rb')}
r = requests.post(url.encode('utf-8'), files=files, headers=headers)
