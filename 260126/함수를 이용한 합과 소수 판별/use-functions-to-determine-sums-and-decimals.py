a, b = map(int, input().split())

# Please write your code here.
def is_Prime(n):
    cnt = 0
    for i in range(1,n+1):
        if n % i == 0:
            cnt += 1
    if cnt == 2:
        return True
            
def is_even(n):
    n10 = n // 10
    n1 = n % 10 
    if (n10 + n1) % 2 == 0:
        return True

cnt = 0
for i in range(a,b+1):
    if is_Prime(i) == True and is_even(i) == True:
        cnt += 1

print(cnt)