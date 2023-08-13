from chalice import Chalice, Response, UnauthorizedError
import json

app = Chalice(app_name='api-minhavagatech')

VALID_TOKEN = '123' #realizar consulta ao DB para validação ou usar JWT com key.


@app.route('/test/api/auth', methods=['POST'])
def recive_webhook():
    request = app.current_request
    message = request.json_body
    headers = request.headers            
    message_body_json = json.dumps(message, indent=4)

    authorization_header = app.current_request.headers.get('Authorization', '')

    if not authorization_header:
        return Response(status_code = 401,
                        headers = {"Content-Type": "application/json"},
                        body= {
                            "Message" : "Token não fornecido",                             
                            }
                )

    if authorization_header.startswith('Bearer ') and authorization_header[7:] == VALID_TOKEN:
        return Response(status_code = 200,
                headers = {"Content-Type": "application/json"},
                body= {
                    "Message" : "Autorizado",                             
                    }
        )
    else:
        return Response(status_code = 401,
                headers = {"Content-Type": "application/json"},
                body= {
                    "Message" : "Token não válido",                             
                    }
        )

@app.route('/calculate', methods=['POST'])
def calculate():
    request = app.current_request
    data = request.json_body
    if 'operation' not in data or 'num1' not in data or 'num2' not in data:
        return Response( 
            status_code=400, 
            body=json.dumps({'error': 'Faltam parâmetros obrigatórios para realizar a operação, num1 e num2'}),
            headers={'Content-Type': 'application/json'}
            )

    operation = data['operation']
    num1 = data['num1']
    num2 = data['num2']
    
    if not isinstance(num1, (int, float)) or not isinstance (num2, (int, float)):
        return Response(
            status_code=400,
            body=json.dumps({'error': 'Os valores num1 e num2 devem ser números'}), 
            headers={'Content-Type': 'application/json'}
    )

    result = None
    if operation == 'add':
        result = num1 + num2
    elif operation == 'subtract':
        result = num1 - num2
    elif operation == 'multiply': 
        result = num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return Response(
                    status_code=400,
                    body=json.dumps({'error': 'Não é possível dividir por zero'}), 
                    headers={'Content-Type': 'application/json'}
                    )

        result = num1 / num2
    else:
        return Response(
                status_code=400,
                body=json.dumps({'error': 'Operação inválida. As operações válidas são: add, subtract, multiply, divide'}), 
                headers={'Content-Type': 'application/json'}
                )
    return Response(
            status_code=200,
            body=json.dumps({'result': result}), 
            headers={'Content-Type': 'application/json'}
    )