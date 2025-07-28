# Usa una imagen base de Python ligera
FROM python:3.11-slim-bookworm

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de Pipenv
COPY Pipfile Pipfile.lock ./

# Instala Pipenv globalmente
RUN pip install pipenv

# Instala las dependencias del proyecto
RUN pipenv install --system --deploy

# Copia el código de la aplicación
COPY app /app/app

# Expone el puerto en el que Uvicorn escuchará
EXPOSE 8000

# Comando para iniciar la aplicación con Uvicorn
# --host 0.0.0.0 permite que la aplicación sea accesible desde fuera del contenedor
CMD ["python3", "-m", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
