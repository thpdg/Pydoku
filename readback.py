myfile = open("gfg.txt", "r")
perms = []
myline = myfile.readline()
while myline:
    myline = myline.rstrip()
    print(myline)
    perms.append(myline)
    myline = myfile.readline()
myfile.close()


for perm in perms:
    print(perm)
    
print(str(perms))
