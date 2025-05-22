# Proyecto Docker: Dos Aplicaciones Flask con MariaDB y PostgreSQL

[![Estado del Proyecto](https://img.shields.io/badge/estado-demostrativo-green)](https://github.com/EstebanGC222/DockerProyecto) <!-- Reemplaza con tu URL de repo si es diferente -->
[![Lenguaje](https://img.shields.io/badge/lenguaje-Python-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Flask-orange.svg)](https://flask.palletsprojects.com/)
[![Orquestación](https://img.shields.io/badge/orquestación-Docker%20Compose-blue.svg)](https://docs.docker.com/compose/)
[![Base de Datos](https://img.shields.io/badge/bases%20de%20datos-MariaDB%20%7C%20PostgreSQL-lightgrey.svg)]()

Este proyecto demuestra la configuración y ejecución de dos aplicaciones web Python Flask independientes, cada una conectada a su propia base de datos (MariaDB y PostgreSQL, respectivamente). La orquestación de todos los servicios (las dos aplicaciones Flask y las dos bases de datos) se gestiona mediante Docker Compose.

## Tabla de Contenidos
* [Descripción General](#descripción-general)
* [Tecnologías Utilizadas](#tecnologías-utilizadas)
* [Servicios Definidos](#servicios-definidos)
* [Detalles de las Aplicaciones](#detalles-de-las-aplicaciones)
    * [Aplicación 1: Flask con MariaDB (Contenedor1)](#aplicación-1-flask-con-mariadb-contenedor1)
    * [Aplicación 2: Flask con PostgreSQL (Contenedor2)](#aplicación-2-flask-con-postgresql-contenedor2)
* [Autor](#autor)

## Descripción General
El propósito de este proyecto es:
1.  Mostrar cómo contenerizar aplicaciones Flask individuales usando Docker.
2.  Ejemplificar la configuración de servicios de bases de datos MariaDB y PostgreSQL en contenedores Docker.
3.  Utilizar Docker Compose para definir, construir y ejecutar un sistema multi-contenedor compuesto por las dos aplicaciones Flask y sus respectivas bases de datos.
4.  Cada aplicación Flask implementa un CRUD básico para usuarios e ítems, interactuando con su base de datos asignada.


## Tecnologías Utilizadas
*   **Python 3.10**: Lenguaje para las aplicaciones Flask.
*   **Flask**: Microframework web para Python.
*   **Flask-MySQLdb**: Extensión de Flask para interactuar con MariaDB/MySQL (usado en App 1).
*   **psycopg2**: Adaptador de PostgreSQL para Python (usado en App 2).
*   **Docker**: Plataforma de contenedores.
*   **Docker Compose**: Herramienta para definir y ejecutar aplicaciones Docker multi-contenedor.
*   **MariaDB**: Sistema de gestión de bases de datos relacional (para App 1).
*   **PostgreSQL**: Sistema de gestión de bases de datos objeto-relacional (para App 2).

## Servicios Definidos
El archivo `docker-compose.yml` define los siguientes servicios:
*   **`cont1-flask`**:
    *   Construye desde `./contenedor1`.
    *   Aplicación Flask que se conecta a `mariadb`.
    *   Expone el puerto `5000` del host al `5000` del contenedor.
    *   Depende del servicio `mariadb`.
*   **`cont2-flask`**:
    *   Construye desde `./contenedor2`.
    *   Aplicación Flask que se conecta a `postgres`.
    *   Expone el puerto `5001` del host al `5001` del contenedor.
*   **`postgres`**:
    *   Utiliza la imagen oficial `postgres:latest`.
    *   Configura usuario, contraseña y base de datos mediante variables de entorno.
    *   Expone el puerto `5432` para acceso (opcional, principalmente para herramientas de gestión).
*   **`mariadb`**:
    *   Utiliza la imagen oficial `mariadb:latest`.
    *   Configura contraseña de root, usuario, contraseña de usuario y base de datos mediante variables de entorno.
    *   Expone el puerto `3306` para acceso.
*   Todos los servicios están conectados a una red definida llamada `app-network`.


## Detalles de las Aplicaciones

Ambas aplicaciones Flask proporcionan una API RESTful para gestionar usuarios e ítems, y crean las tablas necesarias en sus respectivas bases de datos al iniciarse.

### Aplicación 1: Flask con MariaDB (`cont1-flask`)
*   **Puerto de acceso:** `http://localhost:5000`
*   **Base de datos conectada:** MariaDB (servicio `mariadb`)
*   **Mensaje de bienvenida en `/`**: "Bienvenido a la aplicación con MariaDB"
*   **Endpoints Principales:**
    *   `POST /register`: Registra un nuevo usuario (`{"username": "user", "password": "pw"}`).
    *   `POST /login`: Inicia sesión (`{"username": "user", "password": "pw"}`).
    *   `GET /users`: Lista todos los usuarios.
    *   `POST /items`: Crea un nuevo ítem (`{"name": "item_name", "description": "desc"}`).
    *   `GET /items`: Lista todos los ítems.
    *   `PUT /items/<item_id>`: Actualiza un ítem.
    *   `DELETE /items/<item_id>`: Elimina un ítem.

### Aplicación 2: Flask con PostgreSQL (`cont2-flask`)
*   **Puerto de acceso:** `http://localhost:5001`
*   **Base de datos conectada:** PostgreSQL (servicio `postgres`)
*   **Mensaje de bienvenida en `/`**: "Bienvenido a la aplicación con PostgreSQL"
*   **Endpoints Principales:**
    *   `POST /register`: Registra un nuevo usuario.
    *   `POST /login`: Inicia sesión.
    *   `GET /users`: Lista todos los usuarios.
    *   `POST /items`: Crea un nuevo ítem.
    *   `GET /items`: Lista todos los ítems.
    *   `PUT /items/<item_id>`: Actualiza un ítem.
    *   `DELETE /items/<item_id>`: Elimina un ítem.

## Autor
*   **EstebanGC222** - [GitHub](https://github.com/EstebanGC222) 

