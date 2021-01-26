import os
from flask import Flask, jsonify, render_template, request, make_response, url_for, redirect
import pandas as pd
import numpy as np
import joblib
import plotly

app = Flask(__name__)

# ML Model
clf = joblib.load(os.path.join("backend", "clf.joblib"))
def predict_heart_disease(data_input):
    return clf.predict(data_input)


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

        data = predict_heart_disease(pd.DataFrame(
        {
            "age": age, 
            "sex": sex, 
            "cp": cp, 
            "fbs": fbs, 
            "trestbps": trestbps, 
            "chol": chol, 
            "thalach": thalach, 
            "exang": exang,
        },
        index=[0],
    ))


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


if __name__ == "__main__":
    app.run(debug=True)
