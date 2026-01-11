s = input()
s1 = s.replace(s[1],'a',1)
s2 = s1.replace(s1[len(s)-2],'a',1)

print(s2)