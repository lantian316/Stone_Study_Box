def print99_normol():
    for l in range(1,10):
        str1=""
        for k in range(1,l+1):
            str1 = str1 + str(l) + "*" + str(k) + "=" + str(l*k) + "\t"
        print(str1)

    
def print99_porful():
    print ('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))
    
    
    
print99_normol()
print("\n")
print99_porful()