def count_ways_to_construct_sum(n):
    MOD = 10**9 + 7

    # Initialize a list to store the number of ways for each sum from 0 to n
    ways = [0] * (n + 1)

    # There is 1 way to get a sum of 0 (by not throwing the dice)
    ways[0] = 1

    # Calculate the number of ways for each sum from 1 to n
    for i in range(1, n + 1):
        for j in range(1, 7):  # Possible outcomes of throwing a dice (1 to 6)
            if i >= j:
                ways[i] = (ways[i] + ways[i - j]) % MOD

    return ways[n]

# Example usage:
n = int(input())
result = count_ways_to_construct_sum(n)
print(result)
