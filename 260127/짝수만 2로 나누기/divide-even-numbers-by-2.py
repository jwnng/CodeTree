n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def even_check_print(arr):
    for x in arr:
        if x % 2 == 0:
            print(x//2,end=" ")
        else :
            print(x,end=" ")

even_check_print(arr)
