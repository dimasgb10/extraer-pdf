import pandas as pd
import re

# Ruta del archivo TXT original y la ruta de salida del archivo Excel
input_path = "C:\\Users\\dimas\\Downloads\\VENEZUELA_JOSE_LUIS_SIN_LINEAS_CON_COMAS.txt"
output_path = "C:\\Users\\dimas\\Downloads\\VENEZUELA_JOSE_LUIS_SIN_LINEAS_CON_COMAS.xlsx"

# Función para reemplazar las comas en los números decimales por puntos temporales
def replace_commas_in_decimals(line):
    return re.sub(r'(\d+),(\d+)', r'\1.\2', line)

# Crear una copia temporal del archivo con las comas en los decimales reemplazadas por puntos
with open(input_path, 'r') as infile:
    lines = infile.readlines()

# Reemplazar las comas en los números decimales por puntos temporales
modified_lines = [replace_commas_in_decimals(line) for line in lines]

# Guardar el archivo temporal modificado
temp_path = 'C:/Users/dimas/Documents/temp_modificado.txt'
with open(temp_path, 'w') as temp_file:
    temp_file.writelines(modified_lines)

# Leer el archivo temporal en un DataFrame
df = pd.read_csv(temp_path, sep=r'\s*,\s*', header=None, engine='python', skipinitialspace=True, quoting=3)

# Asignar nombres a las columnas (ajusta estos nombres según tus datos)
df.columns = ['Fecha', 'Numero', 'Tipo', 'Monto', 'Saldo']

# Convertir columnas 'Monto' y 'Saldo' de nuevo a formato numérico adecuado
df['Monto'] = df['Monto'].astype(str).str.replace('.', '').str.replace(',', '.').astype(float)
df['Saldo'] = df['Saldo'].astype(str).str.replace('.', '').str.replace(',', '.').astype(float)

# Guardar el DataFrame como un archivo Excel
df.to_excel(output_path, index=False, float_format="%.2f")

print(f'El archivo ha sido guardado en formato Excel en {output_path}')
