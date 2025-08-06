# Challenge Técnico - Automatización de API (Worldsys)

Este proyecto contiene la solución automatizada del challenge técnico para pruebas sobre una API RESTful, utilizando `pytest` y estructura basada en POM (Page Object Model).

---

## 🧪 Stack Tecnológico

- **Lenguaje:** Python 3.x
- **Framework de testing:** Pytest
- **Modelo:** Page Object Model (POM) adaptado a APIs
- **Dependencias:** `requests`, `pytest`, `logging`

---

## 📁 Estructura del Proyecto

challenge_worldsys_api/
├── api/
│ └── import_api.py # Lógica de acceso a la API (POM)
├── tests/
│ └── test_import_api.py # Casos de prueba automatizados
├── requirements.txt # Dependencias del entorno
├── README.md # Documentación del proyecto



---

## 🔧 Instalación y configuración

1. Clonar el repositorio:

```bash
git clone https://github.com/tu-usuario/challenge_worldsys_api.git
cd challenge_worldsys_api
Crear y activar entorno virtual (opcional pero recomendado):

python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
Instalar dependencias:


pip install -r requirements.txt
Configurar token de autenticación en test_import_api.py:

auth_token="colocar_token_valido"
 
▶️ Ejecución de pruebas
Desde la raíz del proyecto, ejecutar:
 
pytest tests/test_import_api.py -v
 
✅ Casos cubiertos
Happy Path
personId válido (ej: 111, 200)
→ Se espera una respuesta HTTP 200 y validación del campo personId en la respuesta.

Sad Path
Valores inválidos: string, None, negativos, ID inexistente.
→ Se espera respuesta HTTP 400 o 404 y mensajes de error en cosistencia con el codigo.

Validación de conexión
Se valida que el servicio responde con algún código HTTP válido para detectar errores de conectividad.

⚠️ Nota importante
Actualmente, el endpoint real https://api.test.worldsys.ar/import no se encuentra accesible públicamente.
Los tests están preparados para su ejecución contra ese endpoint, y han sido estructurados bajo todos los criterios del challenge, incluyendo:

Separación POM

Dinamismo del personId

Manejo de errores

Uso de fixtures

Parametrización de escenarios

🧩 Posibles mejoras (no requeridas)
Mockeo local con Mockoon o Flask para validar comportamiento sin acceso real

Logs a archivo

Integración con CI/CD (GitHub Actions, Jenkins)

Validación con DB (según query sugerida)