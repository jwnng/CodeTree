n1, n2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

# Please write your code here.
def part_seq(a,b):
    for i in range(n1-n2+1):
        cnt = 0
        for j in range(n2):
            if a[j+i] == b[j]:
                cnt += 1
        
        if cnt == n2:
            return True
                
if part_seq(a,b) == True:
    print('Yes')
else:
    print('No')
