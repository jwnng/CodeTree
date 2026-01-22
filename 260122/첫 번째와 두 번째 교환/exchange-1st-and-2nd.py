s = input()
n = list(s)
p1 = n[0]
p2 = n[1]
for i in range(len(n)):
    if n[i] == p1:
        n[i] = p2
    elif n[i] == p2: 
        n[i] = p1

print("".join(n))