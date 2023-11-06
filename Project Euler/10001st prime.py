prime_numbers = []

i = 2  # Start with the first prime number, which is 2

while len(prime_numbers) < 10001:
    is_prime = True
    for prime in prime_numbers:
        if i % prime == 0:
            is_prime = False
            break
    if is_prime:
        prime_numbers.append(i)
    i += 1

print(prime_numbers[-1])
