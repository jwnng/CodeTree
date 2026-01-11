words = input().split()
word1 = words[0]
word2 = words[1]

if len(word1) > len(word2):
    print(word1, len(word1))
elif len(word1) < len(word2):
    print(word2, len(word2))
else :
    print('same')