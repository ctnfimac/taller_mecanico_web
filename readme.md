# Taller Mecánico
Este proyecto busca mejorar la organización de los talleres mecánicos, Para ello el reponsable del taller debera registrarse en la plataforma y una vez tenga una cuenta podrá dar de alta los nuevos autos ingresados a su taller, registrar los trabajos realizados a cada auto y brindar a los clientes un reporte detallado del trabajo realizado


## Tecnologías
- Python 3.10.6
- FastApi
- Django Rest Framework
- Pipenv
- Docker - Docker Compose
- Git

## Arquitectura
- Microservicios 

![Image](https://github.com/user-attachments/assets/adb4ebf2-08e8-45d4-a24c-ff4f76116350)


## Instalación del proyecto

### Requisitos Previos
Contar con las siguientes herramientas antes de la instalación:

- Python
- Pipenv
- Docker - Docker Compose
- Git

## Entorno de desarrollo:

1. Clonar el repositorio y me muevo a la carpeta del proyecto
```bash
git clone https://github.com/ctnfimac/taller_mecanico_web.git
cd taskapp
```

2. Inicio los contenedores de las base de datos y pgadmin:
```bash
docker-compose -f docker-compose.dev.yml up --build -d
```

3. Me posiciono en la carpeta auth-microservice y ejecuto:
```bash
pipenv install #(solo se hace la primera vez para instalar las dependencias)
pipenv shell #(activa el entorno virtual)
uvicorn app.main:app --reload
```

### Documentacion, api auth:
```
http://127.0.0.1:8000/docs
```


