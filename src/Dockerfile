# Imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar archivos al contenedor
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copiar el código fuente
COPY . .

# Comando de ejecución
CMD ["python", "app.py"]
