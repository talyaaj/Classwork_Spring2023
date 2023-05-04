# -*- coding: utf-8 -*-
"""
Created on Wed May  3 13:39:26 2023

@author: lilbl
"""
from pymodm import connect
from PatientModel import Patient
from secrets import mongodb_acct, mongodb_pwd
connect("mongodb+srv://{}:{}"
            "@bme547.89uqvz1.mongodb.net/classhealthdb?retryWrites=true&w=majority".format(mongodb_acct, mongodb_pwd))
def test_add_patient_to_db():
    from health_database_server import add_patient_to_db
    patient_id = 234
    patient_name = "fester"
    blood_type = "O+"
    answer = add_patient_to_db(patient_id, patient_name, blood_type)
    x = Patient.objects.raw({"_id": patient_id}).first()
    x.delete() #this is so that you can recreate and rerun it and stuff, especially
    # if the assert fails, it'll still clear it for u
    assert answer.patient_id == patient_id


# def test_add_new_test():
#     from health_database_server import add_new_test
#     # arange
#     patient_id = 123
#     patient_name = "test"
#     patient_blood_type= "B+"
#     from health_database_server import add_patient_to_db
#     add_patient_to_db(patient_id, patient_name, patient_blood_type)
#     test_name = "HDL"
#     test_value =150
#     #act
#     add_new_test(patient_id, test_name, test_value) #this doesn't return anything
#     # so how do we check if it worked as  intended?
#     #assert
#     from health_database_server import db
#     answer = db[patient_id]["tests"][-1]
#     expected = (test_name, test_value)
#     db.clear() #do this so that it doesn't impact future tests, must be done
#     #before the assert because if the test fails, then the db won't be cleared
#     assert answer == expected

def test_add_new_test():
    from health_database_server import add_new_test
    patient_id = 456
    patient_name = "bobby"
    patient_blood_type = "AB+"
    test_name = "HDL"
    test_value = 150
    add_new_test(patient_id, test_name, test_value)
    x=Patient.objects.raw({"_id": patient_id}).first()
    x.delete() #deletes this test entry from mongodb
    answer = x.tests[-1]
    expected = ("HDL", 150)
    assert answer == expected