class PC:
    def __init__(self, addr):
        self.addr = addr

    def currentPC(self):
        return self.addr

    def incPC(self):
        self.addr = self.addr + 1

    def updatePC(self,imm):
        self.addr = self.addr + imm
