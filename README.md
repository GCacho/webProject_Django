# Complete Django Project
## Guía para la Instalación de Requerimientos y Configuración - Ubuntu 22.04.1 LTS WSL2
___
### Instalación de Paquetes y Requerimientos
- Instalar Actualizaciones de librerias Linux y Python
~~~
    - sudo apt-get update 
    - sudo apt-get upgrade
    - sudo apt-get install python3-pip
    - python3 -m pip install --upgrade pip
    - sudo apt-get install python3-venv
~~~
- Instalar y Activar Ambiente Virtual en la carpeta Raíz (venv)
~~~
    - python3 -m venv venv
    - source venv/bin/activate
~~~
- Instalar Django y Requirements
~~~
    - pip install -r requirements.txt
~~~
- Instalación y Configuración Básica PostgreSQL
~~~
    - sudo apt-get -y install postgresql
    - psql --version
    - sudo passwd postgres
~~~
### Comandos PostgreSQL
- Correr y Verificar Servicio PostgreSQL
~~~
    - sudo service postgresql start
    - sudo service postgresql stop
    - sudo service postgresql status
~~~
- Ingresar a PostgreSQL Shell, Asignar Password y Crear Base de Datos
~~~
    - su postgres
    - psql
    - alter user postgres password 'YourPassword';
    - CREATE DATABASE yourdatabase;
    - (Tanto el usuario como la contraseña y la base de datos deben coincidir con los asignados en el archivo settings.py en la carpeta de webProject)
    - Ctrl + D -> para salir de consola PostgreSql.
~~~
___
### Comandos Django
- Iniciar Proyecto y Aplicaciones Django.
~~~
    - django-admin startproject webProject
    - python3 manage.py startapp webProjectApp
~~~
- Correr Servidor Python
~~~
    - python3 manage.py runserver
~~~
- Hacer migraciones de modelos a base de datos
~~~
    - python3 manage.py makemigrations
    - python3 manage.py sqlmigrate orders 0001 (por si aparece un error)
    - python3 manage.py migrate
~~~
- Crear SuperUsuario
~~~
    - python3 manage.py createsuperuser
~~~
- Ingresar a la Shell
~~~
    - python3 manage.py shell
~~~
Citas:
> Proyecto realizado con ayuda del Maestro Juan D. del canal Pildoras Informáticas: https://youtu.be/1DSi4in2VNA