n = int(input())
while n > 1:
    print(n, end=' ')
    if n % 2 == 0:
        n = int(n / 2)
    else:
        n = int(3 * n + 1)
print(n)

# n = int(input())
# sequence = []

# while n > 1:
#     sequence.append(n)
#     if n % 2 == 1:
#         n = 3 * n + 1
#     else:
#         n = n // 2

# sequence.append(1)

# print(*sequence)
