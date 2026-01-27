n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
def mod_abs(arr):
    for x in arr:
        print(abs(x),end=" ")

mod_abs(arr)