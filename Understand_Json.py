import json

file_path=r"C:\Python_Stuff\skycopetechnologies\data.json"
with open(file_path,'r') as file:
    data=json.load(file)
    
for key, value in data.items():
    print(f"{key}")
    print (f"{value}")