n = int(input())

cnt = 1
for i in range(n):
    for j in range(n):
        if i % 2 == 0:
            cnt = n*i+j+1
        else :
            cnt = (i+1)*n-j
        print(cnt,end=" ")
    print()