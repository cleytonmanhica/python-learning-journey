salario=int(input('qual e o seu salario'))
if salario>1250:
    print('voce recebe um aumento de 10% e  voce passa a ganhar {} '.format((salario*10)/100+salario))
else:
    print('voce recebe um aumento de 15% e voce passa a ganhar {}'.format((salario*15)/100+salario))