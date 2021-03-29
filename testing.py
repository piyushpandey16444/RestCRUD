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


# get_data()

def send_data():
    py_dict = {"id": 6, "name": "Ravi", "roll_no": 6, "city": "MBU"}
    json_dt = json.dumps(py_dict)
    json_response = requests.post(url=URL, data=json_dt)
    j_response = json_response.json()
    print(j_response)


# send_data()


def update_data():
    py_dict = {"id": 6, "name": "Ravi Updated", "roll_no": 7, "city": "MBU"}
    json_dt = json.dumps(py_dict)
    json_response = requests.put(url=URL, data=json_dt)
    j_response = json_response.json()
    print(j_response)


# update_data()


def delete_data():
    py_dict = {"id": 6}
    json_dt = json.dumps(py_dict)
    json_response = requests.delete(url=URL, data=json_dt)
    j_response = json_response.json()
    print(j_response)


delete_data()
