n = int(input())
arr = list(map(int,input().split()))
m = [ x*x for x in arr]

print(*m[:])