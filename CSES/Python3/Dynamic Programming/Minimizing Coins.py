def minimumcoins(n, coins):
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    for i in range(1, n + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[n] if dp[n] != float('inf') else -1

input_str = input().split()

n = int(input_str[0])
total_sum = int(input_str[1])

coins = list(map(int, input().split()))

result = minimumcoins(total_sum, coins)
print(result)
