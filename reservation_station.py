# from initialization import *

class RS:
    def __init__(self,type,busy,operation,source1,source2,data1,data2,ready,inumber):
        self.type = type
        self.busy = busy
        self.operation = operation
        self.source1 = source1
        self.source2 = source2
        self.data1 = data1
        self.data2 = data2
        self.ready = ready
        self.inumber = inumber

    def issueto(self):
         self.busy = 'No'
         self.operation = ''
         self.source1 = ''
         self.source2 = ''
         self.data1 = ''
         self.data2 = ''
         self.inumber = ''
         self.ready = 'No'

    def fill(self,op,s1,s2,d1,d2,inum):
        self.busy = 'Yes'
        self.operation = op
        self.source1 = s1
        self.source2 = s2
        self.data1 = d1
        self.data2 = d2
        self.inumber  = inum

    def Makeready(self):
        self.ready = "Yes"

    def Makefree(self):
        self.ready = "No"

    def getreadybit(self):
       return self.ready

    def Makeunready(self):
        self.ready = "No"

    def Makeunbusy(self):
        self.busy = 'No'

    def gettype(self):
        return self.type

    def getbusy(self):
        return self.busy

    def getoperation(self):
        return self.operation

    def getarg1(self):
        return self.data1

    def getsource1(self):
        return (self.source1)

    def getsource2(self):
        return (self.source2)

    def setarg1(self,d):
        self.data1 = d

    def setarg2(self,d):
        self.data2 = d

    def getarg2(self):
        return self.data2

    def getsign(self):
        tmp = {"Add":"+","Sub":"-","Mul":"*","Div":"/"}
        return tmp[self.operation]

    def getinum(self):
        return self.inumber
