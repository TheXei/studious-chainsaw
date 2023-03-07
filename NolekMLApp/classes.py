import datetime as dt

class testData:
    logTime = []
    stepNo = []
    b31 = []
    b32 = []
    b22 = []
    
    # x_max = dt.datetime()
    # y_max = float()
    
    def __init__(self, _logTime, _stepNo, _b31, _b32, _b22):
        # self.SetLogTime(_logTime)
        self.SetStepNo(_stepNo)
        self.SetB31(_b31)
        self.SetB32(_b32)
        self.SetB22(_b22)
        
    def SetLogTime(self, valList):
        for x in valList:
            self.logTime.append(dt.datetime(x))
    
    def SetStepNo(self, valList):
        for x in valList:
            self.stepNo.append(x)
    
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