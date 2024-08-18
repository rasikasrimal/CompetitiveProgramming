string = input("")
string = sorted(string)
n = len(string)
ans = []
def permute(a, l, r):
    if l == r:
        ans.append(''.join(a))
    else:
        for i in range(l, r + 1):
            a[l], a[i] = a[i], a[l]
            permute(a, l + 1, r)
            a[l], a[i] = a[i], a[l]
permute(list(string), 0, n - 1)
ans = sorted(set(ans))
print(len(ans))
for i in ans:
    print(i)
    