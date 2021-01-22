import pandas as pd
df=pd.read_csv('heart_disease_data.csv')
for index, row in df.iterrows():
    d=row.to_dict()
    print(d)