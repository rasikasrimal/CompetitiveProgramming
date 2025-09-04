# A palindromic number reads the same both ways. The largest palindrome made from the product of two 
# 2-digit numbers is 9009 = 91 * 99

# Find the largest palindrome made from the product of two 
# 3-digit numbers.


def is_palindrome(n):
    return str(n) == str(n)[::-1]

a = 999
largest_palindrome = 0

while a > 100:
    b = 999
    while b > 100:
        n = a * b
        if is_palindrome(n):
            largest_palindrome = max(largest_palindrome, n)
            break
        b -= 1
    a -= 1

print(largest_palindrome)


