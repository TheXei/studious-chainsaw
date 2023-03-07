import pandas as pd
from matplotlib import pyplot as plt


plt.style.use("fivethirtyeight")

data = pd.read_csv('C:\\Users\Marcus\Documents\studious-chainsaw\Marcus-Test-Data\D22102_R1.1_NolekTest_230226.csv')
logTime = data['LogTime']
stepNo = data['StepNo']
circuitName = data['CircuitName']
tmp1 = data['TMP1']
tmp2 = data['TMP2']
b31 = data['B31']
b32 = data['B32']
b21 = data['B21']
b22 = data['B22']
p101 = data['P101']
regSP = data['RegulatorSP']
regFB = data['RegulatorFB']

print(b22)