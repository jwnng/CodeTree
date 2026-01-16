m1 = []

for _ in range(7):
    row = list(map(int,input().split()))
    m1.append(row)

m2 = []

for i in range(3):
    r = []
    for j in range(3):
        mul = m1[i][j] * m1[i+4][j]
        r.append(mul)
    m2.append(r)

for i in range(3):
    for j in range(3):
        print(m2[i][j],end=" ")
    print()
    