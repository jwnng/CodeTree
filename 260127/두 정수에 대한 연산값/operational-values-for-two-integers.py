a, b = map(int, input().split())

# Please write your code here.
def modify(a,b):
    if a > b:
        a += 25
        b *= 2
    elif a < b:
        b += 25
        a *= 2
    return a,b

a,b = modify(a,b)
print(a,b)