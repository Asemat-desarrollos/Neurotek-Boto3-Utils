# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['boto3_utils']

package_data = \
{'': ['*']}

install_requires = \
['boto3-stubs>=1.34.116,<2.0.0',
 'boto3>=1.34.116,<2.0.0',
 'botocore-stubs>=1.34.94,<2.0.0',
 'botocore>=1.34.116,<2.0.0',
 'mypy-boto3-s3>=1.34.105,<2.0.0',
 'mypy-boto3-secretsmanager>=1.34.109,<2.0.0',
 'mypy-boto3-stepfunctions>=1.34.92,<2.0.0',
 'poetry2setup>=1.1.0,<2.0.0']

setup_kwargs = {
    'name': 'boto3-utils',
    'version': '1.1.2',
    'description': 'Utilidades para trabajar con Boto3',
    'long_description': '# Boto3 Utils\n\n> [!IMPORTANT]  \n> No se recomienda hacer _push_ directamente a la rama `main`. Existe un flujo de trabajo para contribuir a este proyecto, que testea y valida los cambios antes de ser integrados en la rama principal. Por favor, sigue las instrucciones de [Contribución](#contribución) para contribuir a este proyecto.\n\nEste repositorio contiene utilidades para trabajar con Boto3. Está pensado para ser publicado como un paquete de Python, alojado y publicado en GitHub.\n\n## Instalación de dependencias de desarrollo\n\n```bash\npoetry install --with dev,test\n```\n\n## Build\n\nSolo instala [poetry](https://python-poetry.org/docs/) y ejecuta:\n\n```bash\npoetry build\n```\n\n## Instalación del paquete\n\nPara instalar el paquete recién creado, simplemente ejecuta:\n\n```bash\npoetry install\n```\n\nDesde la raíz del proyecto.\n\n## Contribución\n\nEste proyecto está configurado para ejecutar pruebas en GitHub Actions. Puedes ver el estado de las pruebas en la pestaña "Actions" de este repositorio.\n\nSi desea contribuir a este proyecto, crea un Pull Request con tus cambios. Asegúrate de que todos los jobs de GitHub Actions pasen antes de solicitar la revisión de tu Pull Request.\n\n> ![IMPORTANTE]\n> Antes de publicar una nueva versión, asegúrate de ejecutar `poetry2setup > setup.py` para actualizar el archivo `setup.py` con la información de la versión actualizada.\n',
    'author': 'Adrian Carreno',
    'author_email': 'adriancarreno.d@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)

