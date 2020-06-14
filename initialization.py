# Initializing the clock
from clock import *

Universal_Clock = Clock(1)

#Initializing Memory
from data_memory import *
from instruction_memory import *
from register_bank import *
from physical_registers import *

f1 = open("Program6.txt","r")
f2 = open("Memory1.txt","r")
f3 = open("RegBank1.txt","r")

temp_ins = f1.read()
temp_ins = temp_ins.split("\n")
ins = [i for i in temp_ins if i ]

temp_mem = f2.read()
temp_mem = temp_mem.split("\n")
mem = [i for i in temp_mem if i]

temp_rb = f3.read()
temp_rb = temp_rb.split("\n")
rb = [i for i in temp_rb if i]

f1.close()
f2.close()
f3.close()

for i in range(0,len(ins)):
   temp_text = ins[i].split(",")
   Instruction_Memory[int(temp_text[0])] = temp_text[1]

for i in range(0,len(mem)):
    temp_text = mem[i].split(",")
    Data_Memory[int(temp_text[0])] = int(temp_text[1])

for i in range(0,len(rb)):
    temp_text = rb[i].split(",")
    Register_Bank["R"+(temp_text[0])] = int(temp_text[1])

#Defining Latencies for Functional Units
Load_Latency  = 2
Add_Latency  = 2
Sub_Latency = 2
Store_Latency  = 2
Multiply_Latency  = 10
Divide_Latency  = 40

#All instruction array
ALLI =  ["ADD","SUB","MUL","DIV","XOR","OR","AND","LD","SD","ADDI","SUBI","MULI","DIVI","JALR","BNE","BEQ","BLT","BGT","JAL"]

#Initializing Reservation Station Units
from reservation_station import *
from load_station import *
from store_station import *
RSAdd1 = RS('Add','No','','','','','','No',"")
RSAdd2 = RS('Add','No','','','','','','No',"")
RSAdd3 = RS('Add','No','','','','','','No',"")

RSMul1 = RS('Mul','No','','','','','','No',"")
RSMul2 = RS('Mul','No','','','','','','No',"")

RSC = [RSAdd1,RSAdd2,RSAdd3,RSMul1,RSMul2]

#Initializing Load Station Units
LS1 = LS('Load','No','','','',"No","")
LS2 = LS('Load','No','','','',"No","")
LS3 = LS('Load','No','','','',"No","")

LSC = [LS1,LS2,LS3]

SS1 = SS('Store','No','','','','',"No","")
SS2 = SS('Store','No','','','','',"No","")
SS3 = SS('Store','No','','','','',"No","")

SSC = [SS1,SS2,SS3]

#Initialozing Functional Units
from adder import *
from multiplier import *
Adder1 = Adder(0)
Adder2 = Adder(0)
Adder3 = Adder(0)

MUL1 = Multiplier(0)
MUL2 = Multiplier(0)

FUAdd = [Adder1,Adder2,Adder3]
FUMUL = [MUL1,MUL2]

#Additional Variables
execute_array=[]
earray = []


#Initializing ROB
from reorder_buffer import *



#Initializing Program Counter
from program_counter import *
Program_Counter = PC(1)

#Loading Fetch functions
from fetch import *

#Loading Decode functions
from decode import *

#Loading Execution functions:
from execute import *

#loading CommonDataBus functions
from common_data_bus import *

#Register Renaming to avoid conflict
from register_renaming import *
