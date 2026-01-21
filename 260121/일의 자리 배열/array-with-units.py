f = list(map(int,input().split()))

for i in range(8):
    f.append((f[i] + f[i+1])%10)

print(*f)