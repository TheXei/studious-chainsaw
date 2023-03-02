import pandas as pd
from matplotlib import pyplot as plt
import plotClass as pc

plt.style.use("fivethirtyeight")

data = pd.read_csv('C:\\Users\Marcus\Documents\PythonApps\matPlotTesting\Test_data.csv')
testDur = data['Test_Duration']
preVals = data['Presure_Values']

myPlot = pc.Plot(testDur, preVals)

plt.plot(myPlot.x_vals, myPlot.y_vals)

plt.title("Presure Test")
plt.ylabel("Presure in mbar")
plt.tight_layout()
plt.axis([0, myPlot.x_max, 0, myPlot.y_max])
plt.show()
