n = int(input())
results = []

for i in range(n):
    a, b = map(int, input().split())
    if (a + b) % 3 == 0 and min(a, b) * 2 >= max(a, b):
        results.append("YES")
    else:
        results.append("NO")

for result in results:
    print(result) 
