import json
import os
from dotenv import load_dotenv

# Cargar el archivo .env
load_dotenv()

# Configuración de Zoho CRM utilizando variables de entorno
CLIENT_ID = os.getenv("ZOHO_CLIENT_ID")
CLIENT_SECRET = os.getenv("ZOHO_CLIENT_SECRET")
REDIRECT_URI = os.getenv("ZOHO_REDIRECT_URI")
BASE_URL = "https://www.zohoapis.com/crm/v2"

# Archivo para almacenar los tokens
TOKEN_FILE = 'tokens.json'

# Función para guardar los tokens en un archivo
def save_tokens(access_token, refresh_token):
    tokens = {
        "access_token": access_token,
        "refresh_token": refresh_token
    }
    with open(TOKEN_FILE, 'w') as f:
        json.dump(tokens, f)

# Función para cargar los tokens desde un archivo
def load_tokens():
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'r') as f:
            tokens = json.load(f)
            return tokens.get('access_token'), tokens.get('refresh_token')
    return None, None

# Inicialmente, los tokens se cargan desde el archivo
ACCESS_TOKEN, REFRESH_TOKEN = load_tokens()

# Configura la cabecera para las peticiones a la API
def get_headers():
    return {
        "Authorization": f"Zoho-oauthtoken {ACCESS_TOKEN}"
    }