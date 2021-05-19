def hash(astring,tablesize):
    sum = 0
    for i in range(len(astring)):
        sum+=(ord(astring[i])*(i+1) )
    return sum%tablesize