n = int(input())

for k in range(1, n + 1):
    count_attack = 0
    count_safe = 0
    for x in range(1, k + 1):
        for y in range(1, k + 1):
            for p in range(1, k + 1):
                for q in range(1, k + 1):
                    if x != p and y != q:
                        if abs(x - p) == 2 and abs(y - q) == 1 or abs(x - p) == 1 and abs(y - q) == 2:
                            count_attack += 1
                        else:
                            count_safe += 1
    print(count_attack)
