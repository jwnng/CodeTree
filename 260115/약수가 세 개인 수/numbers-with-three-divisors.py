start, end = map(int, input().split())

# Please write your code here.
num = 0
# start부터 end까지의 정수 중 약수가 3개인 수를 출력
for i in range(start,end+1):
    # start를 정수 j로 나누어 떨어지면 약수의 갯수를 1 증가
    measure = 0
    for j in range(1,i+1):
        if i % j == 0:
            measure += 1
    if measure == 3:
        num += 1
        
print(num)