
def binario_a_decimal(binario):
  # Extraer los campos del formato IEEE 754
  signo = binario[0]
  exponente = binario[1:9]
  mantisa = binario[9:]

  # Convertir el exponente a decimal
  exponente_decimal = int(exponente, 2) - 127

  # Convertir los .decimales a dec
  mantisa_decimal = 0.0
  for i, bit in enumerate(mantisa):
    mantisa_decimal += int(bit) * 2**(-i-1)

  # Calcular el número decimal
  numero_decimal = (-1)**int(signo) * (1 + mantisa_decimal) * 2**exponente_decimal

  return numero_decimal

def decimal_a_binario(decimal):
    # Manejo de casos especiales
    if decimal == 0:
        return '0' * 32  # Para el caso de 0.0

    # Manejo del signo
    signo = '0' if decimal >= 0 else '1'
    decimal = abs(decimal)

    # Obtener la representación binaria de la parte entera y la parte fraccionaria
    parte_entera_bin = bin(int(decimal))[2:]
    parte_fraccionaria_bin = ''

    # Calcular la parte fraccionaria binaria
    parte_decimal = decimal - int(decimal)
    while parte_decimal > 0:
        parte_decimal *= 2
        parte_fraccionaria_bin += str(int(parte_decimal))
        parte_decimal -= int(parte_decimal)

    # Longitud de la parte entera binaria (sin el 1 implícito)
    longitud_parte_entera = len(parte_entera_bin)

    # Calcular el exponente en binario
    exponente_bin = bin(127 + longitud_parte_entera - 1)[2:].zfill(8)

    # Calcular la mantisa
    mantisa = parte_entera_bin[1:] + parte_fraccionaria_bin
    mantisa = mantisa.ljust(23, '0')[:23]  # Ajustar la longitud a 23 bits

    # Combinar todos los componentes
    numero_binario = signo + exponente_bin + mantisa

    return numero_binario


def menu():
    while True:
        print("\nMenú:")
        print("1. Convertir decimal a binario IEEE 754")
        print("2. Convertir binario IEEE 754 a decimal")
        print("3. Salir")

        opcion = input("Selecciona una opción (1/2/3): ")

        if opcion == '1':
            decimal = float(input("Ingresa el número decimal: "))
            binario = decimal_a_binario(decimal)
            print(f'El número binario IEEE 754 para {decimal} es: {binario}')
        elif opcion == '2':
            binario = input("Ingresa el número binario IEEE 754: ")
            decimal = binario_a_decimal(binario)
            print(f'El número decimal para {binario} es: {decimal}')
        elif opcion == '3':
            print("salkir")
            break
        else:
            print("error")

menu()

"""
pruebas
numero_binario = "11000001000000000000000000000010"
numero_decimal = binario_a_decimal(numero_binario)
print(f"Número binario: {numero_binario}")
print(f"Número decimal: {numero_decimal}")

numero_decimal = -8.000001907348633
numero_binario = decimal_a_binario(numero_decimal)
print(f"Número decimal: {numero_decimal}")
print(f"Número binario: {numero_binario}")
"""


