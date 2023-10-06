# import sys

# n = int(sys.stdin.readline().strip())

# for k in range(1, n + 1):
#     count_attack = 0
#     count_safe = 0
#     for x in range(1, k + 1):
#         for y in range(1, k + 1):
#             for p in range(1, k + 1):
#                 for q in range(1, k + 1):
#                     if x != p and y != q:
#                         if abs(x - p) == 2 and abs(y - q) == 1 or abs(x - p) == 1 and abs(y - q) == 2:
#                             count_attack += 1
#                         else:
#                             count_safe += 1
#     print(count_safe)

import sys
import math

class Combination:
    def __init__(self, k):
        self.k = k

    def calculate_combination(self):
        numerator = math.factorial(self.k**2)
        denominator1 = math.factorial(self.k**2 - 2)
        denominator2 = math.factorial(2)
        result = numerator / (denominator1 * denominator2)
        return result

n = int(sys.stdin.readline().strip())

for k in range(1, n + 1):
    combinations = Combination(k)
    total_positions = combinations.calculate_combination()
    print(total_positions)
