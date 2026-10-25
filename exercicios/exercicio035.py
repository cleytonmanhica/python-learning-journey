print('intruduz 3 medidas para ver se da para formar um triangulo')

md=float(input('digite uma medida em metros:'))
med=float(input('digite uma medida em metros:'))
m=float(input('digite uma medida em metros:'))

if md+med>m and md+m>med and med+m>md:
    print('com essas medidas da para formar um triangulo ')
else:
    print('com essas medidas nao da para formar um triangulo')