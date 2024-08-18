def toh(n, source, auxiliary, target):
    if n == 1:
        return 1, [[source, target]]
    else:
        count1, moves1 = toh(n - 1, source, target, auxiliary)
        count2, moves2 = toh(n - 1, auxiliary, source, target)
        moves = moves1 + [[source, target]] + moves2
        return count1 + 1 + count2, moves

n = int(input())
count, moves = toh(n, 1, 2, 3)
print(count)
for move in moves:
    print(move[0], move[1])
