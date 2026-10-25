masculino=0
femenino=0
while True:
    sexo=input('qual é o seu genéro M ou F:').strip().upper()[0]
    if sexo=='M' or sexo=='F':
        print('sexo {} resgistrado com sucesso'.format(sexo))
        break
    else:
        print('Por favor digite novamente!')
#feito so que esta diferente doque esta no video, ele nao usou if e else