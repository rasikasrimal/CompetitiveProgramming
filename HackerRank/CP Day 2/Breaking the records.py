def records(n, score):
    min = score[0]
    max = score[0]
    min_count = 0
    max_count = 0
    
    for i in range(n):
        if score[i] < min:
            min_count += 1
            min = score[i]
        elif score[i] > max:
            max_count += 1
            max = score[i]
        else:
            pass
    return f"{max_count} {min_count}"

n = int(input(""))
m = input("").split()
score = [int(value) for value in m]

result = records(n, score)
print(result)