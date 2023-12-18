cubes = {
    'red': 12,
    'green': 13,
    'blue': 14,
}

# path = "test_day2.txt"
path = "input_day2.txt"

def checkTurn(cubeInfo):
    for i in range(len(cubeInfo)//2):
        value = int(cubeInfo[2*i])
        color = cubeInfo[2*i+1]
        if color[-1] == ',': color = color[:-1]
        if cubes[color] < value:
            return False
    return True

def checkGame(gameInfo):
    games = gameInfo.split(';')
    for g in games:
        cubeInfo = g.split()
        if not checkTurn(cubeInfo):
            return False
    return True

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
        for g in games:
            if not checkGame(g):
                gSuccess = False
                break
            
        if gSuccess: sum += id

    print(sum)