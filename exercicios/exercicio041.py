ano=int(input('ano de nascimento:'))
anocorrente=int(input('qual e o ano decorrente:'))
idade=anocorrente-ano
if idade<=9:
    print('MARIM')
elif idade<=14:
    print('infantil:')
elif idade< 19:
    print('senior')
elif idade==20:
    print('senior')
else:
    print('master')