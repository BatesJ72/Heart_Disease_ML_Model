# import csv
import pandas as pd

# Read in the data
with open('heart_disease_data.csv', 'r') as file:
    # data = file.read()
    # data = file.readlines()
    # data = file.readline()
    data = pd.read_csv('heart_disease_data.csv')

# Check Data
# print(data)
# print(data.dtypes)
# print(data.describe())


