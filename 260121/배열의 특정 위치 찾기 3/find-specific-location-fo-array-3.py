arr = list(map(int,input().split()))
a = []
for x in arr:
    if x != 0:
        a.append(x)
    else :
        break 

print(sum(a[-3:]))