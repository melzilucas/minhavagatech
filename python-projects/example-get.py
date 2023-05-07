import requests
import json
import datetime

#variables
access_key = '' #crie sua conta gratuita https://meteum.ai/b2b/console/home e capture sua chave (key)
latitude = '-30.0277' #colocar latitude da cidade
longitude = '-51.2287' #colocar longitude da cidade
now = datetime.datetime.now()
date_and_hours = now.strftime("%d/%m/%Y %H:%M:%S")

try:
    headers = {
        'X-Meteum-API-Key': access_key
    }

    response = requests.get(
        f'https://api.meteum.ai/v1/fact?lat={latitude}&lon={longitude}', headers=headers)

    response = response.json()
    #print(response)
    temp = response['temp']

    print('A temperatura para Porto Alegre hoje:', date_and_hours, 'é de', temp,'°C')

#depois é só rodar o código ou executar via terminal: python example-get.py
except NameError as erro:
    print(erro)