A = input()

# Please write your code here.
def palindrome(str):
    if str == str[::-1]:
        return True
    else:
        return False

if palindrome(A) == True:
    print('Yes')
else:
    print('No')
