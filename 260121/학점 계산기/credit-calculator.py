n = int(input())
scores = list(map(float,input().split()))

sum_val = sum(scores[:])/n
print(f"{sum_val:.1f}")
if sum_val >= 4.0:
    print('Perfect')
elif sum_val >= 3.0:
    print('Good')
else:
    print('Poor')