print('-=-'*20)
print('Digite doi numeros para poder calcular')

print('''   [+] Adição
    [-] Subtração
    [*] Multiplicação
    [/] Divisão''')
print('-=-'*20)
n1=int(input('Digite o primeiro número:'))
n2=int(input('Digite o segundo número:'))
operação=input('Digite a operação')
if operação=='+':
    resultado=n1+n2
elif operação=='-':
    resultado=n1-n2
elif operação=='*':
    resultado=n1*n2
elif operação=='/':
    resultado=n1/n2
print('{} {} {} é igual a {} '.format(n1,operação,n2,resultado))    
