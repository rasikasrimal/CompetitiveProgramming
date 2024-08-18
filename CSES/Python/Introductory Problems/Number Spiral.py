t = int(input())
spiral_numbers = []

for _ in range(t):
    y, x = map(int, input().split())
    if y > x:
        if y % 2 == 0:
            spiral = y**2 - x + 1
            # print(spiral)
        else:
            spiral = (y-1)**2 + x
            # print(spiral)
    else:
        if x % 2 == 0:
            spiral = (x-1)**2 + y
            # print(spiral)
        else:
            spiral = x**2 - y + 1
            # print(spiral)
    spiral_numbers.append(spiral)

result = ' '.join(map(str, spiral_numbers))
print(result)