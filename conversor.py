## Monica Salvatierra
## Derek Arreaga

def complemento1(binario):
    digitos = list(binario)
    
    negativo = False
    # si el primer dígito es 1, es negativo, sino se regresa igual
    if digitos[0] == "1":
        negativo = True

    if negativo:
        #Invierte los dígitos
        for i in range(len(digitos)):
            if digitos[i] == "0":
                digitos[i] = "1"
            else:
                digitos[i] = "0"

    # Convertir la lista de dígitos a una cadena y devolverla
    return ''.join(digitos)

def complemento2(binario):
    digitos = list(binario)

    negativo = False
    if digitos[0] == "1":
        negativo = True

    if negativo:
        for i in range(len(digitos)):
            if digitos[i] == "0":
                digitos[i] = "1"
            else:
                digitos[i] = "0"
        carry = 1
        for i in range(len(digitos)-1, -1, -1):
            if digitos[i] == '0':
                digitos[i] = '1'
                carry = 0
                break
            else:
                digitos[i] = '0'
        if carry == 1:
            digitos.insert(0, '1')

    # Convertir la lista de dígitos a una cadena y devolverla
    return ''.join(digitos)


#HEXADECIMAL A DECIMAL
def HexaDec(hexadecimal):
    decimal = int(hexadecimal,16)
    return decimal

#DECIMAL A HEXADECIMAL
def DecHexa(decimal):
    hexadecimal = hex(decimal)
    return hexadecimal

while True:
    print("Menú:")
    print("1. Binario a Complemento A1 y Complemento A2")
    print("2. Hexadecimal a Decimal")
    print("3. Decimal a Hexadecimal")
    print("4. Salir")

    opcion = input("Ingrese una opción: ")

    if opcion == "1":
        print("Seleccionaste la opción 1")
        binario = input("Ingrese su binario a convertir")
        print("El número en binario: "+ binario +" convertido a complemento A 1 es ---> "+complemento1(binario))
        print("El número en binario: "+ binario +" convertido a complemento A 2 es ---> "+complemento2(binario))
    elif opcion == "2":
        print("Seleccionaste la opción 2")
        hexadecimal = input("Ingrese el número en Hexadecimal de 3 dígitos a convertir")
        print("El número hexadecimal: "+ hexadecimal +" convertido a decimal es ---> "+ str(HexaDec(hexadecimal)))
    elif opcion == "3":
        print("Seleccionaste la opción 3")
        decimal = int(input("Ingrese el número en decimal para convertir a Hexadecimal de 3 dígitos"))
        print("El número en decimal: "+ str(decimal) +" convertido a hexadecimal es ---> "+ DecHexa(decimal))
    elif opcion == "4":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida. Por favor ingrese una opción válida.")
