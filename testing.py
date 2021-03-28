import requests
import io
import json
URL = ''


def get_data(id=None):
    py_dict = {}
    if id is not None:
        py_dict = {'id': id}
    json_data = json.dumps(py_dict)
    json_response = requests.get(url=URL, data=json_data)
    py_response = json_response.json()
    print(py_response)


get_data()
