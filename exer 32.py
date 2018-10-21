n = int(input('digite um ano'))
if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
    print('o ano {} é bissexto'.format(n))
else:
    print('o ano não é bissexto')