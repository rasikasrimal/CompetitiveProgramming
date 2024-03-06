DNA = (input())

count = 1
max = 1

for letters in range(len(DNA) - 1):
    if DNA[letters] == DNA[letters + 1]:
        count += 1
        if count > max:
            max = count
    else:
        count = 1

print(max)
