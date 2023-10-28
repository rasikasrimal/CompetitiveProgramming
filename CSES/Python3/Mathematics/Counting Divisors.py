n = int(input(""))
numbers = []
divisors = []

for i in range(n):
    num = int(input(""))
    numbers.append(num)

for i in numbers:
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    divisors.append(count)

print(*divisors, sep="\n")