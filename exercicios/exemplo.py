nome=input('aluno:')
idade=int(input('idade:'))
n1=float(input('1 nota:'))
n2=float(input('2 nota:'))
n3=float(input('3nota:'))

media=(n1+n2+n3)/3
print('a sua media e {:.2f}'.format(media))
print('n\====RESULTADO====')
if media>=10:
    print('situaçao: aprovado')
else:
    print('situaçao: reprovado')
