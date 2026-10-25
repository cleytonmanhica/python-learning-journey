from time import sleep
print('intruduza dois numeros para ver qual e o maior e o menor ou se sao iguais')
n1=float(input('intruduz um numero'))
n2=float(input('intruduz outro numero'))
print('Analizando os dado...')
sleep(5) 
if n1>n2:
    print('o primeiro numero e maior')
elif n2<n1:
    print('o segundo numero e o maior')
else:
    print('nao existe o numero maior os dois sao iguais')
