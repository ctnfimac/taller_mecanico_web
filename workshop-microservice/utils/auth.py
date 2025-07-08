import requests
from rest_framework import status
import jwt

SECRET_KEY = "SaaS-tallerweb"
ALGORITHM = "HS256"

def validate_token(token: str):
    """Esta función lo que hace es verificar si el token
    enviado es correcto, para eso hago uso del microservicio
    de Auth
    """
    url = "http://127.0.0.1:8082/validate-token"
    response = requests.post(url, json={"token": token})
    data = response.json()
    if response.status_code == 200:
        return data.get("valid", False), data
    
    if response.status_code == 401:
        return False, {"message": data.get("detail"), "status_code": status.HTTP_401_UNAUTHORIZED}

    return False, {"message": "Error en el sistema", "status_code": status.HTTP_500_INTERNAL_SERVER_ERROR}



def get_payload_from_token(token):
    """
    Función para desncriptar el token
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except jwt.ExpiredSignatureError:
        print("Token expirado")
        return None
    except jwt.InvalidTokenError as e:
        print("Token no válido:", str(e))
        return None