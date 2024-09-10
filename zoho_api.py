import requests
import logging
from config import BASE_URL, ACCESS_TOKEN

# Configura el logging
logging.basicConfig(level=logging.INFO)

# Función para obtener los headers con el token de acceso
def get_headers():
    return {
        "Authorization": f"Zoho-oauthtoken {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

def create_lead(lead_data):
    url = f"{BASE_URL}/Leads"
    try:
        response = requests.post(url, headers=get_headers(), json={"data": [lead_data]})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error al crear lead: {e}")
        return None

def update_lead(lead_id, updated_data):
    url = f"{BASE_URL}/Leads/{lead_id}"
    try:
        response = requests.put(url, headers=get_headers(), json={"data": [updated_data]})
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error al actualizar lead: {e}")
        return None

def delete_lead(lead_id):
    url = f"{BASE_URL}/Leads/{lead_id}"
    try:
        response = requests.delete(url, headers=get_headers())
        response.raise_for_status()
        return response.status_code
    except requests.exceptions.RequestException as e:
        logging.error(f"Error al eliminar lead: {e}")
        return None

def get_leads_by_criteria(criteria):
    url = f"{BASE_URL}/Leads/search"
    try:
        response = requests.get(url, headers=get_headers(), params=criteria)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Error al obtener leads: {e}")
        return None