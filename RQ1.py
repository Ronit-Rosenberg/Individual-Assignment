# import JSON package
import json

# load and read data India json file
with open('conflict_data_India.json', encoding='utf-16') as file: 
    India_data  = json.load(file) 

# # select the first dictionary of the list
# dictionary1 = India_data[0]
# print(dictionary1)

# load the selected data into a csv file
with open('India_data_filtered.csv', 'w') as file:
    # give the csv file a header
    file.write(f'id, year, deaths_best_estimate\n')
    # loop over all the measurements in the data file and add it to the csv file
    for measurement in India_data:
        # load the selected data into the csv file for every dictionary within the list of India data
        file.write(f'{measurement["id"]}, {measurement["year"]}, {measurement["best"]}\n')