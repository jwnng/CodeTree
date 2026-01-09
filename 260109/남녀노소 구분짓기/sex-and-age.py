n = int(input())
age = int(input())

if n == 0 and age >= 19 :
    print('MAN')
elif n == 1 and age >= 19 :
    print('WAMAN')
elif n == 0 and age < 19 :
    print('BOY')
else :
    print('GIRL')
