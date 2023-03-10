import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
import classes as cls

data = pd.read_csv('C:\\Users\Marcus\Documents\studious-chainsaw\Marcus-Test-Data\D22102_R1.1_NolekTest_230226.csv', sep=';')
logTime = data['LogTime']
stepNo = data['StepNo']
b31 = data['B31']
b32 = data['B32']
b22 = data['B22']

test = cls.testData(logTime, stepNo, b31, b32, b22)

xvals = test.logTimes

fig, ax = plt.subplots(2)

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=15))

ax[0].plot(xvals, test.b22, 'b', label='Presure at B22 sensor')
ax[0].set_xlabel("Time of measurement")
ax[0].set_ylabel("Presure in bar")
ax0 = ax[0].twinx()
ax0.plot(xvals, test.b31, 'g--', label='Temperature at B31 sensor')
ax0.plot(xvals, test.b32, 'r--', label='Temperature at B32 sensor')
ax0.set_ylabel("Temperature in celcius")

ax[1].plot(xvals, test.b22, 'b', label='Presure at B22 sensor')
ax[1].set_xlabel("Time of measurement")
ax[1].set_ylabel("Presure in bar")
ax1 = ax[1].twinx()
ax1.plot(xvals, test.stepNos, 'g--', label='StepNo')
ax1.set_ylabel("StepNo")

plt.title("Presure Test")
plt.gcf().autofmt_xdate()
plt.tight_layout()
ax[0].legend(loc=9)
ax0.legend()
ax[1].legend(loc=9)
ax1.legend()

plt.show()
