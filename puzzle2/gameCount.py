# path = "test_day2.txt"
path = "input_day2.txt"

colors = ['red', 'green', 'blue']

def extractTurn(cubeInfo):
    extDict = dict(zip(colors, [0, 0, 0]))
    for i in range(len(cubeInfo)//2):
        value, color = cubeInfo[2*i:2*i+2]
        if color[-1] == ',': color = color[:-1]
        if extDict[color] < int(value): extDict[color] = int(value)
    return extDict

def updateDict(oldDict, newDict):
    for key in oldDict.keys():
        if oldDict[key] < newDict[key]: oldDict[key] = newDict[key]
    return oldDict

def updateGame(gameInfo):
    extDict = dict(zip(colors, [0, 0, 0]))
    for g in gameInfo.split(';'):
        extDict = updateDict(extDict, extractTurn(g.split()))
    return extDict

def calcSetPower(extDict):
    pow = 1
    for key in extDict.keys():
        pow *= extDict[key]
    return pow

with open(path, 'r') as f:
    lines = f.readlines()
    sum = 0
    for i in range(len(lines)):
        gameInfo = lines[i].split(':')
        gSuccess = True
        extDict = updateGame(gameInfo[1])
        setPower = calcSetPower(extDict)
        sum += setPower
    print(sum)