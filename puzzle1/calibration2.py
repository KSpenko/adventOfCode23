path = "input_day1.txt"
values = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

with open(path, 'r') as f:
    lines = f.readlines()
    sum = 0
    for i in range(len(lines)):
        numbers = []
        numberWords = dict(zip(['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'], values))
        for ic in range(len(lines[i])):
            if lines[i][ic] in values: numbers.append(lines[i][ic])
            keys = list(numberWords.keys())
            for k in keys:
                nk = len(k)
                if lines[i][ic:ic+nk] == k:
                    numbers.append(numberWords[k])
                    ic+=nk-1
        value = int(numbers[0])*10 + int(numbers[-1])
        sum += value
    print(sum)
