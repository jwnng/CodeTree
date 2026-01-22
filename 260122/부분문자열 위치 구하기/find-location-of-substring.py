input_str = input()
target_str = input()

# Please write your code here.
n = len(input_str)
t = len(target_str)
exists = False
idx = -1
for i in range(n-t+1):
    all_same = True
    for j in range(t):
        if input_str[j+i] != target_str[j]:
            all_same = False

    if all_same == True:
        idx = i
        exists = True
        break

if exists == True:
    print(i)
else:
    print(-1)
