a, o, c = input().split()
a = int(a)
c = int(c)

# Please write your code here.
def add(a,c):
    return a+c

def sub(a,c):
    return a-c

def mul(a,c):
    return a*c

def div(a,c):
    return a//c

if o == '+':
    print(f"{a} {o} {c} = {add(a,c)}")
elif o == '-':
    print(f"{a} {o} {c} = {sub(a,c)}")
elif o == '*':
    print(f"{a} {o} {c} = {mul(a,c)}")
elif o == '/':
    print(f"{a} {o} {c} = {div(a,c)}")
else :
    print('False')