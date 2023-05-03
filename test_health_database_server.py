# -*- coding: utf-8 -*-
"""
Created on Wed May  3 13:39:26 2023

@author: lilbl
"""

def test_add_new_test():
    from healh_db_server import add_new_test
    # arange
    patient_id = 123
    patient_name = "test"
    patient_blood_type= "B+"
    from health_database_server import add_patient_to_db
    add_patient_to_db(patient_id, patient_name, patient_blood_type)
    test_name = "HDL"
    test_value =150
    #act
    add_new_test(patient_id, test_name, test_value) #this doesn't return anything
    # so how do we check if it worked as  intended?
    #assert
    from health_db_server import db
    answer = db[patient_id]["tests"][-1]
    expected = (test_name, test_value)
    assert answer == expected