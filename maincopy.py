from initialization import *
from multiprocessing import Process
from operator import itemgetter

def Extract(lst):
    return list( map(itemgetter(0), lst ))

def CheckReady():
    for i in range(0,5):
      if(RSC[i].getbusy()=="Yes"):
        if(str(RSC[i].getarg2())[0]!="R" and str(RSC[i].getarg1())[0]!="R" ):
            RSC[i].Makeready()
    for i in range(0,3):
     if(LSC[i].getbusy()=="Yes"):
        if(str(LSC[i].getarg()) [0]!="R"):
            LSC[i].Makeready()
    for i in range(0,3):
         if(SSC[i].getbusy()=="Yes"):
            if(str(SSC[i].getarg2())[0]!="R" and str(SSC[i].getarg1())[0]!="R" ):
                # print("Timer")
                # print(Universal_Clock.currenttime())
                # print(SSC[i].getarg2())
                # print(SSC[i].getarg1())
                SSC[i].Makeready()

def CheckExec():
   pop_l=[]
   # print(execute_array)
   for i in range(len(execute_array)):
       A = execute_array[i][0]
       time = execute_array[i][1]
       FU = execute_array[i][2]

       if(A.gettype()=="Add"):
           if(Universal_Clock.currenttime() == time+2):
               output = FUAdd[FU].output(int(A.getarg1()),int(A.getarg2()),A.getsign())
               CDB(A.getinum(),output)
               print("Publishing Add")
               RSC[FU].issueto()
               pop_l.append(i)

       elif(A.gettype()=="Mul"):
                if(A.getoperation()=="Mul"):
                     if(Universal_Clock.currenttime() == time+10):
                      output = FUMUL[FU-3].output(A.getarg1(),int(A.getarg2()),A.getsign())
                      CDB(A.getinum(),output)
                      print("Publishing Mul")
                      # print("Executed Mul instruction number: "+str(A.getinum()))
                      RSC[FU].issueto()
                      pop_l.append(i)
                elif(A.getoperation()=="Div"):
                    if(Universal_Clock.currenttime() == time+40):
                        # print("DOING")
                        output = FUMUL[FU-3].output(A.getarg1(),int(A.getarg2()),A.getsign())
                        CDB(A.getinum(),output)
                        print("Publishing Divide")
                        # print("Executed Div instruction number: "+str(A.getinum()))
                        RSC[FU].issueto()
                        pop_l.append(i)

       elif(A.gettype()=="Load"):
          if(Universal_Clock.currenttime() == time+2):
             output = Data_Memory[int(A.getd())+int(A.getarg())]
             CDB(A.getinum(),output)
             print("Publishing Load")
             # print("Executed Load instruction number: "+str(A.getinum()))
             LSC[FU].issueto()
             pop_l.append(i)
             # earray.pop(0)

       elif(A.gettype()=="Store"):
           if(Universal_Clock.currenttime() == time+2):
                   # print("Arg1 "+A.getarg1())
                   # print("Argg")
                   # print(A.getarg2())
                   Data_Memory[int(A.getd())+int(A.getarg2())] = Register_Bank["R"+str(A.getarg1())]
                   # print("Executed Store instruction number: "+str(A.getinum()))
                   SSC[FU].issueto()
                   pop_l.append(i)
                   earray.pop(0)


   if(len(pop_l)!=0):
     pop_l.reverse()
     # print((pop_l))
     b = len(pop_l)
     # print(b)
     for j in range(b):
       execute_array.pop(pop_l[j])

