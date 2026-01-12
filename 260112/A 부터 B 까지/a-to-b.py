a,b = map(int,input().split())
n = a
while n < b :
    if n % 2 == 1 :
        print(n,end=' ')
        n *= 2
    else :
        print(n,end=' ')
        n += 3
    
    if n == b :
        print(n)
        break
    