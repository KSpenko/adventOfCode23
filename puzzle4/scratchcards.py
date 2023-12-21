import numpy as np

path = "test_day4.txt"
# path = "input_day4.txt"

with open(path, "r") as f:
    lines = f.readlines()

    sum = 0
    for line in lines:
        winNumbers, scratchNumbers = line.split(":")[1].split("|")
        winNumbers = np.array(winNumbers.split(), dtype=int)
        scratchNumbers = np.array(scratchNumbers.split(), dtype=int)

        nCoincidence = 0
        for s in scratchNumbers:
            if s in winNumbers:
                nCoincidence += 1
        if nCoincidence > 0: sum += 2**(nCoincidence-1)
    print(sum)