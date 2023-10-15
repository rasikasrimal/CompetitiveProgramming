import math

n = math.factorial(int(input()))
n = str(n)

result = 0

for i in range(len(n) - 1, -1, -1):
    if (n[i] == '0'):
        result += 1
    else:
        break

print(result)