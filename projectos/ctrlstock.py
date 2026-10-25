from time import sleep
print('''=======SGC Avicultura======= ''')
print('''As opcoes disponiveis sao 
[1]Vivo 300MZN
[2]Depenado 320MZN ''')
c=600
print('NOS actualmente temos {} galinhas, lembrando a compra nao pode ser maior que o numero de galinhas disponiveis'.format(c))
compra=int(input('quantas galinhas queres comprar:'))
print('loading...')
sleep(1)
if compra>c:
    print('ERRO, tente novamente')
elif compra==0:
    print('Erro, tente novamente')
elif compra == c:
    print('Parabens! acabou o stoke,na proxima compra tem o desconto de 25%,muito obrigado por escolher a SGC')
else:
    print('compra registrada, muito obrigado por escolher a SGC')