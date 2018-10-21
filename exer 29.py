n =int(input('digite sua velocidade'))
if n >= 80:
    m = (n - 80) * 7
    print('voce foi multado por exceder o limite de velocidade que é de 80km, sua multa é de R${}'.format(m))
else:
    print('Deus abençoe')