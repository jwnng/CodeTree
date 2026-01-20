n = int(input())

for i in range(n):
    cnt = 0
    for j in range(n):
        print(n-cnt,end=" ")
        cnt += 1
    print()