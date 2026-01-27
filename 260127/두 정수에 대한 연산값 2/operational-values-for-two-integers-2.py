a, b = map(int, input().split())

# Please write your code here.
def modify(a,b):
    if a > b:
        a *= 2
        b += 10
    elif a < b:
        a += 10
        b *= 2
    return a,b

a,b = modify(a,b)
print(a,b)