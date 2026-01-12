n = 25
while True :
    int_input = int(input())
    if n < int_input :
        print('Lower')
    elif n > int_input :
        print('Higher')
    else : 
        print('Good')
        break