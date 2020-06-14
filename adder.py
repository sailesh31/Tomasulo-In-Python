#Adder Functional Unit used to do addition and subtraction

class Adder:
    def __init__(self, busybit):
        self.busybit = busybit

    def output(self,arg1,arg2,func):
        if(func=="+"):
            return arg1 + arg2
        else:
            return arg1 - arg2

    def Makebusy(self):
        self.busybit = 1

    def Makefree(self):
        self.busybit = 0
