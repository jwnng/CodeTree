n, m = map(int, input().split())

# Please write your code here.
def min_mul(n,m):
    mul = []

    for i in range(1,n+1):
        for j in range(1,m+1):
            if n * i == m * j:
                    mul.append(n * i)
                    break
                
    print(mul[0])

min_mul(n,m)