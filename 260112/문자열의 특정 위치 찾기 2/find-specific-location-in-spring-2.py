str1 = "apple"
str2 = "banana"
str3 = "grape"
str4 = "blueberry"
str5 = "orange"

ch = input()
cnt = 0
if str1[2] == ch or str1[3] == ch:
    print(str1)
    cnt += 1
if str2[2] == ch or str2[3] == ch:
    print(str2)
    cnt += 1
if str3[2] == ch or str3[3] == ch:
    print(str3)
    cnt += 1
if str4[2] == ch or str4[3] == ch:
    print(str4)
    cnt += 1
if str5[2] == ch or str5[3] == ch:
    print(str5)
    cnt += 1
print(cnt)