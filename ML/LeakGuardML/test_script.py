import pandas as pd
import datetime as dt

def test_script_csv():
    """
        Load in a CSV file and converting some of the data so it can be used in this script
    """
    data = pd.read_csv('Marcus-Test-Data\D22102_R1.1_Test_230226.csv', sep=';')
    presure = []
    logTimes = []
    stepNos =[]
    
    for str in data['B22']:
        if "," in str:
            myStr = str.replace(",", ".")
            presure.append(float(myStr))
        else:
            presure.append(float(str))
    
    for x in data['Log Time']:
        dt_obj = dt.datetime.strptime(x, '%d/%m/%Y %H.%M.%S')
        logTimes.append(dt_obj)
        
    for x in data['StepNo']:
        stepNos.append(x)
    
    time_list = []
    step_list = []
    presure_list = []
    test_list = []
    success = 0
    fails = 0
    
    """
        Main part of the script
        Looks at each data entry for presure, and compares it to the previous data entry, but only for the data entry which is part of the step number between 44000 and 45000
        if the difference between the two data points is less than 0.1%, the test is successful
        but if the difference is higher, the test fails
    """
        
    for time,step,pres in zip(logTimes, stepNos, presure):
        time_list.append(time)
        step_list.append(step)
        presure_list.append(pres)
        if step == 44000 or step == 44500 or step == 45000:
            test_list.append(pres)
            if len(test_list) >= 2:
                pres_diff = test_list[-2] / test_list[-1]
                if pres_diff > 0.99 and pres_diff < 1.01:
                    print(pres_diff, ', Success')
                    success = success + 1
                else:
                    print(pres_diff, ', Fail')
                    fails = fails + 1
                    break
        else:
            continue
        
    # Printing the number of successes and fails discovered in the script
    print('Number of successes: ', success)
    print('Number of fails: ', fails)

test_script_csv()