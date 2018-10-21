a = int(input('digite um numero'))
b = int(input('digite outro numero'))
c = int(input('digite outro numero'))
menor = a
if b<a and b<c:
    menor = b
if c<b and c<a:
    menor = c
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('o menor numero é o {}'.format(menor))
print('o maior numero é {}'.format(maior))