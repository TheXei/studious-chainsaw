import pandas as pd
import csv
import time

data = pd.read_csv('C:\\Users\Marcus\Documents\studious-chainsaw\Marcus-Test-Data\D22102_R1.1_Test_230226.csv', sep=';')
logTime = data['Log Time']
stepNo = data['StepNo']
b31 = data['B31']
b32 = data['B32']
b22 = data['B22']

fieldnames = ["Log Time", "StepNo", "B31", "B32", "B22"]

with open('data.csv', 'w') as csvfile:
    csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csv_writer.writeheader()

i = 0

while True:
    
    with open('data.csv', 'a') as csvfile:
        csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        info = {
            "Log Time" : logTime[i],
            "StepNo" : stepNo[i],
            "B31" : b31[i],
            "B32" : b32[i],
            "B22" : b22[i]
        }
        
        csv_writer.writerow(info)
        print(logTime[i], stepNo[i], b31[i], b32[i], b22[i])
        i = i+1
        
    time.sleep(1)
        