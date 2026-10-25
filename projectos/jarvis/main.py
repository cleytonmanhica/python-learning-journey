import os 
import datetime as dt
#import pyautogui
import requests

print('JARVIS Beta online.sistemas operacionais.')
print('Bom dia,senhor Cleyton.Como posso ajudá-lo')
def agora():
    date=dt.datetime.now()
    
    print(date.strftime("today is  %A, %d of %B  %Y"))

#api integration weather
def temperatura():
    api_key='YOUR API KEY'
    url= 'http://api.weatherapi.com/v1/current.json'

    parametros={
        'key':api_key,
        'q':'Maputo',
        'lang':'pt'
    }
    resposta=requests.get(url,params=parametros)

    if resposta.status_code==200:
        dados_requisicao=resposta.json()
        temp=dados_requisicao['current']['temp_c']
        descricao=dados_requisicao['current']['condition']['text']
        print('Senhor cleyton,neste momento a temperatura de Maputo é de {}°C e as condicoes climáticas são de {}'.format(temp,descricao))



def hora():
    hour=dt.datetime.now()
    print(hour.strftime("senhor cleyton, neste momento são exatamente  %H:%M"))

def calcular():
    primeiro=float(input('primeiro numero:'))
    operacao=input('operacão:')
    segundo=float(input('segundo numero:'))
    if operacao=='+':
        resultado = primeiro+segundo
        print('O resultado de {}+{} é {}'.format(primeiro,segundo,resultado))
    elif operacao=='-':
        resultado=primeiro-segundo
        print('O resultado de {}-{} é {}'.format(primeiro,segundo,resultado))
    elif operacao=='/':
        resultado=primeiro/segundo
        print('O resultado de {} / {} é {}'.format(primeiro,segundo,resultado))
    elif operacao=='*':
        resultado=primeiro*segundo
        print('O resultado de {} x {} é {}'.format(primeiro,segundo,resultado))
def sair():
    print('Aí tamo juntos')


def apresentacao():
    who='Eu me chamo J.A.R.V.I.S que quer dizer just a rather very inteligent system assistente do Sr.Manhiça'
    print(who)

def ola():
    print('como está')
comandos={
    "qualéatemperatura":temperatura,
    "qualatemperatura":temperatura,
    "comoestáatemperatura":temperatura,
    "quantosgrausestão":temperatura,
    "quantosgrausfaz":temperatura,
    "qualéoclima":temperatura,
    "comoestáoclima":temperatura,
    "comoestáotempo":temperatura,
    "qualéatemperaturaagora":temperatura,
    "temperaturaatual":temperatura,
    "jarvisinformeatemperatura":temperatura,
    "jarvisrelatóriometeorológico":temperatura,
    "jarvisverifiqueatemperatura":temperatura,
    'temperatura':temperatura,
    "jarviscomoestãoascondiçõesmeteorológicas":temperatura,
    'quehorassao':hora,
    'olá':ola,
    'oi':ola,
    'quehorassão':hora,
    'quemestu':apresentacao,
    'queméstu':apresentacao,
    'oquetues': apresentacao,
    'dizahora':hora,
    'quehorastens':hora,
    'quediaéhoje':agora,
    'qualeahoraactual':hora,   
    'quehorastemos':hora,
    'diz-meahora':hora,  
    'quediaehoje':agora,
    'qualéadata':agora,
    'qualeadata':agora,
    'emquediaestamos':agora,
    'quediadasemanaéhoje':agora,
    'quediadasemanaehoje':agora,
    'qualéomes':agora,
    'qualéoano':agora,
    'calcule':calcular,
    'calcula':calcular,
    }

    
while True:
    tu=input('Tu:').lower().replace(" ","")
    if tu in comandos:
        comandos[tu]()
   
    elif tu=='sair' or tu=='fechar':
        sair()
        break
    else:
        print('Não entendi esse comando.')
