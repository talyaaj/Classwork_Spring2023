# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 00:51:36 2023

@author: lilbl
"""
import requests


server = "http://127.0.0.1:5000"

r= requests.get(server + "/info")

print(r.status_code)
print(r.text)
out_data = {"name": "David", "HDL_value": 55}
rnew = requests.post(server + "/HDL_analysis", json=out_data)
print(rnew.status_code)
print(rnew.text)

r = requests.get(server + "/add_two/5/26")
print(r.status_code)
print(r.text)
print(r.json())


r = requests.post(server + "/add", json = out_data)
print(r.status_code)
print(r.text)
if r.status_code == 200:
    x = r.json() #this will unjsonify, so it will convert a json string to a python variable like an int
    print(x +2)