n = int(input())
m = [ [ i for i in range(1,n+1) ] for j in range(n)]

for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            print(m[i][j],end="")
        else :

            print(m[i][n-(j+1)],end="")
    print()