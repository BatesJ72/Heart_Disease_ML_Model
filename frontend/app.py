import os
from flask import Flask, jsonify, render_template, request, make_response, url_for, redirect
# import requests
# import json
import pandas as pd
import numpy as np
import joblib
import plotly

app = Flask(__name__)

# model = 

clf = joblib.load("../backend/clf.joblib")

model_input =[]

def predict_heart_disease(input_data):
    return clf.predict([data_input])[0]

input_data = []
data_input = []



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

        input_data.append([age, sex, cp, fbs, trestbps, chol, thalach, exang])
    
        for i in input_data:
            for d in i:
                e = int(d)
                data_input.append(e)
        
        data = predict_heart_disease(data_input)

        if data == 1:
            data = "You are at risk! Take heed!"
        else:
            data = "All good bro!"

        return render_template("results.html", display = "block", data=data)
    else: 
        return render_template("results.html", display = "none")

@app.route("/visuals")
def visual():
    return render_template("visual.html")


@app.route("/predict")
def new_route():

    return predict_heart_disease(input_data)

    

     

if __name__ == "__main__":
    app.run(debug=True)