dependado=320
vivo=300
print('='*60)
print('                  SGC agroaves             ')


print('Sistema de gestão de vendas e stock de frangos')
print('Mais organização.Mais controlo.Mais resultados')
print('='*60)
while True:
    print('                  Menu Principal          ')
    print('''            [1]-Registar venda
            [2]-Consultar venda
            [3]-Controlar stock
            [4]-Relatorios
            [5]-Sair
''')
    Answer=int(input('Escolha uma opção de 1,5:'))
    if Answer==1:
        nome=input('Qual é o nome do cliente:')
        quantidade=int(input('Qual é a quantidade:'))
        tipo=input('O frango é Vivo ou depenado[V/M]:').strip().upper()
        pagamento=input('qual é o metodo de pagamento que foi usado:')
        