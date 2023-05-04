# -*- coding: utf-8 -*-
"""
Created on Sun Mar 26 22:30:12 2023

@author: lilbl
"""

"""
Database = Dictionary
keys => ids for the patients
value: int

and create a dictionary of dictionaries
{1: {"id":1, "name":"David", "blood_type": "O+"},
 2: {"id":1, "name":"David", "blood_type": "O+"},
 3: {"id":1, "name":"David", "blood_type": "O+"},
 "tests": {}}
"""
from flask import Flask, request, jsonify
from pymodm import connect, MongoModel, fields
from PatientModel import Patient
from pymodm import errors as pymodm_errors
from secrets import mongodb_acct, mongodb_pwd

#assigning global variable names
app = Flask(__name__)
testdb = {}

def add_patient_to_db(pid, name, blood_type):
    new_patient = Patient(patient_id=pid,
                          patient_name= name,
                          blood_type= blood_type)
    saved_patient = new_patient.save()
    return saved_patient


@app.route("/new_patient", methods=["POST"])
def post_new_patient():
    """ POST request
    POST request contains patient information in the form of a including
    dictionary {'id': id, 'test_name': test_name, 'test_result': test_result}

    Returns
    -------
    answer : str
        success message that the test was added
    status_code : TYPE
        DESCRIPTION.

    """
    in_data = request.get_json()
    answer, status_code = new_patient_driver(in_data)
    return jsonify(answer), status_code
    # get input data
    # call other functions to do the work, all the work it does needs to be outsie
    # outside the route b/c the route can't be accessed with pytest
    # return a response


@app.route("/add_test", methods=["POST"])
def post_new_test():
    new_test = request.get_json()
    answer, status_code = new_test_driver(new_test)
    return jsonify(answer), status_code



@app.route("/get_results/<patient_id>", methods=["GET"])
def give_results(patient_id):
    test_name_answer, status_code = get_results_driver(patient_id)
    return jsonify(test_name_answer), status_code


def get_results_driver(patient_id):
    validation = validate_patient_id_from_get(patient_id)
    if validation is not True:
        return validation, 400
    patient = testdb[int(patient_id)]
    return patient["test_name"], 200


def validate_patient_id_from_get(patient_id):
    try:
        patient_num = int(patient_id)
    except ValueError:
        return "Patient_id should be an integer"
    if does_patient_exist_in_db(int(patient_id)) is False:
        return "Patient id of {} does not exist in database".format(int(patient_id))
    return True



def add_new_test(pid, test_name, test_result):
    x = Patient.objects.raw({"_id": pid}).first()
    x.tests.append((test_name, test_result))
    x.save()


def does_patient_exist_in_db(pid):
    try:
        x = Patient.objects.raw({"_id": pid}).first()
    except pymodm_errors.DoesNotExist:
        return False
    return True


def new_test_driver(new_test):
    expected_keys = ["id", "test_name", "test_result"]
    expected_types = [int, str, int]
    validation = validate_generic(new_test, expected_keys, expected_types)
    exist = does_patient_exist_in_db(new_test["id"])
    if exist is False:
        return "Patient id {} does not exist in the database".format(new_test["id"]), 400
    if validation is not True:
        return validation, 400
    add_new_test(new_test["id"], new_test["test_name"],
                 new_test["test_result"])
    return "Test successfully added", 200

def new_patient_driver(in_data):
    # validate input, everything that's in in_data should be there
    expected_keys = ["name", "id", "blood_type"]
    expected_types = [str, int, str]
    validation = validate_generic(in_data, expected_keys, expected_types)
    if validation is not True:
        return validation, 400 #400 tells the user that it's a bad request
    # do the work
    add_patient_to_db(in_data["id"], in_data["name"], in_data["blood_type"])
    # return an answer
    return "Patient successfully added", 200


def validate_generic(data, expected_keys, expected_types):
    if type(data) is not dict:
        return "Input is not a dictionary"
    for key, value_type in zip(expected_keys, expected_types):
        if key not in data:
            return "Key {} is missing from input".format(key)
        if type(data[key]) is not value_type:
            return "Key {} has the incorrect value type".format(key)
    return True

def init_server():
   connect("mongodb+srv://{}:{}"
            "@bme547.89uqvz1.mongodb.net/classhealthdb?retryWrites=true&w=majority".format(mongodb_acct, mongodb_pwd))

if __name__ =='__main__':
    init_server()
    app.run()