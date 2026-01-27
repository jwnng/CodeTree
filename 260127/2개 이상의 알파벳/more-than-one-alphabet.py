A = input()

# Please write your code here.
def count_check(str):
    s = set(str)
    if len(s) >= 2:
        print('Yes')
    else :
        print('No')
        
count_check(A)