# no-mas-hambre-server
Un servidor basado en Django 3.0 sobre una DB PostgreSQL

# Setup Development
- Instalar [Docker](https://docs.docker.com/engine/install/)
- Instalar Python 3.8. Se recomienda instalar mediante un ambiente de [Conda](https://docs.conda.io/projects/conda/en/latest/user-guide/install/index.html)
- Instalar (Poetry)[https://python-poetry.org/docs/#installation]
- Abrir terminal en la raíz del proyecto y correr
```
docker-compose --f .\docker-compose-dev.yml up --build -d
```
- Activar ambiente de conda
```
conda activate PYTHON_ENV_NAME
```
- Activar shell de poetry
```
poetry shell
```
- Actualizar migraciones en base de datos
```
python web/app/manage.py migrate
```
- Luego, crear un superusuario corriendo el comando
```
python web/app/manage.py createsuperuser
```
- Seguir instrucciones
- Correr servidor de desarrollo con
```
python web/app/manage.py runserver PORT
```

# Setup production
- Instalar [Docker](https://docs.docker.com/engine/install/)
- 
- Abrir terminal en la raíz del proyecto y correr
```
docker-compose up --build -d
```
- Abrir terminal en container de servidor
```
docker-compose exec -ti web bash
```
- Actualizar migraciones en base de datos
```
python web/app/manage.py migrate
```
- Luego, crear un superusuario corriendo el comando
```
python web/app/manage.py createsuperuser
```
- Salir de terminal
```
exit
```
