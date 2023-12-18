# path = "test_day3.txt"
path = "input_day3.txt"

def getNumbers(line):
    numAr = []
    ic = 0
    while ic < len(line):
        if line[ic].isdigit():
            numAr.append(["", ic, 0])
            while line[ic].isdigit():
                numAr[-1][0] += line[ic]
                ic += 1
                numAr[-1][2] += 1
            numAr[-1][0] = int(numAr[-1][0])
        ic += 1
    return numAr

def hasSymbol(symbols):
    for s in symbols:
        if s not in ['.','0','1','2','3','4','5','6','7','8','9']:
            return True
    return False

def getPartsFromLines(lines, i):
    numAr = getNumbers(lines[i])
    parts = []
    for j in range(len(numAr)):
        symbols = []
        for l in lines:
            if numAr[j][1] == 0: symbols += l[numAr[j][1]:numAr[j][1]+numAr[j][2]+1]
            elif numAr[j][1]+numAr[j][2] == len(l)-1: symbols += l[numAr[j][1]-1:numAr[j][1]+numAr[j][2]]
            else: symbols += l[numAr[j][1]-1:numAr[j][1]+numAr[j][2]+1]
        if hasSymbol(symbols): parts.append(numAr[j][0])
    return parts

with open(path, "r") as f:
    lines = f.readlines()
    nl = len(lines)

    sum = 0
    for i in range(nl):
        if i == 0:
            partsInLine = getPartsFromLines(lines[i:i+2], 0)
        elif i == nl-1:
            partsInLine = getPartsFromLines(lines[i-1:i+1], 1)
        else:
            partsInLine = getPartsFromLines(lines[i-1:i+2], 1)
        for p in partsInLine:
            sum += p

    print(sum)