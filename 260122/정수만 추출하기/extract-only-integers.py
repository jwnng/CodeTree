a,b = input().split()
new_a = ""
new_b = ""
for item in a:
    if item.isdigit():
        new_a += item
    else:
        break

for item in b:
    if item.isdigit():
        new_b += item
    else:
        break

print(int(new_a)+int(new_b))