a,b,c = map(int,input().split())

if a > b :
    if b > c :
        print(b)
    else :
        if a > c :
            print(c)
        else :
            print(a)
else : # b a 
    if a > c :
        print(a)
    else : # b a c
        if b > c :
            print(c)
        else :
            print(b)

