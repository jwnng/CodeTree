Y, M, D = map(int, input().split())

# Please write your code here.
def check_Yoon(Y):
    if Y % 4 == 0 and Y % 100 != 0:
        return True
    elif Y % 4 == 0 and Y % 100 == 0 and Y % 400 == 0:
        return True
    else :
        return False
def check_season(M):
    if M >= 1 and M <= 12:
        if M >= 3 and M <= 5:
            print('Spring')
        elif M >= 6 and M <= 8:
            print('Summer')
        elif M >= 9 and M <= 11:
            print('Fall')
        else :
            print('Winter')
    

def check_month_days(Y,M,D):
    if check_Yoon(Y) == True:
        if M == 2:
            if D <= 29:
                return True
    else:
        if M in [1,3,5,7,8,10,12]:
            if D <=31:
                return True
        elif M in [4,6,9,11]:
            if D <= 30:
                return True
        elif M == 2:
            if D <= 28:
                return True
        else :
            return False


if check_month_days(Y,M,D) == True:
    check_season(M)
else :
    print('-1')