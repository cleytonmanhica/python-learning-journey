import random
computer=random.randint(0,10)
print('---'*20)
print('Eu escolhi um número entre 0 e 10,tente adivinhar qual é!')
print('---'*20)
palpite=0
while True:
    user=int(input('Qual é o teu palpite:'))
    palpite+=1
    if user==computer:
        if palpite==1:
            print('De primeira, que sorte é essa!')
        break
    elif user>computer:
        print('O número que eu escolhi é menor que {}'.format(user))
    elif user<computer:
        print('O número que eu escolhi é maior que {}'.format(user))
print('foram necessarios {} palpites para venceres.'.format(palpite))