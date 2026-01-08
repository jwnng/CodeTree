n = int(input())

book = 3000
mask = 1000

if n >= 0 and n <= 10000 :
    if n >= book :
        print('book')
    elif n < book and n >= mask :
        print('mask')
    else :
        print('no')
else :
    pass