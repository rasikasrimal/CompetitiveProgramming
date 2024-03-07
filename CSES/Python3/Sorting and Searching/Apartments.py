user_input = input("").split(" ")
n = int(user_input[0])
m = int(user_input[1])
k = int(user_input[2])

count = 0

user_size = list(map(int, input("").split(" ")))
apartment_size = list(map(int, input("").split(" ")))

for i in range(m):
    for j in range(n):
        if apartment_size[i] != -1 and user_size[j] - k <= apartment_size[i] <= user_size[j] + k:
            count += 1
            apartment_size[i] = -1
            break

print(count)
