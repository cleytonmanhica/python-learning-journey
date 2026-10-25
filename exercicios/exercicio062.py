print('Gerador de PA')
print('-=-'*10)
primeiro=int(input('Primeiro termo:'))
razão=int(input('Razão:'))
termo=primeiro
cont=1
total=0
mais=10
while mais!= 0:
    total=total+mais
    while cont<=total:
        print('{}--'.format(termo),end='') 
        termo+=razão
        cont+=1
    print('pausa')  
    mais=int(input('Quantos termos você quer mostrar mais:'))
        
print('A progressão foi finalizada com {} termos mostrados'.format(total))
#concluido com tutorial e com raciocineo mas a parte mai importante  acredito eu foi com o raciocineo
