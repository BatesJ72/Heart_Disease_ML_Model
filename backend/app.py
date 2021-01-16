from flask import flask
import joblib

app = Flask(__name__)

clf = joblib.load("clf.joblib")

def predict_heart_disease(age, sex, cp, trestbps, chol, fbs, thalach, exang):
    model_input = [age, sex, cp, trestbps, chol, fbs, thalach, exang]
    return clf.predict([model_input])[0]


@app.route("/")
def status():
    return "The app is up!"

@app.route("/classify", methods=["POST"])
def classify():
    data_dict = request.get_json()

    age = data_dict['age'], 
    sex = data_dict['sex'], 
    cp = data_dict['cp'], 
    trestbps = data_dict['trestbps'], 
    chol = data_dict['chol'], 
    fbs = data_dict['fbs'], 
    thalach = data_dict['thalach'], 
    exang = data_dict['exang']
    
    return jsonify{
        "age" = age, 
        "sex" = sex, 
        "cp" = cp, 
        "trestbps" = trestbps, 
        "chol" = chol, 
        "fbs" = fbs, 
        "thalach" = thalach, 
        "exang" = exang
    }