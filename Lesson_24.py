print('- SOMADOR -')

s = 0
a = 0

for c in range (0, 501, 3):
    if c % 2 == 0:
        print(' ', end = '')
    else:
        print(c, end = '')
        s = s + c
        a = a + 1
print('\n!ACABOU!')
print(s)
print(a)