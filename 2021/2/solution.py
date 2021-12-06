from os import linesep as NEW_LINE
from typing import Tuple
from functools import reduce


def tokenize_instruction(instruction: str) -> Tuple[str, int]:
    direction, depth = instruction.split(' ')
    return (direction, int(depth))


with open('input.txt', 'r') as input_file:
    input = input_file.read()
    vectors = input.split(NEW_LINE)
    vectors = [tokenize_instruction(x) for x in vectors]

# Part 1
# What do you get if you multiply your final horizontal position by your final depth?
x = 0
y = 0

depth_vectors = filter(lambda v: v[0] == 'down' or v[0] == 'up', vectors)
horizontal_vectors = filter(lambda v: v[0] == 'forward' or v[0] == 'back', vectors)

for (direction, magnitude) in depth_vectors:
    y += magnitude if direction == 'down' else magnitude*-1

for (direction, magnitude) in horizontal_vectors:
    x += magnitude if direction == 'forward' else magnitude*-1

print(f'Part 1: {x*y}')

# Part 2
# What do you get if you multiply your final horizontal position by your final depth?
x = 0
y = 0
z = 0

for (direction, magnitude) in vectors:
    # Aim vector
    if direction == 'up' or direction == 'down':
        z += magnitude if direction == 'down' else magnitude*-1
    # Travel vector
    if direction == 'forward' or direction == 'back':
        x += magnitude if direction == 'forward' else magnitude*-1
        y += magnitude * z

print(f'Part 2: {x*y}')
