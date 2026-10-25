frase=str(input('digite um frase').strip()).upper()
palavra=frase.split()
junto=''.join(palavra)
inverso=''
for letra in range(len(junto(-1,-1,-1))):
    inverso+=junto[letra]
print('O inverso de {} é {} '.format(junto,inverso))
if inverso==junto:
    print('temos um palindromo')
else:
    print('a frase digítada não é um palindro')
#concluido mas nao fui eu que fiz foi no curso
