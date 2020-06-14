class SS:
    def __init__(self,type,busy,operation,s1,s2,d1,ready,inumber):
        self.type = type
        self.busy = busy
        self.operation = operation
        self.s1 = s1
        self.s2 = s2
        self.d1 = d1
        self.ready = ready
        self.inumber = inumber

    def issueto(self):
        self.busy = 'No'
        self.operation = ''
        self.s1 = ''
        self.s1 = ''
        self.d1 = ''
        self.inumber = ""
        self.ready = 'No'

    def fill(self,op,s1,s2,d1,inum):
       self.busy = 'Yes'
       self.operation = op
       self.s1 = s1
       self.s2 = s2
       self.d1 = d1
       self.inumber = inum

    def getarg1(self):
        return self.s1

    def setarg1(self,s):
        self.s1 = s

    def getarg2(self):
        return self.s2

    def setarg2(self,s):
        self.s2 = s

    def getd(self):
        return self.d1

    def Makeready(self):
         self.ready = "Yes"

    def getreadybit(self):
          return self.ready

    def gettype(self):
           return self.type

    def getoperation(self):
           return self.operation

    def getbusy(self):
        return self.busy

    def getinum(self):
        return self.inumber
