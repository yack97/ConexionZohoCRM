import requests
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, save_tokens

def get_authorization_code():
    # URL de autorización para obtener el código
    auth_url = f"https://accounts.zoho.com/oauth/v2/auth?response_type=code&client_id={CLIENT_ID}&scope=ZohoCRM.modules.ALL&redirect_uri={REDIRECT_URI}&access_type=offline&prompt=consent"
    print("Visita la siguiente URL para obtener el código de autorización:")
    print(auth_url)
    auth_code = input("Introduce el código de autorización: ")
    return auth_code

def get_access_token(auth_code):
    token_url = "https://accounts.zoho.com/oauth/v2/token"
    data = {
        "grant_type": "authorization_code",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "redirect_uri": REDIRECT_URI,
        "code": auth_code
    }

    try:
        response = requests.post(token_url, data=data)
        response.raise_for_status()  # Lanza un error si la respuesta es un código de error
        token_json = response.json()

        # Obtener y guardar los tokens
        access_token = token_json.get('access_token')
        refresh_token = token_json.get('refresh_token')

        if access_token and refresh_token:
            print("Tokens obtenidos con éxito.")
            print(f"Access Token: {access_token}")
            print(f"Refresh Token: {refresh_token}")
            save_tokens(access_token, refresh_token)  # Guardar tokens
            return access_token, refresh_token
        else:
            print(f"Error al obtener tokens: {token_json.get('error')}, {token_json.get('error_description')}")
            return None, None
    except requests.exceptions.RequestException as e:
        print(f"Error en la solicitud: {e}")
        return None, None