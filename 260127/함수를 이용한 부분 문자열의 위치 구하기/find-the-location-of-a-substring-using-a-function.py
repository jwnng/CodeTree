text = input()
pattern = input()

# Please write your code here.
def seq_part():
    if pattern in text:
        c = text.find(pattern)
        print(c)
    else :
        print('-1')

seq_part()