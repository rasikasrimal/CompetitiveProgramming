user_input = input("").split(" ")
n = int(user_input[0])
x = int(user_input[1])

gondolas = 0

weight = input("").split(" ")
weight = [int(w) for w in weight]
weight.sort()

i = 0
j = n - 1

while i <= j:
    if weight[i] + weight[j] <= x:
        gondolas += 1
        i += 1
        j -= 1
    else:
        j -= 1

print(gondolas)
