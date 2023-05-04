from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import dates as mdates
import pandas as pd
import datetime as dt

data = pd.read_csv('Marcus-Test-Data\D22102_R1.1_Test_230226.csv', sep=';')
logTime = data['Log Time']
stepNo = data['StepNo']
b22 = data['B22']

class testData:
    logTimes = []
    stepNos = []
    b22 = []
    
    def __init__(self, _logTime, _stepNo, _b22):
        """_summary_

        Args:
            _logTime (DateTime): Day and Time of logging
            _stepNo (Integer): The step number the test is at
            _b22 (Float): Presure in bar at B22 sensor
        """
        self.SetLogTime(_logTime)
        self.SetStepNo(_stepNo)
        self.SetB22(_b22)
        
    def SetLogTime(self, valList):
        dt_obj = None
        for x in valList:
            dt_obj = dt.datetime.strptime(x, '%d/%m/%Y %H.%M.%S')
            self.logTimes.append(dt_obj)
            
    
    def SetStepNo(self, valList):
        for x in valList:
            self.stepNos.append(x)
    

    def SetB22(self, valList): 
        for str in valList:
            if "," in str:
                myStr = str.replace(",", ".")
                self.b22.append(float(myStr))
            else:
                self.b22.append(float(str))
                
def _script(object):
    """
        Script for comparing a new value in b22 to all the others to see if presure has fallen
    """
    return


test = testData(logTime, stepNo, b22)

xvals = test.logTimes

fig, ax = plt.subplots()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y %H:%M'))
plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=15))

ax.plot(xvals, test.b22, 'b', label='Presure at B22 sensor')
ax.set_xlabel("Time of measurement")
ax.set_ylabel("Presure in bar")
ax0 = ax.twinx()
ax0.plot(xvals, test.stepNos, 'g--', label='StepNo')
ax0.set_ylabel("StepNo")

plt.title("Presure Test")
plt.gcf().autofmt_xdate()
ax.legend(loc=9)
ax0.legend()

plt.tight_layout()
plt.show()
