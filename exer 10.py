moeda = int(input('olá, digite 1 para dolar e 2 para euro'))
if moeda == 1:
    n = float(input('voçe escolheu dolar, digite o valor em reais'))
    resultado = n/3.25
    print('voçe tem {:.2f} dolar'.format(resultado))
    if resultado < 0:
        print('voçe não tem nenhum dolar')
if moeda ==2:
    n = float(input(' voçe escolheu euro, digite o valor reais'))
    resultado = n/4.00
    print('voçe tem {:.2f} euro'.format(resultado))
    if resultado < 0:
        print('voçe não tem nenhum euro')




