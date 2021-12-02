import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/input.txt', 'r')
input = file.readlines()
input = [int(i) for i in input]
changes = []
totalBigger = 0

for i, line in enumerate(input):   
    line = int(line)
    change = 0

    if input[i-1] > line:
        change = -1
    elif input[i-1] < line:
        change = 1
    changes.append(change)

for change in changes:
    if change > 0:
        totalBigger += 1

print(totalBigger)
