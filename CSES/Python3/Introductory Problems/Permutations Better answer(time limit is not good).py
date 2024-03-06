import random
from itertools import permutations

def is_beautiful(arr):
    for i in range(1, len(arr)):
        if abs(arr[i] - arr[i - 1]) == 1:
            return False
    return True

n = int(input())
numbers = list(range(1, n + 1))

beautiful_permutations = []

for perm in permutations(numbers):
    if is_beautiful(perm):
        beautiful_permutations.append(perm)

if len(beautiful_permutations) == 0:
    print("NO SOLUTION")
else:
    random_permutation = random.choice(beautiful_permutations)
    print(" ".join(map(str, random_permutation)))
