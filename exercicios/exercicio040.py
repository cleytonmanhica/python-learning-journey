from time import sleep
nota1=float(input('introduz a nota da primeira avaliacao:'))
nota2=float(input('introduz a nota da segunda avaliacao:'))
nota3=float(input('introduz a nota da terceira avaliacao:'))
media=(nota1+nota2+nota3)/3
if media<5.0:
    print('reprovado')
elif media>=5.0 and media<= 6.9:
    print('recuperacao')
elif media>=7.0:
    print('Aprovado')
