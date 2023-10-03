n = int(input(''))

my_set = []
for i in range(1, n + 1):
    my_set.append(i)

total = sum(my_set)

def final_subset_with_sum(numbers, total):
    def subset_sum_recursive(numbers, total, index, current_subset):
        if total == 0:
            result.append(current_subset[:])
            return
        if index == len(numbers):
            return
        if total < 0:
            return
        current_subset.append(numbers[index])
        subset_sum_recursive(numbers, total - numbers[index], index + 1, current_subset)
        current_subset.pop()
        subset_sum_recursive(numbers, total, index + 1, current_subset)

    result = []
    subset_sum_recursive(numbers, total, 0, [])
    return result

if total % 2 == 1:
    print('NO')
    exit()
else:
    print('YES')
    set_1 = final_subset_with_sum(my_set, total // 2)
    print(len(set_1[0]))
    print(' '.join(map(str, set_1[0])))

    set_2 = [x for x in my_set if x not in set_1[0]]
    print(len(set_2))
    print(' '.join(map(str, set_2)))
