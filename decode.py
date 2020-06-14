from initialization import *
from reorder_buffer import *
# from vars import *

def Decode(ins):
    parts = ins.split(" ")
    return parts


def Issue(renamed_instruction,instruction_number):
    IS1 = ["ADD","SUB","MUL","DIV","XOR","OR","AND"]
    IS2 = ["LD","ADDI","SUBI","MULI","DIVI"]
    issuedbit = 0
    ninstruction_number = 0
    if(renamed_instruction[0] in IS1):

        rd = renamed_instruction[1]
        rs1 = renamed_instruction[2]
        rs2 = renamed_instruction[3]
        t1 = int(rs1.replace('F',''))
        t2 = int(rs2.replace('F',''))
        Physical_Registers[rs1] = Register_Bank[Physical_Registers_Map[t1]]
        Physical_Registers[rs2] = Register_Bank[Physical_Registers_Map[t2]]
        # print("PHYSCIAL VALS")

        for i in range(0,32):
            if (rs1 == Reorder_Buffer["ROB"+str(i)][1] and Reorder_Buffer["ROB"+str(i)][2]=='No'):
            # if (rs1 == Reorder_Buffer["ROB"+str(i)][1]):
                Physical_Registers[rs1] = "ROB"+str(i)
                # print("REP1")
                # print("ROB"+str(i))

        for i in range(0,32):
            if (rs2 == Reorder_Buffer["ROB"+str(i)][1] and Reorder_Buffer["ROB"+str(i)][2]=='No'):
            # if (rs2 == Reorder_Buffer["ROB"+str(i)][1]):
                Physical_Registers[rs2] = "ROB"+str(i)
                # print("REP2")
                # print("ROB"+str(i))

        # print(Physical_Registers[rs1])
        # print(Physical_Registers[rs2])

        if(renamed_instruction[0] == "ADD"):
            for i in range(0,3):
                if(RSC[i].getbusy()=='No'):
                    RSC[i].fill("Add",rs1,rs2,Physical_Registers[rs1],Physical_Registers[rs2],instruction_number)
                    print("Issued")
                    issuedbit = 1
                    ROBIssue(Get_Free_Rob(), [instruction_number,rd,'No'],Reorder_Buffer)
                    ninstruction_number = instruction_number+1
                    break

        if(renamed_instruction[0] == "SUB"):
            for i in range(0,3):
                if(RSC[i].getbusy()=='No'):
                    RSC[i].fill("Sub",rs1,rs2,Physical_Registers[rs1],Physical_Registers[rs2],instruction_number)
                    issuedbit = 1
                    ROBIssue(Get_Free_Rob(), [instruction_number,rd,'No'],Reorder_Buffer)
                    ninstruction_number = instruction_number+1
                    break

        if(renamed_instruction[0] == "MUL"):
                for i in range(3,5):
                    if(RSC[i].getbusy()=='No'):
                        RSC[i].fill("Mul",rs1,rs2,Physical_Registers[rs1],Physical_Registers[rs2],instruction_number)
                        issuedbit = 1
                        ROBIssue(Get_Free_Rob(), [instruction_number,rd,'No'],Reorder_Buffer)
                        ninstruction_number = instruction_number+1
                        break

        if(renamed_instruction[0] == "DIV"):
                for i in range(3,5):
                    if(RSC[i].getbusy()=='No'):
                        RSC[i].fill("Div",rs1,rs2,Physical_Registers[rs1],Physical_Registers[rs2],instruction_number)
                        issuedbit = 1
                        ROBIssue(Get_Free_Rob(), [instruction_number,rd,'No'],Reorder_Buffer)
                        ninstruction_number = instruction_number+1
                        break

    elif(renamed_instruction[0] =="SD"):
        rs1 = renamed_instruction[1]
        rs2 = renamed_instruction[2]
        imm = renamed_instruction[3]
        t1 = int(rs1.replace('F',''))
        t2 = int(rs2.replace('F',''))
        Physical_Registers[rs1] = Register_Bank[Physical_Registers_Map[t1]]
        Physical_Registers[rs2] = Register_Bank[Physical_Registers_Map[t2]]

        for i in range(0,32):
            if (rs1 == Reorder_Buffer["ROB"+str(i)][1] and Reorder_Buffer["ROB"+str(i)][2]=='No'):
                Physical_Registers[rs1] = "ROB"+str(i)
                # print("REP1")
                # print("ROB"+str(i))

        for i in range(0,32):
            if (rs2 == Reorder_Buffer["ROB"+str(i)][1] and Reorder_Buffer["ROB"+str(i)][2]=='No'):
                Physical_Registers[rs2] = "ROB"+str(i)
                # print("REP2")
                # print("ROB"+str(i))


        for i in range(0,3):
            if(SSC[i].getbusy()=='No'):
                # print("RSVALS")
                # print(rs1)
                # print(rs2)
                SSC[i].fill("Store",Physical_Registers[rs1],Physical_Registers[rs2],imm,instruction_number)
                issuedbit = 1
                ninstruction_number = instruction_number+1
                break


    elif(renamed_instruction[0] in IS2):
        rd = renamed_instruction[1]
        rs1 = renamed_instruction[2]
        imm = renamed_instruction[3]
        t1 = int(rs1.replace('F',''))
        Physical_Registers[rs1] = Register_Bank[Physical_Registers_Map[t1 ]]
        for i in range(0,32):
            if (rs1 == Reorder_Buffer["ROB"+str(i)][1] and Reorder_Buffer["ROB"+str(i)][2]=='No'):
                Physical_Registers[rs1] = "ROB"+str(i)


        # print(ninstruction_number)


        if(renamed_instruction[0] == "LD"):
            for i in range(0,3):
                if(LSC[i].getbusy()=='No'):
                    LSC[i].fill("Load",Physical_Registers[rs1],imm,instruction_number)
                    issuedbit = 1
                    ROBIssue(Get_Free_Rob(), [instruction_number,rd,'No'],Reorder_Buffer)
                    ninstruction_number = instruction_number+1
                    break

        if(renamed_instruction[0] == "ADDI"):
            for i in range(0,3):
                if(RSC[i].getbusy()=='No'):
                    RSC[i].fill("Add",rs1,"imm",Physical_Registers[rs1],imm,instruction_number)
                    issuedbit = 1
                    ROBIssue(Get_Free_Rob(), [instruction_number,rd,'No'],Reorder_Buffer)
                    ninstruction_number = instruction_number+1
                    break
        if(renamed_instruction[0] == "SUBI"):
            for i in range(0,3):
                if(RSC[i].getbusy()=='No'):
                    RSC[i].fill("Sub",rs1,"imm",Physical_Registers[rs1],imm,instruction_number)
                    issuedbit = 1
                    ROBIssue(Get_Free_Rob(), [instruction_number,rd,'No'],Reorder_Buffer)
                    ninstruction_number = instruction_number+1
                    break
        if(renamed_instruction[0] == "MULI"):
                for i in range(3,5):
                    if(RSC[i].getbusy()=='No'):
                        RSC[i].fill("Mul",rs1,"imm",Physical_Registers[rs1],imm,instruction_number)
                        issuedbit = 1
                        ROBIssue(Get_Free_Rob(), [instruction_number,rd,'No'],Reorder_Buffer)
                        ninstruction_number = instruction_number+1
                        break
        if(renamed_instruction[0] == "DIVI"):
                for i in range(3,5):
                    if(RSC[i].getbusy()=='No'):
                        RSC[i].fill("Div",rs1,"imm",Physical_Registers[rs1],imm,instruction_number)
                        issuedbit = 1
                        ROBIssue(Get_Free_Rob(), [instruction_number,rd,'No'],Reorder_Buffer)
                        ninstruction_number = instruction_number+1
                        break


    return issuedbit,ninstruction_number

