print('{:=^40}'.format('===== cleyton sales====='))
preco=float(input('preco das compras:'))
print('''FORMAS DE PAGAMENTO
[1] À vista diheiro/cheque.
[2] À vista no cartao.
[3] Em até 2x no cartao.
[4]3x ou mais no cartao.'''     )
opcao=int(input('qual é a opcão:'))
if opcao==1:
    total=preco-(preco*10/100)

elif opcao==2:   
    total=preco-(preco*5/100)

elif opcao==3:
    total=preco
    parcela=total/2
    print('sua compra sera parcelda em 2x de {:.2f}mt'.format(parcela))

elif opcao==4:
   total=preco+(preco*20/100)
   totpar=int(input('em quantas parcelas:'))
   parcela=total/totpar
   print('compra será parcelada em {}x de 2{:.2f}mt'.format(totpar,parcela))
else:
    total=0.0
    print('opcao invalidade de pagamento.tente novamente!')
print('sua compra de {:.2f}mt vai custar {:.2f}mt no final'.format(preco,total))  