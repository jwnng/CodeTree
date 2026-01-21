arr = list(map(int,input().split()))
a = []
sum = 0
for x in arr:
    if x >= 250:
        break
    a.append(x)
for x in a:
    sum += x
    
print(sum,f"{sum/len(a):.1f}")

     