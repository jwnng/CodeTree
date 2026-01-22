s = input()
l = len(s)
if l % 2 == 0:
    for i in range(l-1,0,-2):
            print(s[i],end="")
else :
    for i in range(l-2,0,-2):
            print(s[i],end="")