n = int(input())

for i in range(1,n+1):
    cnt = 0
    for j in range(1,n+1):
        print(9+2*i+cnt,end=" ")
        cnt += 2
    
    print()