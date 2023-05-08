import pandas as pd
import datetime as dt

def test_script_csv():
    data = pd.read_csv('Marcus-Test-Data\D22102_R1.1_Test_230226.csv', sep=';')
    logTime = data['Log Time']
    stepNo = data['StepNo']
    b22 = data['B22']
    presure = []
    logTimes = []
    stepNos =[]
    
    for str in b22:
        if "," in str:
            myStr = str.replace(",", ".")
            presure.append(float(myStr))
        else:
            presure.append(float(str))
    
    for x in logTime:
        dt_obj = dt.datetime.strptime(x, '%d/%m/%Y %H.%M.%S')
        logTimes.append(dt_obj)
        
    for x in stepNo:
        stepNos.append(x)
    
    time_list = []
    step_list = []
    presure_list = []
    test_list = []
    success = 0
    fails = 0
    
    for time,step,pres in zip(logTimes, stepNos, presure):
        time_list.append(time)
        step_list.append(step)
        presure_list.append(pres)
        if step == 44000 or step == 44500 or step == 45000:
            test_list.append(pres)
            if len(test_list) >= 2:
                pres_diff = test_list[-2] / test_list[-1]
                if pres_diff > 0.99 and pres_diff < 1.01:
                    print('Success')
                    success = success + 1
                else:
                    print('Fail')
                    fails = fails + 1
        else:
            continue

    print('Number of sucesses: ', success)
    print('Number of fails: ', fails)

test_script_csv()

        
# ani = FuncAnimation(plt.gcf(), test_script_csv, interval=1000)

# plt.tight_layout()
# plt.show()


        # plt.cla()
    
        # fig, ax = plt.subplots()
        
        # plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y %H:%M'))
        # plt.gca().xaxis.set_major_locator(mdates.MinuteLocator(interval=15))
        
        # ax.plot(time_list, presure_list, 'b', label='Presure at B22 sensor')
        # ax.set_xlabel("Time of measurement")
        # ax.set_ylabel("Presure in bar")
        # ax0 = ax.twinx()
        # ax0.plot(time_list, step_list, 'g--', label='StepNo')
        # ax0.set_ylabel("StepNo")
        
        # plt.title("Presure Test")
        # plt.gcf().autofmt_xdate()
        # ax.legend(loc=9)
        # ax0.legend()
        # plt.tight_layout()