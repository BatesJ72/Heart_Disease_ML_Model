import os
from flask import Flask, jsonify, render_template, request, make_response
# import requests
# import json
# import pandas as pd

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/visuals")
def visual():
    return render_template("visual.html")


@app.route("/ghostboy")
def you_dont_see_me():
    return "im gonna disappear!"


if __name__ == "__main__":
    app.run(debug=True)