def min_time_to_open_cage(l, p, q, s):
    last_index = {}
    time = 0

    for i in range(l - 1, -1, -1):
        char = s[i]

        if char in last_index:
            duplicate_time = (last_index[char] - i) * q
            time += duplicate_time

            last_index[char] = i
        else:
            time += p

            last_index[char] = i

    return time

T = int(input())
results = []

for _ in range(T):
    L, P, Q = map(int, input().split())
    S = input().strip()
    time = min_time_to_open_cage(L, P, Q, S)
    results.append(time)

for result in results:
    print(result)
