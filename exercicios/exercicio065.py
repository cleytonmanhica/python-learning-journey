n=0
media=0
maior=0
menor=0
continuar=str(input('Quer iniciar o programa[S/N]:')).strip().upper()

while continuar=='S':
    numero=int(input('Digite um numero:'))

    n+=1
    media+=numero
    if n ==1:
        maior=numero
        menor=numero
    else:
        if numero<menor:
            menor=numero
        if numero>maior:
            maior=numero
    continuar=str(input('Quer continuar[S/N]:')).strip().upper()[0]
    while continuar not in {'N','S'}:
        print('resposta invalida!')
        continuar=str(input('Quer continuar[S/N]:')).strip().upper()[0]
if  n!=0:
    media=media/n

print('Foram introduzidos {} números\nA media é {} '.format(n,media)) 
print('O maior número introduzido foi  {} e o menor foi {}'.format(maior,menor))
       
