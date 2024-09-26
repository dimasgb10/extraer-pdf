# Nombre del archivo de entrada y salida
input_file = "C:\\Users\\dimas\\Downloads\\VENEZUELA_JOSE_LUIS.txt"
output_file = "C:\\Users\\dimas\\Downloads\\VENEZUELA_JOSE_LUIS_SIN_LINEAS.txt"

# Abrir el archivo de entrada para lectura y el de salida para escritura
with open(input_file, 'r', encoding='utf-8') as file_in, open(output_file, 'w', encoding='utf-8') as file_out:
    # Leer todas las líneas del archivo de entrada
    lines = file_in.readlines()

    # Iterar sobre las líneas y escribir en el archivo de salida sin espacios en blanco entre líneas
    for line in lines:
        line = line.strip()  # Eliminar espacios en blanco al inicio y final de la línea
        if line:  # Si la línea no está vacía después de quitar los espacios en blanco
            file_out.write(line + '\n')  # Escribir la línea en el archivo de salida

print(f'Se han eliminado los espacios en blanco entre líneas. Puedes encontrar el resultado en {output_file}')
