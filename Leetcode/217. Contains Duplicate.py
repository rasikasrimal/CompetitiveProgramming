n = input("")
n = n.split()

for i in range(0,len(n)):
    for j in range(i+1,len(n)):
        if n[i] == n[j]:
            print("True")
            break
    else:
        continue
    break
else:
    print("False")

