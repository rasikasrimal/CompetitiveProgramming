alice = input("").split()
alice = [int(x) for x in alice]

bob = input("").split()
bob = [int(x) for x in bob]

a_score = 0
b_score = 0

for i in range(3):
    if alice[i] > bob[i]:
        a_score += 1
    elif bob[i] > alice[i]:
        b_score += 1

print(f"{a_score} {b_score}")
    

