import numpy as np

path = "test_day5.txt"
# path = "input_day5.txt"

with open(path, 'r') as f:
    lines = f.readlines()
    nl = len(lines)

    seeds = list(np.array(lines[0].split(":")[1].split(), dtype=int))
    seedSets = [[seeds[2*j], seeds[2*j+1]] for j in range(len(seeds)//2)]
    transSets = []

    rowID = 2
    for i in range(7): # 7 mappings
        rowID += 1
        while rowID < nl and lines[rowID] != "\n":
            map = list(np.array(lines[rowID].split(), dtype=int))
            seedSetsCopy = seedSets.copy()
            remIndex = []
            for iss in range(len(seedSetsCopy)):
                ss = seedSetsCopy[iss]
                if ss[0] <= map[1]+map[2] and ss[0]+ss[1] >= map[1]:
                    overlapSet = [max(ss[0], map[1]), min(ss[0]+ss[1], map[1]+map[2]) - max(ss[0], map[1])]
                    transSets.append( [map[0] + overlapSet[0] - map[1], overlapSet[1]] )
                    if overlapSet[0] > ss[0]: seedSets.append([ss[0], overlapSet[0] - ss[0]])
                    if overlapSet[0]+overlapSet[1] < ss[0]+ss[1]: seedSets.append([overlapSet[0]+overlapSet[1], ss[0]+ss[1] - overlapSet[0]-overlapSet[1]])
                    remIndex.append(iss)
            remIndex.sort(reverse=True)
            for ri in remIndex:
                del seedSets[ri]
            rowID += 1
        seedSets += transSets
        transSets = []
        rowID += 1
    print(seedSets)
    seedSets = np.array(seedSets)
    print(np.amin(seedSets[:,0]))   
        
