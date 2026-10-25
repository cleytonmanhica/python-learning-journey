from time import sleep
times=int(input('Quantos numeros voce quer ver?'))
primeiro=0
segundo=1
numeros=0
resultado=0
soma=0
while times!=numeros :
   print('{}→'.format(primeiro),end='')
   sleep(1)
   resultado= primeiro+segundo
   soma+=primeiro
   primeiro=segundo
   segundo=resultado
   numeros+=1
   
print('FIM.\n A soma de todos os números da sequencia é {}.'.format(soma))