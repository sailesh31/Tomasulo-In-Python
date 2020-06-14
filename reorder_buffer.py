Keys = ["ROB"+str(i) for i in range(0,32)]
Values = ['No','No','No']

Reorder_Buffer = dict.fromkeys(Keys)

Pending_ROB = []

global head
head = 0


for i in range(0,32):
    Reorder_Buffer[Keys[i]] = Values

from initialization import *




def ROBIssue(key,entry,ROB):
    global head
    ROB[key] = entry
    if(head<31):
      head = head+1
    else:
        head = 0


def ROBCommit(k):

    TempD = Reorder_Buffer[k]
    chek = int(k.replace("ROB",''))

    if(k!="ROB0" and Reorder_Buffer["ROB"+str(chek-1)][1]=="No"):
        Register_Bank[Physical_Registers_Map[int(TempD[1].replace('F',''))]] = int(TempD[2])
        print("Comminting "+Physical_Registers_Map[int(TempD[1].replace('F',''))] + " with value "+ str(TempD[2]) )
        if(k in Pending_ROB):
            Pending_ROB.remove(k)
        ROBClear(k)

    elif(k!="ROB0" and Reorder_Buffer["ROB"+str(chek-1)][1]!="No" ):
        if(k not in Pending_ROB):
            # print("Here")
            Pending_ROB.append(k)

    elif(k=="ROB0"):
        Register_Bank[Physical_Registers_Map[int(TempD[1].replace('F',''))]] = int(TempD[2])
        print("Comminting "+Physical_Registers_Map[int(TempD[1].replace('F',''))] + " with value "+ str(TempD[2]) )
        if(k in Pending_ROB):
                    Pending_ROB.remove(k)
        ROBClear(k)


def Get_Free_Rob():
    global head
    for i in range(head,32):
        if(Reorder_Buffer["ROB"+str(i)][1]=="No" and Reorder_Buffer["ROB"+str(i+1)][1]=='No'):
            break
    return "ROB"+str(i)

def ROBClear(k):
    # print("Err " +str(earray))
    earray.pop()
    # print("Err " +str(earray))
    Reorder_Buffer[k] = ['No','No','No']

def Pending_ROB_Commits():
    for i in range(len(Pending_ROB)):
        ROBCommit(Pending_ROB[i])
