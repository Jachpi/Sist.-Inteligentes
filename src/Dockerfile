# 1. Imagen base con Python 3.10
FROM python:3.10-slim

# 2. Instalar dependencias necesarias del sistema
RUN apt-get update && apt-get install -y \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libsm6 \
    libxext6 \
    libxrender-dev \
    && rm -rf /var/lib/apt/lists/*

# 3. Crear directorio de trabajo
WORKDIR /app

# 4. Copiar los archivos de la aplicación
COPY . /app

# 5. Instalar dependencias de Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# 6. Exponer el puerto (opcional si tienes servidor web)
EXPOSE 8000

# 7. Comando para ejecutar la aplicación
CMD ["python", "main.py"]
