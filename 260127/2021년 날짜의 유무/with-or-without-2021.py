M, D = map(int, input().split())

# Please write your code here.
def day_chech(M,D):
    if M == 1 or M == 3 or M == 5 or M == 7 or M == 8 or M == 10 or M == 12:
        if D <= 31:
            return True
    elif M == 4 or M == 6 or M == 9 or M == 11:
        if D <= 30:
            return True  
    elif M == 2:
        if D <= 28:
            return True
    else:
        return False

if day_chech(M,D) == True:
    print('Yes')    
else:
    print('No')