words = [ input() for _ in range(10)]
ch = input()
cnt = 0
for i in range(10):
    if words[i][-1] == ch:
        print(words[i][:])
        cnt += 1
    
if cnt == 0:
    print('None')