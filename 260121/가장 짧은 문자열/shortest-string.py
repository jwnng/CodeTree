a = len(input())
b = len(input())
c = len(input())

if a>b:
    if b>c:
        print(a-c)
    else :
        if a>c:
            print(a-b)
        else :
            print(c-b)
else :
    if a>c:
        print(b-c)
    else :
        if c>b:
            print(c-a)
        else:
            print(b-a)

