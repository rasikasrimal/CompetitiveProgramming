n = int(input())

even_numbers = []
odd_numbers = []

for i in range(1, n + 1):
    if i % 2 == 0:
        even_numbers.append(i)
    else:
        odd_numbers.append(i)

rearranged = []

for even in even_numbers:
    rearranged.append(even)

for odd in odd_numbers:
    rearranged.append(odd)

if abs(len(even_numbers) - len(odd_numbers)) > 1 or 1 < n <= 3:
    print("NO SOLUTION")
else:
    result = ' '.join(map(str, rearranged))
    print(result)
