import json

with open('heart_data_dict.txt') as f: 
    data = f.read() 


json_string = json.dumps(data)
print(json_string)