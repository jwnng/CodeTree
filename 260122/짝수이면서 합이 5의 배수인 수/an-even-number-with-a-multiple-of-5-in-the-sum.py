n = int(input())

# Please write your code here.
def i_m_g(n):
    a = []
    a.append(n // 10)
    a.append(n % 10)
    return n % 2 == 0 and (a[0] + a[1]) % 5 == 0

if i_m_g(n):
    print('Yes')
else:
    print('No')