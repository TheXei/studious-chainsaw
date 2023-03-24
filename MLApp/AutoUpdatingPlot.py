import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import dates as mdates
from matplotlib.animation import FuncAnimation
from itertools import count

index = count()

def animate(i):
    data = pd.read_csv('MLApp\data.csv')
    logTime = data['Log Time']
    stepNo = data['StepNo']
    b31 = data['B31']
    b32 = data['B32']
    b22 = data['B22']
    
    plt.cla()
    
    fig, ax = plt.subplots(2)
    
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y %H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=15))
    
    ax[0].plot(logTime, b22, 'b', label='Presure at B22')
    ax[0].set_xlabel("Time of measurement")
    ax[0].set_ylabel("Presure in bar")
    ax0 = ax[0].twinx()
    ax0.plot(logTime, b31, 'g--', label='Temp at B31')
    ax0.plot(logTime, b32, 'r--', label='Temp at B32')
    ax0.set_ylabel("Temp in Celcius")
    
    ax[1].plot(logTime, b22, 'b', label='Presure at B22 sensor')
    ax[1].set_xlabel("Time of measurement")
    ax[1].set_ylabel("Presure in bar")
    ax1 = ax[1].twinx()
    ax1.plot(logTime, stepNo, 'g--', label='StepNo')
    ax1.set_ylabel("StepNo")
    
    plt.title("Presure Test")
    plt.gcf().autofmt_xdate()
    ax[0].legend(loc=9)
    ax0.legend()
    ax[1].legend(loc=9)
    ax1.legend()
    plt.tight_layout()

ani = FuncAnimation(plt.gcf(), animate, interval=1000, cache_frame_data=False)

plt.tight_layout()
plt.show()