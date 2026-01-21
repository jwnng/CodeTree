n = int(input())
arr = list(map(int,input().split()))
a = []
for x in arr:
    if x % 2 == 0:
        a.append(x)
    
print(*a[::-1])
