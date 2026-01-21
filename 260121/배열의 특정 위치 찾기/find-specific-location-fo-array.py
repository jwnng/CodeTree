arr = list(map(int,input().split()))
even_sum = 0
third_sum = 0

for i in range(1,11):
    if i % 2 == 0:
        even_sum += arr[i-1]
    if i % 3 == 0:
        third_sum += arr[i-1]

print(even_sum,f"{third_sum/3:.1f}")
