Keys = []

Name = "F"

Vals = ["No" for i in range(0,128)]

for i in range(0,128):
    Keys.append(Name+str(i))

Physical_Registers = dict.fromkeys(Keys)

# Physical_Registers_Map = dict.fromkeys(range(0,128))
Physical_Registers_Map = dict(zip(range(0,128),Vals))
