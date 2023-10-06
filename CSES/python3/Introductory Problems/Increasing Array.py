import sys

n = int(sys.stdin.readline().strip())
count = 0
numbers = list(map(int, sys.stdin.readline().split()))
for i in range(1, n):
    if numbers[i - 1] > numbers[i]:
        count = count + numbers[i - 1] - numbers[i]
        numbers[i - 1], numbers[i] = numbers[i], numbers[i - 1]
print(count)
