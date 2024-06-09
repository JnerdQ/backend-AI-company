# Usa una imagen base de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /code

# Copia el archivo de requerimientos al directorio de trabajo
COPY ./requirements.txt /code/requirements.txt

# Instala las dependencias
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copia el archivo de base de datos
COPY ./database.db /code/database.db

# Copia el resto de los archivos de la aplicacion al directorio de trabajo
COPY . /code

# Expone el puerto que se va a usar
EXPOSE 4000

# Comando para correr la aplicación usando uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "4000"]
