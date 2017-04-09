import uuid

def generateCode():

    f = open("code.txt", "w")
    codeset = set()
    i = 0
    while True:
        code = uuid.uuid()
        if code not in codeset:
            codeset.add(code)
            i += 1
            f.write("%d. %s\n" % (i, code))
        if i >= 200:
            break
    f.close()