# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 00:29:24 2023

@author: lilbl
"""

from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"]) #this indicates the base string of the server without any route
def server_status():
    return "Server On"

@app.route("/info", methods=["GET"])
def info_route():
    return "This server was written for BME547"

@app.route("/HDL_analysis", methods=["POST"])
def HDL_route_handler():
    """
    in_data = {"name": <patient_name>, "HDL_value": <HDL_result>}

    Returns
    -------
    None.

    """
    from blood_calculator import HDLLDL_analysis
    in_data = request.get_json()
    print("Received HDL value of {}".format(in_data["HDL_value"]))
    diagnosis = HDLLDL_analysis(in_data["HDL_value"], 24)
    return diagnosis[0]

@app.route("/add", methods=["POST"])
def add_numbers():
    in_data = request.get_json()
    answer = in_data["a"] + in_data["b"]
    if answer<0:
        return "The answer was less than zero, BAD", 400 #default status code is 200, if we want to alert user of something else, we have to send a different status code
    return jsonify(answer)

@app.route("/add_two/<a>/<b>", methods=["GET"]) #it will do something based on the variables
def add_two_handler(a, b): #these two variables will ALWAYS be a string
    answer = int(a) + int(b)
    return jsonify(answer)

if __name__ == '__main__':
    app.run()