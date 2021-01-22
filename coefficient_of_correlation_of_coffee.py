import numpy as np
import csv

def get_data_souce(data_path):
    coffee = []
    sleep = []
    with open(data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row['Coffee in ml']))
            sleep.append(float(row['sleep in hours']))
    return {"x": coffee, "y": sleep}
    

def find_corelation(data_source):
    correlation = np.corrcoef(data_source["x"], data_source["y"])
    print(correlation[0, 1])

def setup():
    data_path = 'E:\Python\WHJR_PYTHON\cl106\coffee.csv'
    data_source = get_data_souce(data_path)
    find_corelation(data_source)

setup()
