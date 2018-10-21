from datetime import date
atual = date.today().year
nasc = int(input('Ano de nascimento'))
idade = atual - nasc
print ('Quem nasceu {} e tem {} anos em {}'.format(nasc,idade,atual))
if idade == 18:
    print ('Voce precisa se alistar  neste ano')
elif idade < 18:
    saldo = idade - 18
    ano = atual = 18
    print ('Faltam {} anos para voce se alistar'. format(saldo))
    print ('seu alistamento sera em {}'.format(ano))
elif idade > 18:
    saldo = idade -18
    ano = atual  - 18
    print ('Voce deveria se alistar em {}'. format(saldo))
    print ('seu alistamento foi em {}'.format(ano))



