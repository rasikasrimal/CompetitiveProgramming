def multiples_of_3_or_5(n):
    sum_of_3 = sum(range(3, n, 3))
    sum_of_5 = sum(range(5, n, 5))
    sum_of_15 = sum(range(15, n, 15))
    return sum_of_3 + sum_of_5 - sum_of_15

print(multiples_of_3_or_5(1000))