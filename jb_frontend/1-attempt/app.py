import os
from flask import Flask, jsonify, render_template, request, make_response, url_for, redirect
# import requests
# import json
import pandas as pd
import numpy as np
# import scaler
import joblib 

app = Flask(__name__)

clf = joblib.load("../backend/clf.joblib")

def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, thalach, exang):
    model_input = [age, sex, cp, trestbps, chol, fbs, thalach, exang]
    return clf.predict([model_input])[0]

    
data = []
# def predict_disease(input_data, model):
#     x = input_data
# #  pass x to the model

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

        # for i in input_data:
        #     for d in i:
        #         d = int(d)
        #         print(type(d))
        #         data.append(d)
        #         print(d)
        

        for i in input_data:
            d = int(i)
            # print(type(d))
            data.append(d)
            # print(d)
        
        print(data)
        print("end")

#   ml function

        return render_template("results.html", display = "block")
    else: 
        return render_template("results.html", display = "none")



@app.route("/visuals")
def visual():
    return render_template("visual.html")


@app.route("/classify")
def classify():

    # data_dict = request.get_json()
 
    # age = data_dict['age'], 
    # sex = data_dict['sex'], 
    # cp = data_dict['cp'], 
    # trestbps = data_dict['trestbps'], 
    # chol = data_dict['chol'], 
    # fbs = data_dict['fbs'], 
    # thalach = data_dict['thalach'], 
    # exang = data_dict['exang']
    
    age = data[0], 
    sex = data[1], 
    cp = data[2], 
    trestbps = data[3], 
    chol = data[4], 
    fbs = data[5], 
    thalach = data[6], 
    exang = data[7]

    # print(exang)

    # prediction = predict_heart_disease(age, sex, cp, trestbps, chol, fbs, thalach, exang)
    # print(prediction)

    # return jsonify({
    #     "age": age, 
    #     "sex": sex, 
    #     "cp": cp, 
    #     "trestbps": trestbps, 
    #     "chol": chol, 
    #     "fbs": fbs, 
    #     "thalach": thalach, 
    #     "exang": exang,
    #     "prediction": bool(prediction)
    # })
    return render_template("results.html")

if __name__ == "__main__":
    app.run(debug=True)