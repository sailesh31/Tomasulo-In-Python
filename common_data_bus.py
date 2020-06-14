#Function used to mimic the working of CDB, i.e. publish data to ROB and RS after execution unit produces result
from initialization import *

def CDB(inum,val):
    # print("IV")
    # print(inum)
    # print(val)
    for i in range(0,32):
        if(Reorder_Buffer["ROB"+str(i)][0]==inum):
            Reorder_Buffer["ROB"+str(i)][2] = val
            print("Caught ROB"+str(i))
            # print("VALUE writting back to"+" "+str(Reorder_Buffer["ROB"+str(i)][1])+" "+str(val))
            break

    for j in range(0,5):
        if(RSC[j].getarg1()=="ROB"+str(i)):
           # print("Match")
           RSC[j].setarg1(val)
        if(RSC[j].getarg2()=="ROB"+str(i)):
            # print("Match")
            RSC[j].setarg2(val)
            # print("RSC")
            # print(RSC[j].getarg2())
    for k in range(0,3):
           if(LSC[k].getarg()=="ROB"+str(i)):
              LSC[k].setarg(val)

    for l in range(0,3):
           if(SSC[l].getarg1()=="ROB"+str(i)):
              # print("Almost Done")
              SSC[l].setarg1(val)
           if(SSC[l].getarg2()=="ROB"+str(i)):
              # print("Almost Done")
              SSC[l].setarg2(val)
