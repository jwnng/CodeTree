n = int(input())
m = [ [0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
            m[j][i] = j+1

for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            print(m[i][j],end="")
        else :
            print(m[n-(i+1)][j],end="")
    print()
    