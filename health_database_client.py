# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 23:35:49 2023

@author: lilbl
"""

import requests


server = "http://127.0.0.1:5000"


patient = {"id": 1, "name": "David", "blood_type": "O+"}
r = requests.post(server + "/new_patient", json=patient)
print(r.status_code)
print(r.text)

new_test = {"id": 1, "test_name": "A1C", "test_result": 27}
r = requests.post(server + "/add_test", json=new_test)
print(r.status_code)
print(r.text)

r = requests.get(server + "/get_results/1")
print(r.status_code)
print(r.text)
answer = r.json()
for t in answer: #this will print each test
    print(t)