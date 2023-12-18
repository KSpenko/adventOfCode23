# path = "test_day2.txt"
path = "input_day2.txt"

cubes = { 'red': 12, 'green': 13, 'blue': 14}

def checkTurn(cubeInfo):
    for i in range(len(cubeInfo)//2):
        value, color = cubeInfo[2*i:2*i+2]
        if color[-1] == ',': color = color[:-1]
        if cubes[color] < int(value): return False
    return True

def checkGame(gameInfo):
    games = gameInfo.split(';')
    for g in games: 
        if not checkTurn(g.split()): return False
    return True

with open(path, 'r') as f:
    lines = f.readlines()
    sum = 0
    for i in range(len(lines)):
        gameInfo = lines[i].split(':')
        games = gameInfo[1].split(';')
        id = int(gameInfo[0].split(' ')[1])
        gSuccess = True
        for g in games:
            if not checkGame(g):
                gSuccess = False
                break
        if gSuccess: sum += id
    print(sum)