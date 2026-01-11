n = int(input())
arr = list(map(int,input().split()))

double = [ n**2 for n in arr]

for i in range(len(double)):
    print(double[i],end=' ')