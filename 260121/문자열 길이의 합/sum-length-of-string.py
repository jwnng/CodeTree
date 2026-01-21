n = int(input())
cnt_sum = 0
cnt = 0
words = [ input() for _ in range(n)]
for word in words:
    cnt_sum += len(word)
    for ch in word:
        if ch == 'a':
            cnt += 1 

print(cnt_sum, cnt)