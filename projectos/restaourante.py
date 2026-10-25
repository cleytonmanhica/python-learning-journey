print('======Restaurante SGC====== ')
print('Bem vindo(s) ao nosso restaurante')
d=int(input('qual e o numero de pessoas nesta messa:'))
print('''Os principais pratos sao:
[1]Batata e frango
[2]ovo cozido
[3]Camarao
[4]Carne de porco
[5]peixe grelhado
[6]So uma agua
''')
pratos=0

for c in range(d):
    b=int(input('Qual será o {} pedido:'.format(c+1)))
    pratos+=b
    print('O numero de refeicoes pedidas sao{}'.format(pratos))
print('Muito obrigado por escolher o nosso restaurante')