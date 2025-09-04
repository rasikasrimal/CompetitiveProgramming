def generate_primes(n):
    primes = []
    num = 2
    while len(primes) < n:
        is_prime = True
        for p in primes:
            if p * p > num:
                break
            if num % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
        num += 1
    return primes

def largest_prime_factor(n):
    primes = generate_primes(int(n ** 0.5))
    for p in reversed(primes):
        if n % p == 0:
            return p
    return n

print(largest_prime_factor(600851475143))