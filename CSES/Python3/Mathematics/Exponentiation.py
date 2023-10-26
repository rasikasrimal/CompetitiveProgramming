n = int(input())
numbers = []
for _ in range(n):

    a, b = map(int, input().split())
    numbers.append(pow(a, b, 10**9 + 7))

print(*numbers, sep='\n')