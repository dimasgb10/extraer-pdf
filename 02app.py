import pdfplumber

def pdf_to_text(pdf_path, txt_path):
    with pdfplumber.open(pdf_path) as pdf:
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    txt_file.write(text)
                    txt_file.write('\n\n')  # Añade un espacio entre páginas

# Ruta del archivo PDF y la ruta de salida del archivo TXT
pdf_path = "C:\\Users\\dimas\\Downloads\\VENEZUELA_JOSE_LUIS.pdf"
txt_path = "C:\\Users\\dimas\\Downloads\\VENEZUELA_JOSE_LUIS.txt"

pdf_to_text(pdf_path, txt_path)

print(f'El archivo PDF se ha convertido a TXT y se ha guardado en {txt_path}')