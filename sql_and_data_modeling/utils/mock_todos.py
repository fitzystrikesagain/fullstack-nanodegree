import json

from faker import Faker
import requests

fake = Faker()
url = "http://localhost:5000/api/todos/create"
headers = {'Content-Type': 'Application/JSON'}

for _ in range(50):
    todo = fake.bs()
    data = {"description": todo, "list_id": 1}
    data = json.dumps(data)
    print(data)
    r = requests.post(url, data=data, headers=headers)
