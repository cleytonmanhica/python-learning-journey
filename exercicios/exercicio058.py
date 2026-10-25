import random
from time import sleep
palpites=0
computer=random.randint(0,10)
print('-=-'*20)
print('Eu vou escolher um numero entre 0 e 10 tente adivinhar')
print('-=-'*20)
user=int(input('Qual é o seu palpite:'))
while True:

    
    print('loading...')
    sleep(1)
    if computer ==user:
        print('Vitoria')
        palpites+=1
        if palpites==1:
            print('De primeira,Craque')
        break
    elif user>10:
        user=int(input('Numero invalido...tente novamente:'))
    else:
        print('Derrota')
        palpites+=1
        if user>computer:
            print('O numero que eu escolhi é menor!')
            user=int(input('Qual é o seu palpite:'))
        elif user<computer:
            print('O numero que eu escolhi é maior!')  
            user=int(input('Qual é o seu palpite:'))
                                
print('foram necessarios {} palpites para venceres'.format(palpites))
print('Eu escolhi o número {} e voce escolheu {}'.format(computer,user))
#concluido