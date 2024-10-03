# **Extraer PDF a Excel**

Este proyecto contiene un conjunto de herramientas para convertir estados bancarios en formato PDF a archivos Excel. Aunque el proceso no es 100% automatizado, permite realizar conversiones de manera semiautomática con los 5 archivos incluidos.

## **Características**
- Conversión eficiente de estados bancarios en PDF a Excel.
- Proceso semiautomático para manejar conversiones de manera flexible.
- Facilita la gestión y análisis de datos financieros extraídos de estados bancarios.

## **Requisitos**
- **Python 3.x** instalado.
- **Bibliotecas necesarias**: `pdfplumber`, `pandas` (u otras que estés utilizando).

# **Instrucciones de uso**

1. Descargar los archivos: Clona o descarga este repositorio en tu máquina local.
  git clone https://github.com/dimasgb10/extraer-pdf.git

2. la carpeta extraer-pdf consiste de 6 archivos en total, pero 5 de ellos estan en orden numerico. El primer archivo "01unirPDF.py" es para unir los archivos pdf del extracto bancario por ejemplo (si es necesario unir los PDF)
 
3. El segundo archivo "02app.py" se usa para transformar todo el pdf en un archivo TXT, yo realizo este paso, para poder eliminar todas las letras y lineas que no me interesan que vayan en mi archivo de excel

4. el tercer archivo "03eliminadolineas.py" es para eliminar todos los espacios en blanco del documento txt, y asi poder tener un archivo consecutivo sin espacios (todo esto para acoplar el txt y poder llevarlo a excel de la mejor manera), en este paso es vital que ubiquen una coma segun cada celda que requieran ejemplo: el txt viene: 01/09/2024    646464646464   Debito   300,00   1200,00. Van a ubicar la coma por ejemplo asi: 01/09/2024  ,  646464646464  , Debito ,  300,00   1200,00. Estas comas son para indicar al codigo mas adelante que son para las celdas ejemplo: 01/09/2024 en una celda, 64646464646 en otra celda, y asi sucesivamente.

5. el cuarto archivo "04replace_space_with_comma" es para poder ubicar una coma entre los saldos y los montos que ingresaron o egresaron, aqui ya depende de como salga su extracto bancario.

6. Finalmente el quinto archivo, se usa para transformar a excel, pero aun no termina el procedimiento. Puesto que la transformacion no pone las comas para separar los decimales, por ende todavia haria falta ubicar las comas, pero eso se hace facilmente en VSCODE.

Generalmente este proceso no me demora mas de 10 minutos, y gracias a esto puedo tener el extracto bancario en EXCEL y poder generar tablas dinamicas y manipular la data mucho mejor que en el excel, ahorrandome mucho trabajo.

## **Personalización**
Puedes modificar los scripts según tus necesidades para adaptarlos a otros tipos de documentos PDF o ajustar el formato de salida en Excel.

## **Limitaciones**
El proceso aún requiere algunos pasos manuales para completar la conversión..
Solo compatible con archivos PDF que contienen tablas estructuradas de manera legible por el código.

## **Contribuciones**
¡Las contribuciones son bienvenidas! Si tienes sugerencias, mejoras o encuentras algún error, no dudes en abrir un issue o enviar un pull request.

## **Licencia**
Este proyecto está bajo la licencia MIT. Puedes usarlo y modificarlo según los términos de la licencia.


Puedes instalar las bibliotecas ejecutando:
```bash
pip install pdfplumber pandas openpyxl
```

# Muchas Gracias!!


