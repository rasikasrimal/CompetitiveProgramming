n = int(input(''))
 
my_set = []
for i in range(1, n + 1):
    my_set.append(i)
 
total = sum(my_set)
 
if total % 2 == 1:
    print('NO')
    exit()
else:
    target_sum = total // 2
    dp = [False] * (target_sum + 1)
    dp[0] = True
 
    for num in my_set:
        for j in range(target_sum, num - 1, -1):
            dp[j] |= dp[j - num]
 
    if not dp[target_sum]:
        print('NO')
        exit()
 
    print('YES')
    set_1 = []
    i = target_sum
    for num in reversed(my_set):
        if i >= num and dp[i - num]:
            set_1.append(num)
            i -= num
 
    print(len(set_1))
    print(' '.join(map(str, set_1)))
 
    set_2 = [x for x in my_set if x not in set_1]
    print(len(set_2))
    print(' '.join(map(str, set_2)))