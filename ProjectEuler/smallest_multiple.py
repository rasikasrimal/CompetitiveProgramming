import math
n = 20
numbers = []
for i in range(1,n+1):
    numbers.append(i)

lcm = numbers[0]
for num in numbers[1:]:
    lcm = (lcm * num) // math.gcd(lcm, num)

print(lcm)
