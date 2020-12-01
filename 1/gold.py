from itertools import combinations
import math

numbers = [int(line.strip()) for line in open('input.txt')]
print(math.prod(next(filter(lambda x: sum(x)==2020, list(combinations(numbers, 2))))))
