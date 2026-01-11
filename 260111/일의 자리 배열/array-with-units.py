a,b = map(int,input().split())
arr = [a,b]

for x in range(8) :
    next = arr[x] + arr[x+1]
    arr.append(next)

arr2 = [ i%10 for i in arr]
for i in range(len(arr2)):
    print(arr2[i],end=' ')