# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 23:36:17 2023

@author: lilbl
"""
import requests

patient_types = requests.get("http://vcm-7631.vm.duke.edu:5002/get_patients/tj95")
patients = patient_types.json()
recipient_patient_id = patients["Recipient"]
donor_patient_id = patients["Donor"]
recipient_blood_type = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/" + recipient_patient_id)
donor_blood_type = requests.get("http://vcm-7631.vm.duke.edu:5002/get_blood_type/" + donor_patient_id)
recipient_blood_type = recipient_blood_type.text
donor_blood_type = donor_blood_type.text

def check_blood_type(r, d):
    if r == d:
        answer = "Yes"
    else:
        answer = "No"
    return answer

answer = check_blood_type(recipient_blood_type, donor_blood_type)
def output(answer):
    out_data = {"Name": "tj95", "Match": answer}
    return out_data

out_data = output(answer)

post_r = requests.post("http://vcm-7631.vm.duke.edu:5002/match_check", json=out_data)
print(post_r.status_code)
print(post_r.text)