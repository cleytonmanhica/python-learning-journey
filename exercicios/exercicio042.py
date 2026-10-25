print('digite tres medids para ver se forma um triangulo!')
med1=float(input('introduz a primeira medida:'))
med2=float(input('introduz a segunda medida:'))
med3=float(input('introduz a terceira medida:'))
 
if med1+med2>med3 and med2+med3>med1 and med3+med1>med2:
 if med1==med2==med3:
    print('com essas medidads da par formar um triangulo equilatero!')
 elif med1!=med2!=med3 and med1!=med3:
    print('com essas medidas da para formar um teiangulo escaleno! ')
 else:
    print('com essas medidas da para formar um triangulo isosceles')

else:
    print('com essas mdidas nao da para forma um triangulo!')
