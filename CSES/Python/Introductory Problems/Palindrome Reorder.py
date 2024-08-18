from collections import Counter

s = input()
freq = Counter(s)
odd_count = sum(1 for f in freq.values() if f % 2 == 1)

if odd_count > 1:
    print("NO SOLUTION")
else:
    palindrome = []

    for c, f in freq.items():
        if f % 2 == 0:
            palindrome.extend([c] * (f // 2))

    if odd_count == 1:
        odd_char = next(c for c, f in freq.items() if f % 2 == 1)
        count_middle = freq[odd_char]
        middle = [odd_char] * count_middle
    else:
        middle = []

    print("".join(palindrome + middle + list(reversed(palindrome))))
