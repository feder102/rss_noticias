## Descripción

El siguiente código en pyhton nos permite generar un bot que nos parsea las noticias RSS de un canal y nos las enviá por Telegram.
El proyecto ademas cuenta con un archivo Dockerfile que nos permite crear una imagen apartir de la imagen *public.ecr.aws/lambda/python:3.9* y  dentro de la misma corre los requerimientos que necesitamos en el proyecto.
Dentro de AWS se crear una funcion Lambda utilizando la opcion de image contenedor ( no es necesaria para el uso del bot)

## Instalación

Descargamos el repositorio y hacemos un cp del archivo template (config_template.py)

```bash
cp config_template.py config.py
```

Dentro del archivo *config.py* cambiamos las variables que para nuestro primer caso solo nos interesa *TOKEN* y *CHAT_ID*

```python
TOKEN = '49283742SDFSDFSDF32984723894'
CHAT_ID = -10097429837498
```

## Contribuciones
Los pull request son siempres bienvenidos. Abierto a mejoras! 

## Aportes para el proyecto

Si queres colaborar con lo minimo te dejo mis billeteras
Binance Smart Chain BUSD (BEP20) ??
- 0x883e6c8d5dbbe8fde3c232b3282028dc010d1bc2
Lemon Tag (ARG) ??
- $fcastiglione
CVU (ARG)
- 0000168300000004143358

# GRACIAS ?? 