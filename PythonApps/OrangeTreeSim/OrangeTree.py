class OrangeTree:
    age = int()
    height = int()
    treeAlive = bool()
    numOranges = int()
    orangesEaten = int()
    
    def __init__(self, age, height, treeAlive):
        try: 
            if age >= 0: self.age = age
        except:
            print("Age can't be a negative number, please try again")
        self.height = height
        self.treeAlive = treeAlive
    
    def OneYearPasses(self):
        self.age = self.age + 1
        self.numOranges = 0
        self.orangesEaten = 0
        if self.age < 80:
            self.height = self.height + 2
        else:
            self.treeAlive = False
        if self.age >= 2 and self.age < 80: self.numOranges = self.age * 5-5
    
    def EatOranges(self, count):
        if count <= self.numOranges:
            self.numOranges = self.numOranges - count
            self.orangesEaten = self.orangesEaten + count