arr = list(map(int,input().split()))
a = []
for x in arr:
    if x % 3 == 0:
        break
    else: 
        a.append(x)

print(a[-1])