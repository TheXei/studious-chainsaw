import datetime as dt

class testData:
    logTime = []
    stepNo = []
    b31 = []
    b32 = []
    b22 = []
    
    x_max = dt.datetime()
    y_max = float()
    
    def __init__(self, _logTime, _stepNo, _b31, _b32, _b22):
        
    
    def SetTestDuration(self, x):
        self.test_Dur = x[0]
        
    def SetXValues(self, valList):
        self.x_vals = range(0, len(valList))
    
    def SetB31(self, valList):
        y_list = []
        for x in valList:
            y_list = list(x.split(";"))
        
        for i in y_list:
            self.y_vals.append(float(i))
    
    def SetB32(self, valList):
        y_list = []
        for x in valList:
            y_list = list(x.split(";"))
        
        for i in y_list:
            self.y_vals.append(float(i))

    def SetB22(self, valList):
        y_list = []
        for x in valList:
            y_list = list(x.split(";"))
    
        for i in y_list:
            self.y_vals.append(float(i))
    
    def FindYMax(self):
        for x in self.y_vals:
            if x > self.y_max:
                self.y_max = x
        self.y_max = self.y_max + (self.y_max/100*10)