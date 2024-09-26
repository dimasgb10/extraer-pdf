import re

# Ruta del archivo TXT original y la ruta de salida del archivo modificado
input_path = "C:\\Users\\dimas\\Downloads\\VENEZUELA_JOSE_LUIS_SIN_LINEAS.txt"
output_path = "C:\\Users\\dimas\\Downloads\\VENEZUELA_JOSE_LUIS_SIN_LINEAS_CON_COMAS.txt"

# Leer el archivo TXT
with open(input_path, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Función para reemplazar el espacio entre dos valores numéricos con una coma rodeada de tres espacios
def replace_space_with_comma(line):
    # Expresión regular ajustada para manejar valores negativos y formatos numéricos variados
    return re.sub(r'(-?\d{1,3}(?:\.\d{3})*,\d{2})\s+(-?\d{1,3}(?:\.\d{3})*,\d{2})', r'\1   ,   \2', line)

# Procesar cada línea
modified_lines = [replace_space_with_comma(line) for line in lines]

# Guardar el archivo modificado
with open(output_path, 'w', encoding='utf-8') as file:
    file.writelines(modified_lines)

print(f'El archivo ha sido modificado y guardado en {output_path}')
