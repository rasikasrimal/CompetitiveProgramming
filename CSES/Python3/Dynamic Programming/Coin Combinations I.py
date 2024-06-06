def read_input():
    n, x = map(int, input().split())
    coin_values = list(map(int, input().split()))
    
    return n, x, coin_values

n, x, coin_values = read_input()
print(f"Number of coins: {n}")
print(f"Desired sum of money: {x}")
print(f"Coin values: {coin_values}")
