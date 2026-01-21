n = int(input())
arr = list(map(int,input().split()))
nm = []
for x in arr:
    if x % 2 == 0:
      nm.append(x)

print(*nm)  