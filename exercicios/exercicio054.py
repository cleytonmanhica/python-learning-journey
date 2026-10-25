menor=0
maior=0
ano_actual=int(input('Em que ano estamos:'))
for c in range(7):
    print(c+1)
    ano=int(input('em que ano a {} nasceu:'.format(c)))
    
    now=ano_actual-ano
    if now>=18:
        maior+=1
    elif now<18:
     menor+=1
print('Das 7 pessoas {} já atingiram a maior idade e {} não '.format(maior,menor))
#concluido