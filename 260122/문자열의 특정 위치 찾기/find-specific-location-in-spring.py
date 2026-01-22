s,c = input().split()

n = len(s)
idx = -1

for i in range(n):
    if s[i] == c:
        idx = i
        break

if idx == -1: 
    print('No')
else :
    print(idx)