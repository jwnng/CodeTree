arr = list(map(int,input().split()))
a = []
for x in arr:
    if x != 0:
        a.append(x)
    else :
        break

for i in range(len(a)):
    print(a[len(a)-i-1],end=" ")
    