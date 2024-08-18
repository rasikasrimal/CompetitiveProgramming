MOD = 10**9 + 7

def count_ways_to_construct_sum(n, x, coin_values):
    dp = [0] * (x + 1)
    dp[0] = 1
    
    for c in coin_values:
        for i in range(c, x + 1):
            dp[i] = (dp[i] + dp[i - c]) % MOD
    
    return dp[x]

# Input parsing
n, x = map(int, input().split())
coin_values = list(map(int, input().split()))

# Function call
result = count_ways_to_construct_sum(n, x, coin_values)

# Output
print(result)
