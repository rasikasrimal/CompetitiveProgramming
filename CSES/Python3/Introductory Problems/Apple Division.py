n = int(input())
p = list(map(int, input().split()))

def apple_division(n, p):
    total_sum = sum(p)
    min_diff = float('inf')
    for i in range(1, 1 << n):
        curr_sum = 0
        for j in range(n):
            if i & (1 << j):
                curr_sum += p[j]
        min_diff = min(min_diff, abs(total_sum - 2 * curr_sum))
    return min_diff

result = apple_division(n, p)
print(result)
