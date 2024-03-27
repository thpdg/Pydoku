import time
good_vals = []
board_vals = []

# MAybe do %10 instead?
def isValid_mods(int1,existing_int, debug=False):
    isValid_start_time = time.time()
    while int1 > 0:
        v1 = int(int1%10)
        v2 = int(existing_int%10)
        if v2 != 0:
            if v1 != v2:
                if debug:
                    print(" " + str(int1) + " not compatible with existing values " + str(existing_int))
                print("  --- %s seconds F ---" % (time.time() - isValid_start_time))
                return False
            
        int1 = int(int1/10)
        existing_int = int(existing_int/10)
    if debug:
        print(" " + str(int1) + " compatible with existing values " + str(existing_int))
    print("  --- %s seconds T ---" % (time.time() - isValid_start_time))
    return True

def isValid_strings(int1, existing_int, debug=False):
    # Convert integers to strings
    str1 = str(int1)
    existing = str(existing_int)

    str1 = str1.zfill(9)
    existing = existing.zfill(9)

    # Check if lengths are equal
    if len(str1) != len(existing):
        print(" Strings " + str1 + " and " + existing + " are different lengths")
        return False

    # Compare corresponding characters
    for i in range(len(str1)):
        if existing[i] != '0' and str1[i] != existing[i]:
            if debug:
                print(" Strings " + str1 + " and " + existing + " aren't compatible")
            return False

    # All non-zero characters are the same
    return True

index = 0
print("Starting...")
start_time = time.time()
for parm in filter(lambda num: len(set(str(num))) == len(str(num)) and '0' not in str(num), range(123456789,999999999)):
    # Continue if not valid with current block and future blocks
    if not isValid_mods(parm,23056780, True):
        continue
    
    print(index,end="")
    print(": ", end="")
    print(parm)
    index+=1

print("--- %s seconds ---" % (time.time() - start_time))