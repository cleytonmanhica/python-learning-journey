import random
from time import sleep

computer=random.randint(0,5)
print('-=-'*10)
print('i will choose one number between 0 and 5')
print('-=-'*10)
user=int(input('choose one numeber between 0 and 5:'))
print('loading...')
sleep(5)
print('the computer chose {},and you chose {}'.format(computer,user))

if computer==user:
    print('VICTORY')
else:
    print('GAME OVER')

