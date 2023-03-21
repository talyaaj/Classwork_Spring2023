# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 00:29:24 2023

@author: lilbl
"""

from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"]) #this indicates the base string of the server without any route
def server_status():
    return "Server On"

@app.route("/info", methods=["GET"])
def info_route():
    return "This server was written for BME547"

if __name__ == '__main__':
    app.run()