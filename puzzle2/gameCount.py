colors = ['red', 'green', 'blue']

# path = "test_day2.txt"
path = "input_day2.txt"

def extractTurn(cubeInfo):
    extDict = dict(zip(colors, [0, 0, 0]))
    for i in range(len(cubeInfo)//2):
        print(cubeInfo[2*i], cubeInfo[2*i+1])
        value = int(cubeInfo[2*i])
        color = cubeInfo[2*i+1]
        if color[-1] == ',': color = color[:-1]
        if extDict[color] < value:
            extDict[color] = value
    print(extDict)
    return extDict

def updateDict(oldDict, newDict):
    # print(oldDict, newDict)
    for key in oldDict.keys():
        if oldDict[key] < newDict[key]:
            oldDict[key] = newDict[key]
    # print(oldDict)
    return oldDict

def updateGame(gameInfo):
    extDict = dict(zip(colors, [0, 0, 0]))
    games = gameInfo.split(';')
    for g in games:
        print(g)
        cubeInfo = g.split()
        extDict = updateDict(extDict, extractTurn(cubeInfo))
    print(extDict)
    return extDict

def calcSetPower(extDict):
    pow = 1
    for key in extDict.keys():
        pow *= extDict[key]
    return pow

with open(path, 'r') as f:
    lines = f.readlines()
    # print(lines)

    sum = 0
    for i in range(len(lines)):
        # split lines with spaces
        gameInfo = lines[i].split(':')
        games = gameInfo[1].split(';')
        id = int(gameInfo[0].split(' ')[1])
        # print(id, len(games))

        gSuccess = True
        extDict = updateGame(gameInfo[1])
        setPower = calcSetPower(extDict)
            
        sum += setPower

    print(sum)