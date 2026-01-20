n = int(input())

for i in range(1,2*n+1):
    if i % 2 == 1:
        cnt = n-(i+1)//2+1
    else :
        cnt = i // 2
    print("* " * cnt)