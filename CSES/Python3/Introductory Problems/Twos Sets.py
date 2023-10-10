n = int(input(''))
 
my_set = []
for i in range(1, n + 1):
    my_set.append(i)
 
total = sum(my_set)
 
def final_subset_with_sum(numbers, total):
    results = [[] for _ in range(total + 1)]
    results[0] = [[]]
 
    for num in numbers:
        for i in range(total, num - 1, -1):
            for prev_subset in results[i - num]:
                results[i].append(prev_subset + [num])
 
    return results[total]
 
if total % 2 == 1:
    print('NO')
    exit()
else:
    print('YES')
    set_1 = final_subset_with_sum(my_set, total // 2)[0]
    print(len(set_1))
    print(' '.join(map(str, set_1)))
 
    set_2 = [x for x in my_set if x not in set_1]
    print(len(set_2))
    print(' '.join(map(str, set_2)))