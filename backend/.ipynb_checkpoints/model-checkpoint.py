import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import joblib


df = pd.read_csv("heart_disease_data.csv")

df = (
    df.drop("restecg", axis=1)
    .drop("oldpeak", axis=1)
    .drop("slope", axis=1)
    .drop("ca", axis=1)
    .drop("thal", axis=1)
)

y = df["condition"].values
X = df.drop("condition", axis=1).values

dt_p_fin = DecisionTreeClassifier(criterion="entropy", max_depth=7)
dt_p_fin.fit(X_train, y_train)
y_test_pred_dt_p_fin = dt_p_fin.predict(X_test)
print("Criterion=entropy", classification_report(y_test, y_test_pred_dt_p_fin))

dt_p_fin.fit(X, y)

joblib.dump(dt_p_fin, "clf.joblib")