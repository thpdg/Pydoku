good_vals = []

index = 0
for parm in filter(lambda num: len(set(str(num))) == len(str(num)) and '0' not in str(num), range(123456789,999999999)):
    print(index,end="")
    print(": ", end="")
    print(parm)
    index+=1

