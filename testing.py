import requests
import json
URL = 'http://localhost:8000/data/'


def get_data(id=None):
    py_dict = {}
    if id is not None:
        py_dict = {'id': id}
    json_data = json.dumps(py_dict)
    json_response = requests.get(url=URL, data=json_data)
    j_response = json_response.json()
    print(j_response)


get_data(4)
