import os
from flask import Flask, jsonify, render_template, request, make_response
# import requests
# import json
import pandas as pd
import numpy as np
# import scaler

app = Flask(__name__)

# MODEL SHOULD OPEN HERE
# with open(f"randomforest.pickle, 'rb'") as model:
#   scaler = pickle.load(model) 


@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST": 
        
        # chol = int(request.form[chol])
        # values = [chol, value, value, value]

        # data = pd.Dataframe(np.array([values])
        # scaled_values = scaler.transform(data)

        # results = model.predict(scaled_values)

        # if results == 1:
        #     output_message = "you have heart disease" 

        # else
        #     output_message = specificy here
    
        
    return render_template("index.html", output_message)
    

@app.route("/visuals")
def visual():
    return render_template("visual.html")


@app.route("/ghostboy")
def you_dont_see_me():
    return "im gonna disappear!"


if __name__ == "__main__":
    app.run(debug=True)