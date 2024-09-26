Extraer PDF a Excel

Este proyecto contiene un conjunto de herramientas para convertir estados bancarios en formato PDF a archivos Excel. Aunque el proceso no es 100% automatizado, permite realizar conversiones de manera semiautomática con los 5 archivos incluidos.

Características
Conversión eficiente de estados bancarios en PDF a Excel.
Proceso semiautomático para manejar conversiones de manera flexible.
Facilita la gestión y análisis de datos financieros extraídos de estados bancarios.
Requisitos
Python 3.x instalado.
Bibliotecas necesarias: PyPDF2, pandas, openpyxl (u otras que estés utilizando).
Puedes instalar las bibliotecas ejecutando:

bash
Copiar código
pip install PyPDF2 pandas openpyxl
Instrucciones de Uso
Descargar los archivos: Clona o descarga este repositorio en tu máquina local.

bash
Copiar código
git clone https://github.com/TuUsuario/extraer-pdf.git
Colocar los archivos PDF: Coloca los estados bancarios en formato PDF que deseas convertir dentro de la carpeta adecuada (explicar si tienes una carpeta específica).

Ejecutar el script: Ejecuta el archivo principal del script que convierte los archivos PDF a Excel. Dependiendo del archivo que ejecutes, puede ser algo como:

bash
Copiar código
python convertir_pdf_a_excel.py
Revisar el resultado: El archivo Excel generado se almacenará en la carpeta de salida que se especifica en el código.

Personalización
Puedes modificar los scripts según tus necesidades para adaptarlos a otros tipos de documentos PDF o ajustar el formato de salida en Excel.
Limitaciones
El proceso aún requiere algunos pasos manuales para completar la conversión.
Solo compatible con archivos PDF que contienen tablas estructuradas de manera legible por el código.
Contribuciones
¡Las contribuciones son bienvenidas! Si tienes sugerencias, mejoras o encuentras algún error, no dudes en abrir un issue o enviar un pull request.

Licencia
Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo según los términos de la licencia.
