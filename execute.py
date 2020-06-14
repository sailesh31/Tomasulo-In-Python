from adder import *
from multiplier import *
from initialization import *
from common_data_bus import *

def Execute(A,time,FU):
     Load_Latency  = 2
     Add_Latency  = 2
     Sub_Latency = 2
     Store_Latency  = 2
     Multiply_Latency  = 10
     Divide_Latency  = 40

     if(A.gettype()=="Add"):
         FUAdd[FU].Makebusy()
         output = FUAdd[FU].output(int(A.getarg1()),int(A.getarg2()),A.getsign())
         CDB(A.getinum(),output)

     elif(A.gettype()=="Mul"):
        FUMul[FU-3].Makebusy()
        if(A.getoperation()=="Mul"):

              output = FUMul[FU-3].output(A.getarg1(),A.getarg2(),A.getsign())
              CDB(A.getinum(),output)
              FUMul[FU-3].Makefree()
        else:

                output = FUMul[FU-3].output(A.getarg1(),A.getarg2(),A.getsign())
                CDB(A.getinum(),output)
                FUMul[FU-3].Makefree()

     elif(A.gettype()=="Load"):

             output = A.getd()+A.getarg()
             CDB(A.getinum(),output)
