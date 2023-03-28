# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 16:02:05 2023

@author: lilbl
"""

import requests

r = requests.get("https://api.github.com/repos/talyaaj/Classwork_Spring2023/branches")
# information that comes back from the server will be stored in the variable r
print(r)
print(type(r))
print(r.status_code) #status code tells you whether or not the request was good (an example of a bad one is 404 not found)
#200 is the status code for good request. All other code types are on github,schedule, apis/requests/servers

print(r.text)
cheese = r.text
print(cheese)
# if we want to see the requested information, it'll be in a text format

branches = r.json()
#this changes the string to an actual list

for x in branches: #each index in the list is a dictionary
    print(x["name"])

#browsers make GET requests so you visualize yourgithub request by copy/pasting it, but NOT a post request
# %%
# out_data = {"name": "Talya Jeter", "net_id": "tj95",
#            "e-mail": "talya.jeter@duke.edu"}
# post_r = requests.post("http://vcm-21170.vm.duke.edu:5000/student",
#                       json=out_data)
print(r.status_code)
print(r.text)

