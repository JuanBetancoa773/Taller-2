# 1️⃣ Imagen base oficial de Python
FROM python:3.10-slim

# 2️⃣ Define el directorio de trabajo dentro del contenedor
WORKDIR /app

# 3️⃣ Copia los archivos del proyecto al contenedor
COPY . /app

# 4️⃣ Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# 5️⃣ Expone el puerto 5000 (Flask usa este por defecto)
EXPOSE 5000

# 6️⃣ Comando para ejecutar la aplicación
CMD ["python", "app.py"]
