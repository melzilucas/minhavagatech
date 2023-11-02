from chalice import Chalice
import boto3
from variables import *

app = Chalice(app_name = 'send-message-sms')

@app.route('/send/sms')
def send_sms():
    request = app.current_request
    message = request.json_body      
    number_phone = message['phone_number']
    
    client = boto3.client(
    service_name = 'sns',
    region_name = 'us-east-1',
    aws_access_key_id = aws_access_key_id,
    aws_secret_access_key = aws_secret_access_key
)

    client.publish(
        PhoneNumber = number_phone,
        Message = 'Olá, Minha Vaga Tech! Esse post está incrível!'
    )
    return {'Mensagem': 'SMS enviada com sucesso'}