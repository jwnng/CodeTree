n, m = map(int, input().split())

# Please write your code here.
def swap(n,m):
    tmp = n
    n = m
    m = tmp
    return n,m

n,m = tuple(swap(n,m))
print(n,m)
