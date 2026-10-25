peso=float(input('qual e o seu peso:'))
altura=float(input('qual e a sua altura:'))
imc=peso/altura**2
if imc<18.5:
    print('abaixo do peso')
elif imc<25.0:
    print('ideal')
elif imc<30:
    print('sobrepeso')
elif imc<40:
    print('obessidade')
else:
    print('obesidade morbida')