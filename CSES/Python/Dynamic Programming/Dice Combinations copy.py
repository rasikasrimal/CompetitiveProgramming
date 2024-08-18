def count_ways_to_construct_sum(n):
    MOD = 10**9 + 7

    ways = [0] * (n + 1)

    ways[0] = 1

    for i in range(1, n + 1):
        for j in range(1, 7): 
            if i >= j:
                ways[i] = (ways[i] + ways[i - j]) % MOD

    return ways[n]

n = int(input())
result = count_ways_to_construct_sum(n)
print(result)
