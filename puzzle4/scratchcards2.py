import numpy as np

path = "test_day4-2.txt"
# path = "input_day4.txt"

with open(path, "r") as f:
    lines = f.readlines()

    sum = 0
    scratchcards = [1]
    for line in lines:
        multiplier = scratchcards.pop(0)
        sum += multiplier

        winNumbers, scratchNumbers = line.split(":")[1].split("|")
        winNumbers = np.array(winNumbers.split(), dtype=int)
        scratchNumbers = np.array(scratchNumbers.split(), dtype=int)

        nCoincidence = 0
        for s in scratchNumbers:
            if s in winNumbers:
                nCoincidence += 1
        
        for i in range(nCoincidence):
            if len(scratchcards) > i: scratchcards[i] += multiplier
            else: scratchcards.append(multiplier)
        
        if len(scratchcards) > 0: scratchcards[0] += 1
        else: scratchcards.append(1)
    print(sum)