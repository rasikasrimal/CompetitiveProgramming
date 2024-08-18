user_input = input("").split(" ")
n = int(user_input[0])
m = int(user_input[1])
k = int(user_input[2])

count = 0

user_size = list(map(int, input("").split(" ")))
apartment_size = list(map(int, input("").split(" ")))

user_size.sort()
apartment_size.sort()

user_index = 0
apartment_index = 0

while user_index < n and apartment_index < m:
    if user_size[user_index] - k <= apartment_size[apartment_index] <= user_size[user_index] + k:
        count += 1
        user_index += 1
        apartment_index += 1
    elif user_size[user_index] - k > apartment_size[apartment_index]:
        apartment_index += 1
    else:
        user_index += 1

print(count)
