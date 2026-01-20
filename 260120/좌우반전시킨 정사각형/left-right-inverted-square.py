n = int(input())
m = [ [0 for i in range(n)] for j in range(n)]

for i in range(n):
    for j in range(n):
        m[i][j] = (i+1)*(j+1)

for i in range(n):
    for j in range(n):
        print(m[i][n-j-1],end=" ")
    print()
        