arr = list(map(int,input().split()))
a = []
for x in arr:
    if x == 0:
        break
    else :
        a.append(x)

print(sum(a),f"{sum(a)/len(a):.1f}")