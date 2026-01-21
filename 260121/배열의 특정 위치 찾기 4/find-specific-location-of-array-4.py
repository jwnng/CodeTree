arr = list(map(int,input().split()))
a = []
cnt = 0
for x in arr:
    if x == 0:
        break
    else:
        if x % 2 == 0:
            cnt += 1
            a.append(x)

print(cnt,sum(a))