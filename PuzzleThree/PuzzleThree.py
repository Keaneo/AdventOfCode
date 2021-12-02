import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
file = open(dir_path + '/input.txt', 'r')

input = file.readlines()

depth = 0
horizontal = 0

for i, instruction in enumerate(input):

    instruction = instruction.split(' ')   

    if instruction[0] == 'forward':
        horizontal += int(instruction[1])
    elif instruction[0] == 'up':
        depth -= int(instruction[1])
    elif instruction[0] == 'down':
        depth += int(instruction[1])

print(horizontal * depth)