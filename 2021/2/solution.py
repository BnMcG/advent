from os import linesep as NEW_LINE
from typing import Tuple

UP = 'up'
DOWN = 'down'
BACK = 'back'
FORWARD = 'forward'

def tokenize_instruction(instruction: str) -> Tuple[str, int]:
    direction, depth = instruction.split(' ')
    return (direction, int(depth))


with open('input.txt', 'r') as input_file:
    input = input_file.read()
    vectors = input.split(NEW_LINE)
    vectors = [tokenize_instruction(x) for x in vectors]

# Part 1
# What do you get if you multiply your final horizontal position by your final depth?
x = sum([magnitude if direction == FORWARD else magnitude*-1 for (direction, magnitude) in filter(lambda v: v[0] == FORWARD or v[0] == BACK, vectors)])
y = sum([magnitude if direction == DOWN else magnitude*-1 for (direction, magnitude) in filter(lambda v: v[0] == DOWN or v[0] == UP, vectors)])

print(f'Part 1: {x*y}')

# Part 2
# What do you get if you multiply your final horizontal position by your final depth?
x = 0
y = 0
z = 0

for (direction, magnitude) in vectors:
    # Aim vector
    if direction == UP or direction == DOWN:
        z += magnitude if direction == DOWN else magnitude*-1
    # Travel vector
    if direction == FORWARD or direction == BACK:
        x += magnitude if direction == FORWARD else magnitude*-1
        y += magnitude * z

print(f'Part 2: {x*y}')