def DecodeBJ(renamed_instruction):
    if(CheckVars(renamed_instruction)):
            if(renamed_instruction[0]=="BNE"):
                rs1 = renamed_instruction[1]
                rs2 = renamed_instruction[2]
                t1 = int(rs1.replace('F',''))
                t2 = int(rs2.replace('F',''))

                Physical_Registers[rs1] = Register_Bank[Physical_Registers_Map[t1]]
                Physical_Registers[rs2] = Register_Bank[Physical_Registers_Map[t2]]

                if(Physical_Registers[rs1]!=Physical_Registers[rs2]):
                    Program_Counter.updatePC(int(renamed_instruction[3]))
                return 1


            elif(renamed_instruction[0]=="BQE"):
                t1 = int(rs1.replace('F',''))
                t2 = int(rs2.replace('F',''))
                rs1 = renamed_instruction[1]
                rs2 = renamed_instruction[2]
                Physical_Registers[rs1] = Register_Bank[Physical_Registers_Map[t1]]
                Physical_Registers[rs2] = Register_Bank[Physical_Registers_Map[t2]]

                if(Physical_Registers[rs1]==Physical_Registers[rs2]):
                    Program_Counter.updatePC(int(renamed_instruction[3]))
                return 1

            elif(renamed_instruction[0]=="BLT"):
                rs1 = renamed_instruction[1]
                rs2 = renamed_instruction[2]
                t1 = int(rs1.replace('F',''))
                t2 = int(rs2.replace('F',''))

                Physical_Registers[rs1] = Register_Bank[Physical_Registers_Map[t1]]
                Physical_Registers[rs2] = Register_Bank[Physical_Registers_Map[t2]]

                if(Physical_Registers[rs1]<Physical_Registers[rs2]):
                    Program_Counter.updatePC(int(renamed_instruction[3]))
                return 1

            elif(renamed_instruction[0]=="BGT"):
                rs1 = renamed_instruction[1]
                rs2 = renamed_instruction[2]
                t1 = int(rs1.replace('F',''))
                t2 = int(rs2.replace('F',''))

                Physical_Registers[rs1] = Register_Bank[Physical_Registers_Map[t1]]
                Physical_Registers[rs2] = Register_Bank[Physical_Registers_Map[t2]]

                if(Physical_Registers[rs1]>Physical_Registers[rs2]):
                    Program_Counter.updatePC(int(renamed_instruction[3]))
                return 1


            elif(renamed_instruction[0]=="JAL"):
                Program_Counter.updatePC(int(renamed_instruction[2]))
                return 1
                # Register_Bank[decoded_instruction[1]] = PC.currentPC()

            elif(renamed_instruction[0]=="JALR"):
                rs2 = renamed_instruction[2]
                t2 = int(rs2.replace('F',''))
                Physical_Registers[rs2] = Register_Bank[Physical_Registers_Map[t2]]
                Program_Counter.updatePC(Physical_Registers[renamed_instruction[2]]+int(renamed_instruction[3]))
                return 1
                # Register_Bank[decoded_instruction[1]] = PC.currentPC()
    else:
        return 0


def CheckVars(renamed_instruction):
    for i in range(0,32):
        if(Reorder_Buffer["ROB"+str(i)][1]==renamed_instruction[1]):
            return 0
        if(Reorder_Buffer["ROB"+str(i)][1]==renamed_instruction[2]):
            return 0
    return 1
