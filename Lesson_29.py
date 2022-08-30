print('- Palindrec -')

a = (input('Digite uma frase: ')).strip().upper()
b = a.split()
c = ''.join(b)

print(c)

inverso = ''
for l in range(len(c) -1, -1, -1):
    inverso = inverso + c[l]
print(inverso)
if c == inverso:
    print('BAH!')
else:
    print('Deu erro')
inverso = c[::-1]
print(inverso)
