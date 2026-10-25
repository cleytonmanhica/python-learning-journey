soma=0
cont=0
for c in range(1,7):
     n1=int(input('digite o {} valor:'.format(c)))
     if n1% 2==0:
       soma+=n1
       cont+=1
print('voce informou {} numeros pares  e a soma foi {}'.format(cont,soma))
#concluido