class Multiplier:
    def __init__(self, busybit):
        self.busybit = busybit

    def output(self,arg1,arg2,func):

        if(func=="*"):
             # print(arg1)
             # print(arg2)
             return arg1 * arg2
        else:
            # print(arg1)
            # print(arg2)
            return arg1 / arg2


    def Makebusy(self):
        self.busybit = 1

    def Makefree(self):
        self.busybit = 0
