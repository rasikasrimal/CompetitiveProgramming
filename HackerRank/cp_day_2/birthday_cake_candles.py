def birthdayCakeCandles(candles):
    max_height = max(candles)
    count = candles.count(max_height)
    return count

n = int(input(""))
m = input("").split()

candles = [int(height) for height in m]

result = birthdayCakeCandles(candles)
print(result)