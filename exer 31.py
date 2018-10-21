n = float(input('digite a distancia'))
if n <= 200:
    p = n*0.50
else:
    p = n*0.45
print('o preço da sua passagem é {}'.format(p))