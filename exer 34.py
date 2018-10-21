num = float(input('digite seu salario'))
if num <= 1250:
    aumento = (num*15/100)+num
else:
    aumento = (num*10/100)+num
print(' Seu salario passa a ser de  {}'.format(aumento))
