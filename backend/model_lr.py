# import packages
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import make_pipeline

import joblib

# read in data
df = pd.read_csv("heart_disease_data.csv")

# drop unused columns
df = (
    df.drop("restecg", axis=1)
    .drop("oldpeak", axis=1)
    .drop("slope", axis=1)
    .drop("ca", axis=1)
    .drop("thal", axis=1)
)

# rename exang: exercise induced angina (1 = yes; 0 = no)
df = df.assign(exang=lambda df: df["exang"].replace({0: "no", 1: "yes"}))

# rename sex
df = df.assign(sex=lambda df: df["sex"].replace({0: "female", 1: "male"}))

# rename fbs: (fasting blood sugar > 120 mg/dl) (1 = true; 0 = false)
df = df.assign(fbs=lambda df: df["fbs"].replace({0: "false", 1: "true"}))

# rename cp: chest pain type
df = df.assign(
    cp=lambda df: df["cp"].replace(
        {
            0: "typical angina",
            1: "atypical angina",
            2: "non-anginal pain",
            3: "asymptomatic",
        }
    )
)

# Set x and y
target = "condition"

y = df["condition"]
X = df.drop("condition", axis=1)

cf = ColumnTransformer(
    [
        ("numerical", "passthrough", ["age", "trestbps", "chol", "thalach"],),
        ('"categorical"', OneHotEncoder(drop="first"), ["sex", "cp", "fbs", "exang"]),
    ]
)

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, stratify=y)

# train model 
lr_pipeline = make_pipeline(cf, LogisticRegression())

lr_pipeline.fit(X, y)

# create joblib file
joblib.dump(lr_pipeline, "clf.joblib")