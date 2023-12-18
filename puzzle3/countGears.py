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

def getGearsFromLines(lines, i):
    if i == 0: numAr = getNumbers(lines[0])
    else: numAr = getNumbers(lines[1])

    gears = []
    for j in range(len(numAr)):
        symbols = []
        for l in lines:
            symbols += l[ (numAr[j][1] - (0 if numAr[j][1]==0 else 1)) : (numAr[j][1]+numAr[j][2] + (0 if numAr[j][1]+numAr[j][2]==len(l)-1 else 1)) ]
        
        nl = numAr[j][2]+2 if (numAr[j][1] != 0 and numAr[j][1]+numAr[j][2] != len(l)-1) else numAr[j][2]+1
        for si in range(len(symbols)):
            if symbols[si] == '*': gears.append([ ( si//nl + (0 if i==0 else i-1), si%nl + (numAr[j][1]-1 if numAr[j][1] > 0 else 0) ), numAr[j][0]])
    return gears

def checkGearCandidate(gear, gearCandidates):
    count, ratio = 0, 1
    gear2s = []
    for gear2 in gearCandidates:
        if gear[0] == gear2[0]:
            count += 1
            ratio *= gear2[1]
            gear2s.append(gear2)
        if count > 2: break
    return count, gear2s, ratio

with open(path, "r") as f:
    lines = f.readlines()
    nl = len(lines)

    gearCandidates = []
    for i in range(nl):
        gearCandidates += getGearsFromLines(lines[(i if i==0 else i-1) : (i+1 if i==nl-1 else i+2)], i)

    sum = 0
    gcForPop = gearCandidates.copy()
    while len(gcForPop) > 0:
        gear = gcForPop.pop()
        count, gear2s, ratio = checkGearCandidate(gear, gearCandidates)
        if count == 2:
            for g2 in gear2s:
                gearCandidates.remove(g2)
            sum += ratio
    print(sum)