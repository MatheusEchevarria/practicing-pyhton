casa = float(input('Valor da casa; R$'))
salario = float(input('Salario do comprador'))
anos = int (input('Quantos anos de financiamento?'))
prestaçao = casa / (anos * 12)
minimo = salario * 30 / 100
print('Para pagar uma casa de R${:.2f} em {} anos'.format(casa, anos), end='')
print('A prestação será de R${:.2f}'.format(prestaçao))
if prestaçao <= minimo:
    print('Emprestimo pode ser CONCEDIDO')
else:
    print('Emprestimo NEGADO pradordor; R$')
