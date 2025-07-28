# 🚀 FastAPI Dollar Price App

Este es un proyecto de ejemplo de una API RESTful construida con FastAPI que obtiene el precio del dólar de Banxico y lo expone a través de una interfaz web simple.

## ✨ Características

-   **API RESTful:** Endpoint para obtener el precio del dólar. 💰
-   **Integración con Banxico:** Utiliza el servicio de Banxico para obtener datos actualizados. 🏦
-   **Interfaz Web:** Una página web sencilla para visualizar el precio del dólar. 🌐
-   **Contenedorización:** Soporte para Docker para un despliegue fácil y consistente. 🐳
-   **Manejo de Errores:** Implementación de manejadores de excepciones personalizados. 🛡️

## 🛠️ Requisitos

-   Python 3.11+ 🐍
-   Pipenv (para gestión de dependencias) 📦
-   Docker (opcional, para ejecutar en un contenedor) 🚢

## ⚙️ Configuración del Entorno

Crea un archivo `.env` en la raíz del proyecto con tu token de Banxico:

```
BANXICO_TOKEN="TU_TOKEN_DE_BANXICO"
```

Puedes obtener un token de Banxico registrándote en su [sitio web](https://www.banxico.org.mx/SieInternet/consultarDirectorioInternetAction.do?accion=consultarCuadro&idCuadro=CP150&locale=es). 🔑

## ▶️ Ejecución Local

1.  **Clona el repositorio:**

    ```bash
    git clone https://github.com/vicogarcia16/fastapi-dollar-app.git
    cd fastapi-dollar-app
    ```

2.  **Instala las dependencias con Pipenv:**

    ```bash
    pipenv install
    ```

3.  **Activa el entorno virtual y ejecuta la aplicación:**

    ```bash
    pipenv shell
    uvicorn app.main:app --host 0.0.0.0 --port 8000
    ```

    La aplicación estará disponible en `http://localhost:8000`. 💻

## 🐳 Ejecución con Docker

1.  **Construye la imagen Docker:**

    ```bash
    docker build -t fastapi-dollar-app .
    ```

2.  **Ejecuta el contenedor Docker:**

    Asegúrate de tener tu archivo `.env` configurado en la raíz del proyecto.

    ```bash
    docker run --env-file ./.env -p 8000:8000 fastapi-dollar-app
    ```

    La aplicación estará disponible en `http://localhost:8000`. 🚀

## ☁️ Despliegue en Render

Render es una excelente opción para desplegar aplicaciones FastAPI. Puedes conectar tu repositorio de GitHub directamente a Render. Asegúrate de configurar la variable de entorno `BANXICO_TOKEN` en la configuración de tu servicio en Render.

**Pasos generales:**

1.  Crea una nueva Web Service en Render. ✨
2.  Conecta tu repositorio de GitHub. 🔗
3.  Configura el comando de construcción (Build Command) y el comando de inicio (Start Command).
    -   **Build Command:** `pipenv install --system --deploy`
    -   **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
4.  Añade la variable de entorno `BANXICO_TOKEN` en la sección de Environment Variables de tu servicio en Render. 🔑

## 📚 Herramientas y Librerías Utilizadas

-   **FastAPI:** Framework web moderno y rápido para construir APIs con Python. ⚡
-   **Uvicorn:** Servidor ASGI de alta performance para aplicaciones Python. 🚀
-   **Jinja2:** Motor de plantillas para renderizar las vistas HTML. 📄
-   **Requests:** Librería HTTP para hacer peticiones a la API de Banxico. 🌐
-   **Pydantic:** Para la validación de datos y la definición de esquemas. ✅
-   **Pipenv:** Herramienta para la gestión de dependencias y entornos virtuales. 📦

## 📂 Estructura del Proyecto

```
.env
Dockerfile
Pipfile
Pipfile.lock
README.md
.gitignore
app/
├── __init__.py
├── main.py
├── core/
│   ├── __init__.py
│   ├── config.py
│   ├── exception_handlers.py
│   └── exceptions.py
├── routers/
│   ├── __init__.py
│   └── dollar_price.py
├── schemas/
│   └── dollar.py
├── services/
│   ├── __init__.py
│   └── banxico_service.py
├── static/
│   └── css/
│       └── style.css
└── templates/
    ├── base.html
    ├── index.html
    ├── welcome.html
    └── partials/
        └── _footer.html
```
