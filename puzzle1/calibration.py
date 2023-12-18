path = "input_day1.txt"

with open(path, 'r') as f:
    lines = f.readlines()
    sum = 0
    for i in range(len(lines)):
        numbers = []
        for char in lines[i]:
            if char in ['1', '2', '3', '4', '5', '6', '7', '8', '9']: numbers.append(char)
        value = int(numbers[0])*10 + int(numbers[-1])
        sum += value
    print(sum)
