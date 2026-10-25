limite=80
urvl=int(input('qual e a sua velocidade,em km/h'))
if urvl>limite:
    multa=(urvl-limite)*7
    print('o limete de velocidade e de {}km/h e voce estava a {}km/h'.format(limite,urvl))
    print('a sua multa e de {}MT'.format(multa))
else:
    print('obrigado por seguir o codigo de estrada,tenha uma boa viagem')