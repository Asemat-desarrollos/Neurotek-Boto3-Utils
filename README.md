# Boto3 Utils

> [!IMPORTANT]  
> No se recomienda hacer _push_ directamente a la rama `main`. Existe un flujo de trabajo para contribuir a este proyecto, que testea y valida los cambios antes de ser integrados en la rama principal. Por favor, sigue las instrucciones de [Contribución](#contribución) para contribuir a este proyecto.

Este repositorio contiene utilidades para trabajar con Boto3. Está pensado para ser publicado como un paquete de Python, alojado y publicado en GitHub.

## Instalación de dependencias de desarrollo

```bash
poetry install --with dev,test
```

## Build

Solo instala [poetry](https://python-poetry.org/docs/) y ejecuta:

```bash
poetry build
```

## Instalación del paquete

Para instalar el paquete recién creado, simplemente ejecuta:

```bash
poetry install
```

Desde la raíz del proyecto.

## Contribución

Este proyecto está configurado para ejecutar pruebas en GitHub Actions. Puedes ver el estado de las pruebas en la pestaña "Actions" de este repositorio.

Si desea contribuir a este proyecto, crea un Pull Request con tus cambios. Asegúrate de que todos los jobs de GitHub Actions pasen antes de solicitar la revisión de tu Pull Request.
