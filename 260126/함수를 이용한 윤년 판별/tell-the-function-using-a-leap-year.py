y = int(input())

# Please write your code here.
def yun_Year(n):
    if n % 4 != 0 :
        return False
    if (n % 100 == 0 and n % 400 != 0):
        return False

    return True
        
if yun_Year(y) == True:
    print('true')
else :
    print('false')