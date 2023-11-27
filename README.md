# Precipitacion_Mx_Explorer_Tool

Bienvenido a la **Herramienta de exploración de Precipitación México (1985-2022)**. Este proyecto proporciona una herramienta para explorar datos de precipitación en México.

## Descripción

Este repositorio contiene una aplicación para visualizar y analizar datos de precipitación en distintas regiones de México. La herramienta utiliza datos meteorológicos para generar gráficos interactivos y facilitar la comprensión de los patrones de precipitación a lo largo del tiempo.
![W](https://github.com/victortg95/Precipitacion_Mx_Explorer_Tool/blob/master/src/static/working.gif)

## Características

- **Visualización Interactiva:** Explora datos de precipitación a través de gráficos interactivos y mapas.
- **Filtros Personalizados:** Personaliza la visualización mediante filtros de fecha y ubicación geográfica.
- **Consulta en ChatGPT:** Consulta en ChatGPT eventos meteorológicos relevantes en la fecha deseada.

## Requisitos

- Python 3.x
- Bibliotecas Python (se proporciona un archivo `requirements.txt`)

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/victortg95/Precipitacion_Mx_Explorer_Tool.git
    ```

2. Accede al directorio del proyecto:

    ```bash
    cd Precipitacion_Mx_Explorer_Tool
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta la aplicación:

    ```bash
    cd src/
    flask --app app run
    ```

2. Abre tu navegador y accede a [http://127.0.0.1:5000](http://127.0.0.1:5000).

3. Para realizar consultas con la herramienta de ChatGPT se requiere una **API Key**.



## Licencia

Este proyecto está bajo la Licencia [MIT](LICENSE).
