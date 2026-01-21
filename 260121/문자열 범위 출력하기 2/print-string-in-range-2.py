str = input()
n = int(input())

if n >= len(str):
    print(str[::-1])
else :
    print(str[-1:-n-1:-1])