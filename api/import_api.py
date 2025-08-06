import requests
import logging

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImportAPI:
    """
    Clase POM (Page Object Model) para manejar las operaciones de la API
    """

    def __init__(self, base_url="https://api.test.worldsys.ar", auth_token=None):
        """
        Inicializa la clase ImportAPI
        
        Args:
            base_url (str): URL base de la API
            auth_token (str): Token de autenticación
        """
        self.base_url = base_url.rstrip('/')
        self.auth_token = auth_token
        self.headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {auth_token}" if auth_token else ""
        }

    def send_person(self, person_id):
        """
        Envía una persona a través de la API
        
        Args:
            person_id (int): ID de la persona a enviar
            
        Returns:
            requests.Response: Respuesta de la API
        """
        url = f"{self.base_url}/import"
        payload = [{"personId": person_id}]

        try:
            logger.info(f"Enviando personId: {person_id} a {url}")
            response = requests.post(url, json=payload, headers=self.headers)
            logger.info(f"Respuesta recibida - Status: {response.status_code}, Body: {response.text}")
            return response

        except requests.exceptions.RequestException as e:
            logger.error(f"Error en la petición: {str(e)}")
            raise
