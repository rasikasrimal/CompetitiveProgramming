def minimumCoins(n, coins):
    dp = [n + 1] * (n + 1)  # Initialize with a large value
    dp[0] = 0

    for i in range(1, n + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] != n + 1:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[n] if dp[n] != n + 1 else -1

if __name__ == "__main__":
    n, totalSum = map(int, input().split())
    coins = list(map(int, input().split()))

    result = minimumCoins(totalSum, coins)
    print(result)
