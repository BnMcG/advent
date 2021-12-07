from os import linesep as NEW_LINE
from collections import Counter

with open('input.txt', 'r') as input_file:
    input = input_file.read()
    bytes = input.split(NEW_LINE)
    bytes = [int(b, 2) for b in bytes]


# Part 1
# What is the power consumption of the submarine?
number_of_bits = max([b.bit_length() for b in bytes])

gamma = 0
epsilon = 0

# Iterate from the end to the start as we'll be operating on 
# the most significant bit first and pushing it left every time we iterate
for i in range(number_of_bits - 1, -1, -1):
    bits = list(map(lambda b: 1 if b & (1 << i) != 0 else 0, bytes))
    most_common = Counter(bits).most_common()

    gamma = gamma << 1
    if most_common[0][0] == 1:
        gamma = gamma | (1 << 0)
    
    epsilon = epsilon << 1
    # most_common[-1] is the end of the most_common list and therefore the least common
    if most_common[-1][0] == 1:
        epsilon = epsilon | (1 << 0)

print(f'Part 1: {gamma * epsilon}')


# Part 2
# verify the life support rating
oxygen_generator_candidates = bytes.copy()
co2_scrubber_candidates = bytes.copy()

for i in range(number_of_bits - 1, -1, -1):
    o2_bits = list(map(lambda b: 1 if b & (1 << i) != 0 else 0, oxygen_generator_candidates))
    o2_most_common = Counter(o2_bits).most_common()

    if len(oxygen_generator_candidates) > 1:
        o2_1_most_common = o2_most_common[0][0] == 1
        o2_0_most_common = o2_most_common[0][0] == 0
        o2_as_common = o2_most_common[0][1] == o2_most_common[-1][1]
        oxygen_generator_candidates = list(filter(lambda b: True if ((o2_1_most_common or o2_as_common) and b & (1 << i) != 0) or (o2_0_most_common and not o2_as_common and b & (1 << i) == 0) else False, oxygen_generator_candidates))

    co2_bits = list(map(lambda b: 1 if b & (1 << i) != 0 else 0, co2_scrubber_candidates))
    co2_most_common = Counter(co2_bits).most_common()

    co2_0_least_common = co2_most_common[-1][0] == 0
    co2_1_least_common = co2_most_common[-1][0] == 1
    co2_as_common = co2_most_common[0][1] == co2_most_common[-1][1]
    
    if len(co2_scrubber_candidates) > 1:
        co2_scrubber_candidates = list(filter(lambda b: True if ((co2_0_least_common or co2_as_common) and b & (1 << i) == 0) or (co2_1_least_common and not co2_as_common and b & (1 << i) != 0) else False, co2_scrubber_candidates))

print(f'Part 2: {oxygen_generator_candidates[0] * co2_scrubber_candidates[0]}')