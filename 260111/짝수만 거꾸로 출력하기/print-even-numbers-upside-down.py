n = int(input())
arr = list(map(int,input().split()))
for i in range(n,0,-1):
    if arr[n-i] % 2 == 0 :
        print(arr[n-i],end=' ')
    else :
        pass
        