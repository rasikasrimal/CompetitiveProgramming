n = int(input())
values = list(map(int, input().split()))

unique_sums = set()
unique_sums.add(0)

for val in values:
    new_sums = set()
    for sum_val in unique_sums:
        new_sums.add(sum_val + val)
    unique_sums.update(new_sums)

unique_sums.remove(0)

unique_sums = sorted(unique_sums)
print(len(unique_sums))
print(" ".join(map(str, unique_sums)))
