def sum_even_fibonacci(limit):
    a, b = 1, 1
    even_sum = 0

    while a <= limit:
        if a % 2 == 0:
            even_sum += a
        a, b = b, a + b

    return even_sum

n = 4000000
result = sum_even_fibonacci(n)
print(result)
