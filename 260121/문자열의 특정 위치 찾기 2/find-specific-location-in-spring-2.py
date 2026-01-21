arr = [ "apple", "banana", "grape", "blueberry", "orange" ]
a = input()
cnt = 0
for i in range(5):
    for j in range(10):
        if j == 2 or j == 3:
            if arr[i][j] == a:
                print(arr[i])
                cnt += 1
    
print(cnt)