while True:
    print('-=-'*10)
    print('''
    [1]Cadastrar novo estudante
    [2]Visualizar/Listar os estudantes cadastrados 
    [3]Comparar medias 
    [4]Listar os 3 melhores estudantes
    [5]Vizualizar quantidade de alunos cadastrados
    [6]Sair do programa
    ''')
    print('-=-'*10)
    comando=int(input('tu:'))
    if comando==1:
        nome=str(input('Nome do estudante:'))
        idade=int(input('Idade:'))
        clesse=int(input('classe:'))
        nota1=float(input('Nota na 1ᵃ avaliação:'))
        nota2=float(input('Nota da 2ᵃ avliação:'))
        nota3=float(input('Nota da 3ᵃ avaliação: '))
        media=nota1+nota2+nota3/3

        continua=input('Quer continuar:').upper()
        if continua=='SIM':
            ...
        else:
            break






    elif comando==6:
        print('see you later')
        break