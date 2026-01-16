n,m = map(int,input().split())
m1 = []
m2 = []
m1 = [list(map(int,input().split())) for _ in range(n)]
m2 = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if m1[i][j] == m2[i][j]:
            print('0',end = " ")
        else :
            print('1',end = " ")
    print()
