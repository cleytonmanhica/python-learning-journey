print('-=-'*20)
print('Digite um número para ver se é par ou impar')
print('-=-'*20)
numero=int(input('Digite um numero:'))
if numero % 2==0:
    print('O número {} é par!'.format(numero))
else:
    print('O número {} é impar!'.format(numero))