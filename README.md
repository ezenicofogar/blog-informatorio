# blog-informatorio

## Cómo iniciar el proyecto

### Comandos generales :pushpin:

Cómo iniciar el proyecto (modo DEBUG).

1. Copiar `.env.example` a `.env`:
    ```sh
    cp .env.example .env
    ```

1. Iniciar servidor de desarrollo (**dentro de tu [`virtualenv`](#pip-y-virtualenv)**):
    ```sh
    python django-project/manage.py runserver
    ```

### `Pip` y `Virtualenv` :memo:

Cómo crear el entorno virtual e instalar las dependencias.

1. Crear `venv`:
    ```sh
    python -m venv venv
    ```

1. **Activar el entorno virtual**:
    - En linux:
        ```sh
        source venv/bin/activate
        ```
    - En windows:
        ```sh
        .\venv\Scripts\activate
        ```

1. Instalar las dependencias:
    ```sh
    pip install -r requirements.txt
    ```

### Usar `pipenv` (alternativa a `venv`) :coffee:

1. Instalar `pipenv`:
    ```sh
    pip install pipenv
    ```

1. Instalar entorno virtual:
    ```sh
    pipenv install
    ```

1. Activar el entorno virtual:
    ```sh
    pipenv shell
    ```
