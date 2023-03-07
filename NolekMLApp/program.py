import pandas as pd
from matplotlib import pyplot as plt
import classes as cls

data = pd.read_csv('C:\\Users\Marcus\Documents\studious-chainsaw\Marcus-Test-Data\D22102_R1.1_NolekTest_230226.csv', sep=';')
logTime = data['LogTime']
stepNo = data['StepNo']
b31 = data['B31']
b32 = data['B32']
b22 = data['B22']

test = cls.testData(logTime, stepNo, b31, b32, b22)

# print(type(test.logTime[0]))
print(type(test.stepNo[0]))
print(type(test.b31[0]))
print(type(test.b32[0]))
print(type(test.b22[0]))

fig, ax1 = plt.subplots()

ax2 = ax1.twinx()
ax1.plot(test.b22, 'b', label='Presure at B22 sensor')
ax2.plot(test.b31, 'g--', label='Temperature at B31 sensor')
ax2.plot(test.b32, 'r--', label='Temperature at B32 sensor')

ax1.set_ylabel("Presure in bar")
ax2.set_ylabel("Temperature in celcius")

plt.title("Presure Test")
plt.tight_layout()
ax1.legend(loc=9)
ax2.legend()
plt.show()
