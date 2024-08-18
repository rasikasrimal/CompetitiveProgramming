def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_max_gcd_pair(arr):
    n = len(arr)
    max_gcd = -1

    for i in range(n):
        for j in range(i + 1, n):
            current_gcd = gcd(arr[i], arr[j])
            if current_gcd > max_gcd:
                max_gcd = current_gcd

    return max_gcd

n = int(input())
arr = list(map(int, input().split()))

result = find_max_gcd_pair(arr)
print(result)
