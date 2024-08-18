n = int(input(""))
numbers = list(map(int, input("").split(" ")))
distinct = len(list(set(numbers)))
print(distinct)