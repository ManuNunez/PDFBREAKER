# PDF BREAKER

## Descripción
Este script en Python proporciona funciones para manipular archivos PDF. Puede unir varios archivos PDF en uno solo o dividir un PDF en partes más pequeñas.

## Requisitos
- Python 3.x
- PyPDF2 (instalable a través de pip: `pip install PyPDF2`)


## Funciones

### `pdfSplitter(input_file, start_page, end_page)`
Esta función divide un archivo PDF en un rango de páginas especificado y guarda las páginas seleccionadas en un nuevo archivo PDF.

#### Parámetros
- `input_file`: Ruta del archivo PDF que se dividirá.
- `start_page`: Página de inicio para la división del PDF.
- `end_page`: Página final para la división del PDF.

### `pdfMerger(input_files, output_file)`
Esta función une varios archivos PDF en uno solo.

#### Parámetros
- `input_files`: Lista de rutas de archivos PDF que se unirán.
- `output_file`: Nombre del archivo PDF de salida que contendrá la fusión de los archivos de entrada.


## Contribución
¡Siéntete libre de contribuir a este proyecto! Si tienes ideas de mejora o encuentras errores, por favor abre un problema o envía una solicitud de extracción.

## Autor
Manuel Nuñez - [GitHub](https://github.com/ManuNunez)
