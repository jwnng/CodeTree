n = 4
m = []
for _ in range(4):
    row = list(map(int,input().split()))
    m.append(row)

for i in range(4):
    total = 0
    for j in range(4):
        total += m[i][j]
    print(total)
