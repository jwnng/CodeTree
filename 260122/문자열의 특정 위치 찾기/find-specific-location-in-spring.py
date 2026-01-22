s,c = input().split()

n = len(s)
idx = -1

for i in range(n-1):
    if s[i] == c:
        idx = i
        break
print(idx)
if idx == -1: 
    print('No')