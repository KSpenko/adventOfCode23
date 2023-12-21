import numpy as np

path = "test_day5.txt"
# path = "input_day5.txt"

with open(path, 'r') as f:
    lines = f.readlines()
    nl = len(lines)

    seeds = list(np.array(lines[0].split(":")[1].split(), dtype=int))
    transseeds = []

    rowID = 2
    for i in range(7): # 7 mappings
        rowID += 1
        while rowID < nl and lines[rowID] != "\n":
            map = list(np.array(lines[rowID].split(), dtype=int))
            seedsCopy = seeds.copy()
            for s in seedsCopy: 
                if s >= map[1] and s < map[1]+map[2]: 
                    transseeds.append( map[0] + (s - map[1]) )
                    seeds.remove(s)
            rowID += 1
        seeds += transseeds
        transseeds = []
        rowID += 1
    print(seeds)
    print(np.amin(seeds))   
        
