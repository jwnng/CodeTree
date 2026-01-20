n = int(input())

for i in range(n):
    for j in range(n):
        if j % 2 == 0:
            cnt = i+1
        else :
            cnt = n-i
        print(cnt,end="")
    print()