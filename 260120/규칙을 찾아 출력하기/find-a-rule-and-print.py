n = int(input())

for i in range(1,n+1):
    for j in range(1,n+1):
        if i != 1 and j != 1 and i != n and j != n :
            if j == i or i < j :
                print(" ",end=" ")
            else :
                print("*",end=" ")
        else : 
            print("*",end=" ")
    print()
                