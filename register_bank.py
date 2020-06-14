Keys = []
Values = [0] * 32

Name = "R"

for i in range(0,32):
    Keys.append(Name+str(i))

Register_Bank = dict(zip(Keys,Values))
