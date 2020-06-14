from initialization import *

def RegisterRenaming(ins):
    type1 = ["ADD","SUB","MUL","DIV","XOR","OR","AND"]
    type2 = ["LD","ADDI","SUBI","MULI","DIVI","JALR"]
    type3 = ["SD","BNE","BEQ","BLT","BGT"]
    type4 = ["JAL"]
    ret_ins = ""

    temp_ins = ins
    temp_ins_type = temp_ins[0]
    ret_ins = ret_ins+temp_ins_type
    if(temp_ins_type in type1):

        if(temp_ins[2] in Physical_Registers_Map.values()):
            ret2= " F" + str(get_latest_key(temp_ins[2],Physical_Registers_Map))
        else:
            empty_key = get_empty_key("No",Physical_Registers_Map)
            Physical_Registers_Map[empty_key] = temp_ins[2]
            ret2 = " F" + str(empty_key)

        if(temp_ins[3] in Physical_Registers_Map.values()):
            ret3 =  " F" + str(get_latest_key(temp_ins[3],Physical_Registers_Map))
        else:
            empty_key = get_empty_key("No",Physical_Registers_Map)
            Physical_Registers_Map[empty_key] = temp_ins[3]
            ret3 =  " F" + str(empty_key)
        empty_key = get_empty_key("No",Physical_Registers_Map)
        Physical_Registers_Map[empty_key] = temp_ins[1]
        ret_ins = ret_ins + " F" + str(empty_key)+ret2+ret3

    elif(temp_ins_type in type2):

        if(temp_ins[2] in Physical_Registers_Map.values()):
            ret2 =  " F" + str(get_latest_key(temp_ins[2],Physical_Registers_Map))
        else:
            empty_key = get_empty_key("No",Physical_Registers_Map)
            Physical_Registers_Map[empty_key] = temp_ins[2]
            ret2 =  " F" + str(empty_key)

        empty_key = get_empty_key("No",Physical_Registers_Map)
        Physical_Registers_Map[empty_key] = temp_ins[1]
        ret_ins = ret_ins + " F" + str(empty_key)+ret2


        ret_ins = ret_ins+" "+temp_ins[3]


    elif(temp_ins_type in type3):
            if(temp_ins[1] in Physical_Registers_Map.values()):
                ret_ins = ret_ins + " F" + str(get_latest_key(temp_ins[1],Physical_Registers_Map))
            else:
                empty_key = get_empty_key("No",Physical_Registers_Map)
                Physical_Registers_Map[empty_key] = temp_ins[1]
                ret_ins = ret_ins + " F" + str(empty_key)

            if(temp_ins[2] in Physical_Registers_Map.values()):
                ret_ins = ret_ins + " F" + str(get_latest_key(temp_ins[2],Physical_Registers_Map))
            else:
                empty_key = get_empty_key("No",Physical_Registers_Map)
                Physical_Registers_Map[empty_key] = temp_ins[2]
                ret_ins = ret_ins + " F" + str(empty_key)
            ret_ins = ret_ins + " " + temp_ins[3]

    elif(temp_ins_type in type4):
        empty_key = get_empty_key("No",Physical_Registers_Map)
        Physical_Registers_Map[empty_key] = temp_ins[1]
        ret_ins = ret_ins + " F" + str(empty_key) + " " + temp_ins[2]
    # print(ret_ins)
    return ret_ins

def get_latest_key(val,diction):
    key = 0
    for i in range(0,128):
        if(diction[i]==val):
             key = i
    return key

def get_empty_key(val,diction):
    for i in range(0,128):
        if(diction[i]==val):
            break
    return i
