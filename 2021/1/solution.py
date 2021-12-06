from os import linesep as NEW_LINE
from typing import List


def count_measurement_increases(m: List[int]) -> int:
    number_of_measurements = len(m)
    return sum([1 if m[i] > m[i-1] else 0 for i in range(1, number_of_measurements)])


with open('input.txt', 'r') as input_file:
    input = input_file.read()
    measurements = input.split(NEW_LINE)
    measurements = [int(m) for m in measurements]

# Part 1
# count the number of times a depth measurement increases from the previous measurement.
print(f'Part 1: {count_measurement_increases(measurements)}')

# Part 2
# count the number of times the sum of measurements in this sliding window increases
windows = [measurements[i] + measurements[i+1] + measurements[i+2] for i in range(len(measurements) - 2)]
print(f'Part 2: {count_measurement_increases(windows)}')
