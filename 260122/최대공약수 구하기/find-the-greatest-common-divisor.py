n, m = map(int, input().split())

# Please write your code here.
def max_divisor(n,m):
    a = []
    b = []
    ab = []
    for i in range(1,n+1):
        if n % i == 0:
            a.append(i)
    for i in range(1,m+1):
        if m % i == 0:
            b.append(i)
    
    for i in range(len(a)):
        for j in range(len(b)):
            if a[i] == b[j]:
                ab.append(a[i])
    print(max(ab[:]))

max_divisor(n,m)