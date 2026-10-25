from time import sleep

ano=int(input('ano de nascimento'))
nome=str(input('qual e o seu nome'))
anod=int(input('em que ano estamos'))
idade=anod-ano
print('=====Analisando os dados...=====')
sleep(3)
if idade<18:
    print('ainda tem uns anos para se alistar ao serviço militar')
elif idade==18:
    print('esta na hora de se alistar')
elif idade>18:
    print('bom dia senhor {} ja passou a idade de se alistar.'.format(nome))
print('muito obrigado pela participacao senhor {}.'.format(nome))