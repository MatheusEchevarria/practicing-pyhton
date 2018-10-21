import random
n1 = input('digite um nome')
n2 = input('digite outro nome')
n3 = input('digite outro nome')
lista = [n1,n2,n3]
escolhido = random.choice(lista)
print('a pessoa escolhida a lavar a louça foi {}'.format(escolhido))

