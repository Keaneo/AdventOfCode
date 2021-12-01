file = open('./input.txt', 'r')
input = file.readlines()
input = [int(i) for i in input]

sums = []

for i, val in enumerate(input[:-2]):
    group = (val, input[i+1], input[i+2])
    sum = group[0] + group[1] + group[2]
    sums.append(sum)

changes = []
totalBigger = 0

for i, sum in enumerate(sums):   
    change = 0

    if sums[i-1] > sum:
        change = -1
    elif sums[i-1] < sum:
        change = 1
    changes.append(change)

for change in changes:
    if change > 0:
        totalBigger += 1

print(totalBigger)
