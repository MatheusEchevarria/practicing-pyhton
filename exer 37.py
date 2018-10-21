num = int(input('digite um numero inteiro'))
print('''Escolha umas bases para conversão:
[ 1 ] conversão em binário
[ 2 ] converter para octal
[ 3 ] converter para hexadecimal''')
opção = int(input('Sua opção:'))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para hexadecial é igual a {}'.format(num,hex(num)[2:]))
