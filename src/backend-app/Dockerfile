# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Evita que Python escriba ficheros .pyc
ENV PYTHONDONTWRITEBYTECODE 1
# Asegura que la salida de Python se muestre en la terminal sin buffer
ENV PYTHONUNBUFFERED 1

# Crea un usuario no-root para correr la aplicación por seguridad
RUN groupadd -r appuser && useradd -r -g appuser appuser

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el fichero de requerimientos PRIMERO para aprovechar el caché de Docker
COPY requirements.txt .

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copia el resto del código de la aplicación
COPY . .

# Cambia al usuario no-root
USER appuser

# Expone el puerto en el que corre la aplicación
# ... (resto del fichero)
EXPOSE 8080
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "app:app"]