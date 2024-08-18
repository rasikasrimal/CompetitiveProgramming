import math

def count_divisors(num):
    divisors = 1
    for i in range(2, int(math.sqrt(num)) + 1):
        exponent = 0
        while num % i == 0:
            num //= i
            exponent += 1
        divisors *= (exponent + 1)
    if num > 1:
        divisors *= 2
    return divisors

n = int(input())
numbers = []
for _ in range(n):
    num = int(input())
    divisors = count_divisors(num)
    numbers.append(divisors)

print(*numbers, sep="\n")
