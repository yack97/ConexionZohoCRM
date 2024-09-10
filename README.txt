Proyecto de Gestión de Leads con Zoho CRM

Este proyecto tiene como objetivo la creación, actualización y eliminación de leads en Zoho CRM mediante operaciones CRUD utilizando un archivo CSV con la información inicial. Se implementa una API con autenticación basada en tokens para interactuar con Zoho CRM y un script de Python que procesa los datos de leads desde un archivo CSV. Además, se realiza una limpieza de datos previa en el archivo limpieza_de_datos.ipynb.

Pasos para la Ejecución del Proyecto

1. Obtener Tokens de Autenticación para Zoho CRM

El proceso de autenticación con Zoho CRM se realiza en dos pasos: obtener el código de autorización y luego usar ese código para obtener el token de acceso (access token). Este es un paso clave para permitir que el script interactúe con la API de Zoho CRM.

Paso 1: Obtener el Código de Autorización

El código de autorización se obtiene utilizando las credenciales de la aplicación registrada en Zoho. Este código es necesario para generar el token de acceso y el token de refresco.

Paso 2: Obtener el Token de Acceso

Con el código de autorización, se llama a la función get_access_token(), que genera el access token y el refresh token. Estos tokens se utilizan en cada solicitud a la API de Zoho CRM.

Código para obtener el token:

        from auth import get_authorization_code, get_access_token

        auth_code = get_authorization_code()
        access_token, refresh_token = get_access_token(auth_code)

2. Funcionalidades Principales (CRUD)

Se implementaron tres funciones principales en el archivo zoho_api.py:

	1.	create_lead(lead_data): Crea un lead nuevo en Zoho CRM utilizando los datos del lead.
	2.	update_lead(lead_id, lead_data): Actualiza un lead existente en Zoho CRM con nuevos datos.
	3.	delete_lead(lead_id): Elimina un lead existente en Zoho CRM basado en su ID.

Estas funciones interactúan directamente con la API de Zoho CRM usando el access token obtenido previamente.

Ejemplo de creación de lead:

        lead_data = {
            "First_Name": "John",
            "Last_Name": "Doe",
            "Company": "Example Corp",
            "Title": "Manager",
            "Email": "johndoe@example.com",
            "Lead_Source": "Advertisement",
            "Lead_Status": "Contacted"
        }

        response = create_lead(lead_data)


3. Manejo de Datos con limpieza_de_datos.ipynb

El archivo limpieza_de_datos.ipynb contiene una serie de pasos que se utilizaron para realizar una limpieza y transformación de los datos iniciales del archivo CSV (leads.csv). Esto incluye eliminar datos nulos, filtrar valores indeseados, y realizar reemplazos en los datos.

Pasos Realizados en limpieza_de_datos.ipynb:

	1.	Cargar los Datos:
	2.	Visualizar las Primeras Filas del Archivo:
	3.	Ver el Tamaño del DataFrame:
	4.	Eliminar Filas con Valores Nulos:\
	5.	Eliminar Filas con Fuentes de Leads Indeseadas:
	6.	Reemplazar Valores en la Columna Lead Source:
	7.	Guardar el DataFrame Modificado en un Nuevo CSV:

4. Informe Final

Al ejecutar el script principal (main.py), se genera un informe final que incluye:

	•	Número total de leads leídos desde el CSV.
	•	Número de leads creados en Zoho CRM.
	•	Número de leads actualizados.
	•	Número de leads eliminados.

5. Requerimientos

Antes de ejecutar el proyecto, asegúrate de tener instaladas las siguientes dependencias:

	•	pandas
	•	requests
	•	logging

6. Conclusión

Este proyecto te permite automatizar la gestión de leads en Zoho CRM, realizando las operaciones CRUD de manera programática a partir de un archivo CSV con leads iniciales. El manejo de datos se realizó de forma detallada en el archivo limpieza_de_datos.ipynb para asegurar la calidad de los datos antes de interactuar con la API de Zoho CRM.