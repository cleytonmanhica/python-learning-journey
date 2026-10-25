n1=int(input('digite o primeiro numero:'))
n2=int(input('digite o segundo numero:'))
while True:  

    print('-=-'*20)
    print('[1]somar')
    print('[2]Multiplicar')
    print('[3]maior')
    print('[4]novos numeros')
    print('[5]sair do programa ')
    print('-=-'*20)
    resposta=int(input('Oque queres fazer:'))
    if resposta==1:
        resultado=n1+n2
        print('{} + {} é {}'.format(n1,n2,resposta))
    elif resposta==2:
        resultado=n1*n2
        print('{} x {} é {}'.format(n1,n2,resultado))
    elif resposta==3:
        if n1>n2:
            print('O numero {} é maior que {}'.format(n1,n2))
        elif n2>n1:
            print('o numero {} é maior que {}'.format(n2,n1))
        elif n1==n2:
            print('são iguais')
        else:
            print('erro')
    elif resposta==4:
        n1=int(input('digite o primeiro numero:'))
        n2=int(input('digite o segundo numero:'))
    elif resposta==5:
        print('Adeus')
        break
    else:
        print('comando invalido,tente novamente')
#cocluido