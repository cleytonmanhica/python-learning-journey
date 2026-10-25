frase=str(input('digite uma frase:')).upper().strip()
print('A letra A aparee {} vezes na frase'.format(frase.count('A')) )
print('A primeira letra a apareceu na posicao {}'.format(frase.find('A')+1))
print('A primeira letra A apaece na posicao {}'.format(frase.rfind('A')))