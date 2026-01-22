s = input()
n = list(s)
word1 = n[0]
word2 = n[1]
for i in range(len(n)):
    if n[i] == word2:
        n[i] = word1

print("".join(n))