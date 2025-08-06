import pytest
from api.import_api import ImportAPI

class TestImportAPI:
    """
    Clase de tests para la API de importación
    """
    
    @pytest.fixture
    def api_client(self):
        """
        Fixture para crear una instancia del cliente API
        """
        # Configuración para la API real del challenge
        return ImportAPI(
            base_url="https://api.test.worldsys.ar",
            auth_token="******"  
        )
    
    @pytest.mark.parametrize("person_id, expected_status", [
        (111, 200),  # Happy path
        (200, 200),  # Happy path
    ])
    def test_send_person_happy_path(self, api_client, person_id, expected_status):
        """
        Test del happy path - casos exitosos
        
        Args:
            api_client: Fixture del cliente API
            person_id (int): ID de la persona
            expected_status (int): Status code esperado
        """
        response = api_client.send_person(person_id)
        
        # Validaciones
        assert response is not None, "La respuesta fue None (fallo de conexión)"
        assert response.status_code == expected_status, f"Status esperado: {expected_status}, obtenido: {response.status_code}"
        
        # Validación del contenido de la respuesta 
        if response.status_code == 200:
            response_json = response.json()
            assert "personId" in response_json, "personId no encontrado en la respuesta"
            assert response_json["personId"] == person_id, "personId en respuesta no coincide"
        
        print(f"[INFO] person_id={person_id}, status={response.status_code}, body={response.text}")
    
    @pytest.mark.parametrize("person_id, expected_status", [
        ("invalid", 400),  # Sad path - string inválido
        (None, 400),       # Sad path - None
        (-1, 400),         # Sad path - número negativo
        (999999, 404),     # Sad path - ID inexistente
    ])
    def test_send_person_sad_path(self, api_client, person_id, expected_status):
        """
        Test del sad path - casos de error
        
        Args:
            api_client: Fixture del cliente API
            person_id: ID de la persona (inválido)
            expected_status (int): Status code esperado
        """
        response = api_client.send_person(person_id)
        
        # Validaciones para casos de error
        assert response is not None, "La respuesta fue None (fallo de conexión)"
        assert response.status_code == expected_status, f"Status esperado: {expected_status}, obtenido: {response.status_code}"
        
        # Validar que hay un mensaje de error apropiado
        if response.status_code >= 400:
            response_text = response.text.lower()
            error_indicators = ["error", "invalid", "not found", "bad request"]
            has_error_message = any(indicator in response_text for indicator in error_indicators)
            assert has_error_message or len(response_text) > 0, "No se encontró mensaje de error apropiado"
        
        print(f"[INFO] person_id={person_id}, status={response.status_code}, body={response.text}")
    
    def test_send_person_connection_validation(self, api_client):
        """
        Test adicional para validar la conexión básica
        """
        # Test con un ID válido básico
        response = api_client.send_person(111)
        
        # Al menos debe haber una respuesta (aunque falle por URL incorrecta)
        assert response is not None, "No se pudo establecer conexión con la API"
        
        # El status debe ser un código HTTP válido
        assert isinstance(response.status_code, int), "Status code no es un entero válido"
        assert 100 <= response.status_code <= 599, f"Status code inválido: {response.status_code}"
