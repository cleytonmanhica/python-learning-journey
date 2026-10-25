import random
from time import sleep
print('''vamos jogar pedra papel e tesoura
[1]Pedra
[2]papel
[3]Tesoura
 ''')

player=int(input('escolhe:'))
computer=random.randint(1,3)
sleep(2)
if computer==1:
    if player==1:
        print('EMPATE!')
    elif player==2:
        print('VITORIA!')
    elif player==3:
        print('PERDEU!')
    else:
        print('ERRO,tente novamente!')
elif computer==2:
    if player==1:
        print('PERDEU!')
    elif player==2:
        print('EMPATE!')
    elif player==3:
        print('VITORIA!')
    else:
        print('ERRO,tente novamente!')
elif computer==3:
    if player==1:
        print('VITORIA!')
    elif player==2:
        print('PERDEU!')
    elif player==3:
        print('EMPATE!')  
    else:
        print('ERRO,tente novamente!')
else:
    print('ERRO,tente novamente!')  