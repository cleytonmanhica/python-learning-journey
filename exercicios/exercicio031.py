distancia=int(input('qual e a distancia da viagem'))
pricen=distancia*0.50
if distancia<=200:
    print('a sua viagem custa {} MT '.format(distancia))
else:
    print('a sua viagem custa {}'.format(distancia*0.45))

