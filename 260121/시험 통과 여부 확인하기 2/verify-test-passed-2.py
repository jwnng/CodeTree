n = int(input())
cnt = 0
arr = [None] * n
for i in range(n):
    arr[i] = list(map(int,input().split()))


for i in range(n):
    if sum(arr[i])/4 >= 60.0:
        print('pass') 
        cnt += 1
    else :
        print('fail') 
        
print(cnt)