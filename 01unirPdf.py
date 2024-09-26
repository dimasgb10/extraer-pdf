import os
from PyPDF2 import PdfReader, PdfWriter

def merge_pdfs(input_folder, output_path):
    # Crear un objeto PdfWriter que servirá para unir los PDFs
    pdf_writer = PdfWriter()

    # Recorrer todos los archivos en la carpeta de entrada
    for filename in sorted(os.listdir(input_folder)): # trae los archivos PDF segun el orden alfabetico de la carpeta
        if filename.endswith('.pdf'):
            file_path = os.path.join(input_folder, filename)
            
            # Leer el archivo PDF
            pdf_reader = PdfReader(file_path)
            
            # Añadir todas las páginas del PDF al objeto PdfWriter
            for page_num in range(len(pdf_reader.pages)):
                pdf_writer.add_page(pdf_reader.pages[page_num])
    
    # Escribir el archivo PDF resultante
    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

    print(f'PDFs unidos exitosamente en {output_path}')

if __name__ == '__main__':
    # Carpeta que contiene los PDFs a unir
    input_folder = "C:\\Users\\dimas\\Downloads\\vzla_jose_luis"  # Cambia esta ruta a la carpeta donde están tus PDFs
    
    # Ruta del archivo PDF resultante
    output_path = "C:\\Users\\dimas\\Downloads\\VENEZUELA_JOSE_LUIS.pdf"  # Cambia esta ruta al nombre y ubicación que deseas para el PDF unido
    
    merge_pdfs(input_folder, output_path)
