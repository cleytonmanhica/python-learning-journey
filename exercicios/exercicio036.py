from time import sleep
house_price=float(input('qual e o valor da casa'))
salario=float(input('quanto voce recebe'))
years=int(input('em quantos anos voce vai pagar o emprestimo'))
total_meses=years*12
prestacao=house_price/total_meses
limite=(salario*30)/100
print('PROCESSANDO OS DADOS...')
sleep(5)

if prestacao>=limite:
    
    print('emprestimo RECUSADO!')
else:
    print('emprestimo APROVADO')