import csv
import plotly.express as px
import numpy as np

def getData (data_path):
    Size_of_TV = []
    averageTimeSpent = []
    with open (data_path) as csv_file:
        csv_reader= csv.DictReader(csv_file)
        for row in csv_reader:
            Size_of_TV.append(float(row["Marks In Percentage"]))
            averageTimeSpent.append(float(row["Days Present"]))
    
    return {"x": Size_of_TV, "y": averageTimeSpent}

def findCorrelation (datasource):
    Correlation = np.corrcoef(datasource["x"], datasource["y"])

    print("Correlation = ", Correlation[0,1])


def setup():
    data_path="./data/Student Marks vs Days Present.csv"
    datasource= getData(data_path)
    findCorrelation(datasource)

setup()

