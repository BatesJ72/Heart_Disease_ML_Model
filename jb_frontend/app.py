import os
from flask import Flask, jsonify, render_template, request, make_response, url_for, redirect
# import requests
# import json
import pandas as pd
import numpy as np
import joblib

app = Flask(__name__)

clf = joblib.load("../backend/clf.joblib")

# def predict_heart_disease(input_data):
    # for i in input_data:
    #     model_input.append(i)
#     return clf.predict([model_input])[0]

def predict_heart_disease(input_data):
    return clf.predict([data])[0]
    

input_data = []
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


        input_data.append([age, sex, cp, fbs, trestbps, chol, thalach, exang])

     
        # prediction = predict_heart_disease(input_data)

        # input_data == ({
        #     "age": int(age), 
        #     "sex": bool(sex), 
        #     "cp": int(cp), 
        #     "trestbps": int(trestbps), 
        #     "chol": int(chol), 
        #     "fbs": int(fbs), 
        #     "thalach": int(thalach), 
        #     "exang": int(exang),
        #     # "prediction": bool(prediction)
        # })

        print(input_data)
        
        for i in input_data:
            for d in i:
                e = int(d)
                print(e)
                print(f"type: {type(e)}")
                data.append(e)

        

        print("end")

        print(data)
        print("end2")

        return render_template("results.html", display = "block")
    else: 
        return render_template("results.html", display = "none")



@app.route("/visuals")
def visual():
    return render_template("visual.html")



@app.route("/predict")
def new_route():

    # print(data)
    
    # for i in data:
    #     print(type(i))

    # print("end3")
    
    print(predict_heart_disease(data))

    return render_template("visual.html")

    # return predict_heart_disease(data)

    

     

if __name__ == "__main__":
    app.run(debug=True)