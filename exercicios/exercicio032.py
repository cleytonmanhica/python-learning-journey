ano =int(input('digite um ano para ver se e bissexto '))
if ano %4==0 and ano %100==0 and ano %400==0:
    print('o ano {} e bissexto'.format(ano))
else:
    print('o ano {} nao e bissexto'.format(ano))
