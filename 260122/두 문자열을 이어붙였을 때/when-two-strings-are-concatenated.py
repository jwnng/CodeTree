a = input()
b = input()

m1 = a + b
m2 = b + a
cnt = 0
for i in range(len(a+b)):
    if m1[i] == m2[i]:
        cnt += 1

if cnt == len(a+b):
    print('true')
else :
    print('false')