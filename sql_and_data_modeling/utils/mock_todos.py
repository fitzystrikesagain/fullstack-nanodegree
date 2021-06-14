import json

from faker import Faker
import requests

fake = Faker()
url = "http://localhost:5000/api/todos/create"
headers = {'Content-Type': 'Application/JSON'}

for _ in range(20):
    todo = fake.bs()
    data = {"description": todo, "list_id": 2}
    data = json.dumps(data)
    print(data)
    r = requests.post(url, data=data, headers=headers)
