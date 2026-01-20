n = int(input())
cnt = 0
for i in range(n):
    if i % 2 == 0:
        for j in range(i//2+1):
            print("*",end=" ")
    else :
        for j in range(n-cnt):
            print("*",end=" ")
        cnt += 1
    print()

for i in range(n):
    if i % 2 == 0:
        for j in range(n//2+1-i//2):
            print("*",end=" ")
    else :
        cnt -= 1
        for j in range(n-cnt):
            print("*",end=" ")
    print()