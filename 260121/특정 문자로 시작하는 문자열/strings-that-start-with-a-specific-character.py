n = int(input())
words = [ input() for _ in range(n)]
ch = input()
cnt = 0
len_sum = 0
for i in range(n):
    if words[i][0] == ch:
       len_sum += len(words[i])
       cnt += 1

print(cnt,f"{len_sum/cnt:.2f}")