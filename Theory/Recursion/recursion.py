def way(n, m):    
    if n == 0:
        return 1
    elif n < 0 or m == 0:
        return 0
    else:
        return way(n, m-1) + way(n-m, m)

print(way(9, 5))
