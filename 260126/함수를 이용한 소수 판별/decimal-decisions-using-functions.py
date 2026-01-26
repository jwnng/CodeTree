a, b = map(int, input().split())

# Please write your code here.

def isPrime(n):
    cnt = 0
    for i in range(1,n+1):
        if  n % i == 0:
            cnt += 1
    if cnt == 2:
        return True
            
    
sum = 0
for n in range(a,b+1):
    if isPrime(n) == True:
        sum += n

print(sum)