age=0
maior_mulher=0
maior_homem=0
name=''
for c in range(4):
    print(c+1)
    nome=str(input('Qual é o seu nome:'))
    idade=int(input('Quantos anos você tem:'))
    sexo=str(input('O seu sexo é Masculino ou Femenino:')).lower()
    age+=idade/4
    if sexo=='femenino' and idade<20:
            maior_mulher+=1
    elif sexo=='masculino' and c==1:
        maior_homem=idade
        name=nome
    else:
        if sexo=='masculino' and idade>maior_homem:
            maior_homem=idade
            name=nome

   
print('O nome do homem mais velho é {}'.format(name ))

print('Neste grupo tem {} mulheres com menos de 20 anos'.format(maior_mulher))

print('A media de idade do grupo é de {:.0f} anos'.format(age))