print('-=-'*10)
print('O programa só para quando você digita 999')
print('-=-'*10)
n=0
soma=0
numero=0
while numero !=999:
    numero=int(input('digite  outro número:'))
    n+=1
    soma+=numero
    
print('você digitou {} números e a soma deles é igual a {} '.format(n,(soma-999)))