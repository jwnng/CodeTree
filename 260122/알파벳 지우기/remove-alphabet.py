a = input()
b = input()
new_a = ""
new_b = ""
for item in a:
    if item.isdigit():
        new_a += item

for item in b:
    if item.isdigit():
        new_b += item
        
print(int(new_a)+int(new_b))