# postgres-with-doker
Este proyecto muestra cómo usar Docker Compose para orquestar una API en Flask con una base de datos PostgreSQL


#Requisitos Previos

Antes de ejecutar el proyecto, se requiere de tener instalados:

Docker
Docker Compose

#Instalación y Ejecución

1. Clonar el repositorio

git clone https://github.com/tu-usuario/tu-repo.git
cd tu-repo

2. Crear y levantar los contenedores con Docker Compose

docker-compose up --build

Esto iniciará los servicios de la base de datos y la API.

3. Verificar que los contenedores están corriendo

docker ps

Debe mostrar dos contenedores en ejecución: backend (Flask API) y db (PostgreSQL).

#Uso de la API

Obtener todos los estudiantes

curl -X GET http://localhost:5000/students

Obtener un estudiante por ID

curl -X GET http://localhost:5000/students/1

Agregar un nuevo estudiante

curl -X POST http://localhost:5000/students \
     -H "Content-Type: application/json" \
     -d '{"name": "Juan", "age": 22, "career": "Ingeniería"}'

Actualizar un estudiante por ID

curl -X PUT http://localhost:5000/students/1 \
     -H "Content-Type: application/json" \
     -d '{"name": "Juan Pérez", "age": 23, "career": "Matemáticas"}'

Eliminar un estudiante por ID

curl -X DELETE http://localhost:5000/students/1

Detener y eliminar contenedores

Para detener los contenedores, usa:

docker-compose down

Volúmenes de datos

La base de datos se almacena en un volumen de Docker para persistencia de datos:

volumes:
  db_data:

Para eliminar la base de datos completamente, ejecuta:

docker volume rm docker_compose_sql_db_data

#Notas

Asegúrarse de que el puerto 5000 no esté ocupado en la máquina.
Se puede modificar la configuración de la base de datos en docker-compose.yml.
