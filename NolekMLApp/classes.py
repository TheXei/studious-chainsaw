class testData:
    
    
    x_max = int()
    y_max = int()
    
    def __init__(self, _Test_Dur, _Y_Vals):
        self.SetTestDuration(_Test_Dur)
        self.SetYValues(_Y_Vals)
        self.SetXValues(self.y_vals)
        self.FindYMax()
        self.x_max = self.x_vals[-1]
    
    def SetTestDuration(self, x):
        self.test_Dur = x[0]
        
    def SetXValues(self, valList):
        self.x_vals = range(0, len(valList))
    
    def SetYValues(self, valList):
        y_list = []
        for x in valList:
            y_list = list(x.split(";"))
        
        for i in y_list:
            self.y_vals.append(int(i))
    
    def FindYMax(self):
        for x in self.y_vals:
            if x > self.y_max:
                self.y_max = x
        self.y_max = self.y_max + (self.y_max/100*10)