decode_unit_free = 1
instruction_number = 1
dectypeins = ["BNE","BEQ","BLT","BGT","JAL","JALR"]
print("Time0")
head = 0;
# earray.append(0)
# earray.pop(0)
# Universal_Clock.clocktick()
while(True):
 # print(Reorder_Buf    fer)
 # print("ER")
 # print(execute_array)
 # print("PEndROB")
 # print(Pending_ROB)
 if(decode_unit_free):
        #print("Free")
        instruction = Fetch(Instruction_Memory,Program_Counter.currentPC())
        Program_Counter.incPC()
        decoded_instruction = Decode(instruction)
        renamed_instruction = RegisterRenaming(decoded_instruction)
        renamed_instruction = Decode(renamed_instruction)
        print("Instruction Feteched: "+ str(decoded_instruction) + " >> " + str(renamed_instruction))
        # print(earray)
        if(decoded_instruction[0]=="END"):
             print("END")
             break

 if(renamed_instruction[0] not in dectypeins):
             decode_unit_free,instruction_number = Issue(renamed_instruction,instruction_number)
             if(decode_unit_free ):
                earray.append(1)
             # print("Return"+str(instruction_number))
 elif(renamed_instruction[0] in dectypeins):
             decode_unit_free = DecodeBJ(renamed_instruction)


 CheckReady()
 CheckExec()
 for i in range(0,5):
        if(RSC[i].getreadybit() == 'Yes'):
          # print("Extract")
          # print(Extract(execute_array))
          if(RSC[i] not in Extract(execute_array)):
            execute_array.append([RSC[i],Universal_Clock.currenttime(),i])
            if(i<3):
                print("Exection in Add unit -- operation -- "+ RSC[i].getoperation())
            else:
                print("Exection in Mul unit  -- operation -- "+  RSC[i].getoperation() )
            # RSC[i].Makeunready()
            # RSC[i].Makeunbusy()


 for j in range(0,3):
        if(LSC[j].getreadybit()== 'Yes'):
         if(LSC[j] not in Extract(execute_array)):
            execute_array.append([LSC[j],Universal_Clock.currenttime(),j])
            print("Exection in Load unit -- operation -- Load")
            # LSC[j].Makeunready()
            # LSC[j].Makeunbusy()


 for l in range(0,3):
        if(SSC[l].getreadybit()== 'Yes'):
         if(SSC[l] not in Extract(execute_array)):
            execute_array.append([SSC[l],Universal_Clock.currenttime(),l])
            print("Exection in Store unit -- operation -- Store")
            # SSC[l].Makeunready()
            # SSC[l].Makeunbusy()


 for k in range(0,32):
        if(Reorder_Buffer["ROB"+str(k)][2]!='No'):
            # print("Comminting ROB "+str(k))
            ROBCommit("ROB"+str(k))



 print("Time"+str(Universal_Clock.currenttime()))
 Pending_ROB_Commits()
 Universal_Clock.clocktick()

# print("HereTher")

# while(Universal_Clock.currenttime()<200):

 # print(execute_array)
while(len(earray)!=0):
 # print("PEndROB")
 # print(Pending_ROB)
 # print(Reorder_Buffer)
 CheckReady()
 CheckExec()
 for i in range(0,5):
     if(RSC[i].getreadybit() == 'Yes'):
        if(RSC[i] not in Extract(execute_array)):
         execute_array.append([RSC[i],Universal_Clock.currenttime(),i])
         if(i<3):
             print("Exection in Add unit -- operation -- "+ RSC[i].getoperation())
         else:
             print("Exection in Mul unit  -- operation -- "+  RSC[i].getoperation() )
         # RSC[i].Makeunready()
         # RSC[i].Makeunbusy()


 for j in range(0,3):
     if(LSC[j].getreadybit()== 'Yes'):
      if(LSC[j] not in Extract(execute_array)):
         execute_array.append([LSC[j],Universal_Clock.currenttime(),j])
         print("Exection in Load unit -- operation -- Load")
         # LSC[j].Makeunready()
         # LSC[j].Makeunbusy()
 for l in range(0,3):
        if(SSC[l].getreadybit()== 'Yes'):
         if(SSC[l] not in Extract(execute_array)):
            execute_array.append([SSC[l],Universal_Clock.currenttime(),l])
            print("Exection in Store unit -- operation -- Store")

 for k in range(0,32):
     if(Reorder_Buffer["ROB"+str(k)][2]!='No' ):
         ROBCommit("ROB"+str(k))


 Pending_ROB_Commits()

 print("Time"+str(Universal_Clock.currenttime()))
 # Pending_ROB_Commits(earray)
 Universal_Clock.clocktick()
# print(Reorder_Buffer["ROB7"][1])
# print(earray)
#Uncommment the below print functions to see the final state of memories
# print(earray)
# print(Instruction_Memory)
# print(Register_Bank)
# print(Physical_Registers)
# print(Universal_Clock.currenttime())
# print(Data_Memory)
