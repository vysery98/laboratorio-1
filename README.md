# API Laboratorio 1

Desarrollada por 
Luis Quizhpe
Miguel Perez
Juan Diego Guevara

## Tecnologías usadas
Python
Flask
Docker
curl
GitHub

## Estructura del proyecto
main.py código fuente principal
requirements.txt  dependencias
Dockerfile  configuración del contenedor
README.md  documentación del proyecto
scoreCredit.py evalua score crediticio de personas
auth.py autenticacion de usuario
appHealth.py muestra estado de app

## Endpoints

### GET /
Devuelve un mensaje de bienvenida y datos básicos del API.

### GET /health
Verifica si el servicio está activo.

### GET /scoreCredit
Muestra score crediticio

### POST /auth
Ingreso de credenciales usuario


### Ejemplo de request
```json
curl -X POST http://127.0.0.1:8080/auth/login -H "Content-Type: application/json" -d "{\"username\":\"admin\",\"password\":\"1234\"}"
 