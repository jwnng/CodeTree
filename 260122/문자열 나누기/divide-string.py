n = int(input())
m = input()
tot_str = ""
for c in m:
    if c != ' ':
        tot_str += c

for i in range(1,len(tot_str)+1):
    if i % 5 == 0:
        print(tot_str[i-1])
    else :
        print(tot_str[i-1],end="")