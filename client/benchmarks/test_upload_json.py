import json
import requests

url = 'http://127.0.0.1:8000/upload/'
secret = 'e984c3017cd1a0dff0ef9f0c394a5c285e421411'
headers = {'Content-Type': 'application/json; charset=utf-8', 'Authorization': secret}
with open("/home/guo/PythonClass/results_need.json", 'r') as load_f:
    load_data = json.load(load_f)
    postdata = load_data
    post = []
    post.append(postdata)

r = requests.post(url.encode('utf-8'), data=json.dumps(post).encode('utf-8'), headers=headers)
