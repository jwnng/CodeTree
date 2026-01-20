n = int(input())
m = [[0 for i in range(n)]for j in range(n)]
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            m[j][i] = j+1
        else :
            m[j][i] = n-j


for i in range(n):
    for j in range(n):
        print(m[i][j],end="")
    print()
