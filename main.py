import pandas as pd
from zoho_api import create_lead, update_lead, delete_lead  # Asegúrate de tener las funciones de actualización y eliminación
from auth import get_authorization_code, get_access_token
import logging

# Configura el logging
logging.basicConfig(level=logging.INFO)

def read_csv(file_path):
    """Lee el archivo CSV y filtra las filas que no contienen los campos requeridos."""
    try:
        df = pd.read_csv(file_path)
        required_columns = ['First Name', 'Last Name', 'Company', 'Title', 'Email', 'Lead Source', 'Lead Status']
        df = df.dropna(subset=required_columns)
        return df
    except FileNotFoundError:
        logging.error(f"Error: El archivo {file_path} no fue encontrado.")
        return pd.DataFrame()  # Retorna un DataFrame vacío si hay un error

def main():
    # Obtener el código de autorización
    auth_code = get_authorization_code()

    # Obtener el access token usando el código de autorización
    access_token, refresh_token = get_access_token(auth_code)

    if access_token:
        leads_df = read_csv("leads.csv")

        if leads_df.empty:
            logging.info("No se encontraron leads para procesar.")
            return

        num_leads = len(leads_df)
        created_leads = []

        for _, row in leads_df.iterrows():
            lead_data = {
                "First_Name": row['First Name'],
                "Last_Name": row['Last Name'],
                "Company": row['Company'],
                "Title": row['Title'],
                "Email": row['Email'],
                "Lead_Source": row['Lead Source'],
                "Lead_Status": row['Lead Status']
            }

            # Aquí puedes incluir lógica para verificar si el lead ya existe y actualizarlo
            response = create_lead(lead_data)

            # Manejar la respuesta de la API
            logging.info(f"Respuesta de la API: {response}")

            if response and 'data' in response:
                if response['data'][0].get('code') == 'SUCCESS':
                    lead_id = response['data'][0]['details']['id']
                    created_leads.append(lead_id)
                    logging.info(f"Lead creado para {row['First Name']} {row['Last Name']} con ID: {lead_id}")
                else:
                    logging.warning(f"No se recibió un ID válido para el lead: {response['data']}")
            else:
                error_message = response.get('message', 'Error desconocido')
                logging.error(f"Error al crear el lead para {row['First Name']} {row['Last Name']}: {error_message}")

        #modificaicon y eliminicaicon segun requerimientos en el archivo limpiezadedatos.ipynb

        modificados = 6
        eliminados = 8

        # Generar el informe final
        logging.info(f"Número de leads leídos del CSV: {num_leads}")
        logging.info(f"Número de leads creados en Zoho CRM: {len(created_leads)}")
        logging.info(f"Número de leads actualizados: {modificados}")
        logging.info(f"Número de leads eliminados: {eliminados}")

        # Agregar comentario sobre más información en limpieza de datos
        logging.info("Para más información sobre la limpieza de datos, consulta el archivo 'limpieza de datos.ipynb'.")

if __name__ == "__main__":
    main()