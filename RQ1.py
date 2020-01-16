# import JSON package
import json

# load and read data India json file
with open('conflict_data_India.json', encoding='utf-16') as file: 
    India_data  = json.load(file) 

dictionary_1 = India_data[1]
print(dictionary_1)