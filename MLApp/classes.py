import datetime as dt

class testData:
    logTimes = []
    stepNos = []
    b31 = []
    b32 = []
    b22 = []
    
    # x_max = dt.datetime()
    # y_max = float()
    
    def __init__(self, _logTime, _stepNo, _b31, _b32, _b22):
        """_summary_

        Args:
            _logTime (DateTime): Day and Time of logging
            _stepNo (Integer): The step number the test is at
            _b31 (Float): Temperature at B31 sensor
            _b32 (Float): Temperature at B32 sensor
            _b22 (Float): Preasure in bar at B22 sensor
        """
        self.SetLogTime(_logTime)
        self.SetStepNo(_stepNo)
        self.SetB31(_b31)
        self.SetB32(_b32)
        self.SetB22(_b22)
        
    def SetLogTime(self, valList):
        dt_obj = None
        for x in valList:
            dt_obj = dt.datetime.strptime(x, '%d/%m/%Y %H.%M.%S')
            self.logTimes.append(dt_obj)
            
    
    def SetStepNo(self, valList):
        for x in valList:
            self.stepNos.append(x)
    
    def SetB31(self, valList):
        for str in valList:
            if "," in str:
                myStr = str.replace(",", ".")
                self.b31.append(float(myStr))
            else:
                self.b31.append(float(str))
    
    def SetB32(self, valList):
        for str in valList:
            if "," in str:
                myStr = str.replace(",", ".")
                self.b32.append(float(myStr))
            else:
                self.b32.append(float(str))

    def SetB22(self, valList): 
        for str in valList:
            if "," in str:
                myStr = str.replace(",", ".")
                self.b22.append(float(myStr))
            else:
                self.b22.append(float(str))

    
    # def FindYMax(self):
    #     for x in self.y_vals:
    #         if x > self.y_max:
    #             self.y_max = x
    #     self.y_max = self.y_max + (self.y_max/100*10)