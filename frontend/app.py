import os
from flask import Flask, jsonify, render_template, request, make_response, url_for, redirect
# import requests
# import json
import pandas as pd
import numpy as np
# import scaler

app = Flask(__name__)

# model = 

def predict_disease(input_data, model):
    x = input_data
#  pass x to the model

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST": 
        

        age = request.form["age"]
        sex = request.form["sex"]
        cp = request.form["cp"]
        fbs = request.form["fbs"]
        trestbps = request.form["trestbps"]
        chol = request.form["chol"]
        thalach = request.form["thalach"]
        exang = request.form["exang"]

        input_data = [age, sex, cp, fbs, trestbps, chol, thalach, exang]
        
        print(input_data)

#   ml function

        return render_template("results.html", display = "block")
    else: 
        return render_template("results.html", display = "none")

@app.route("/visuals")
def visual():
    return render_template("visual.html")


if __name__ == "__main__":
    app.run(debug=True)