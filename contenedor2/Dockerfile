# Imagen base de Python
FROM python:3.10

# Configuración del directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación
COPY . .

# Instalar dependencias
RUN pip install flask psycopg2

# Exponer el puerto donde correrá la aplicación Flask
EXPOSE 5001

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
