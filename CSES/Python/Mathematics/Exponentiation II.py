n = int(input())
numbers = []
for _ in range(n):

    a, b, c = map(int, input().split())
    numbers.append(pow(a, pow(b, c, 10**9 + 7), 10**9 + 7))

print(*numbers, sep='\n')