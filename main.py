def saludar():
    nombre = input("Por favor, ingresa tu nombre: ")
    return f"Hola {nombre}, bienvenido"

def contador_numeros(numero):
    if numero < 1:
        print("Por favor, ingresa un número entero positivo.")
        return
    for i in range(1, numero + 1):
        print(i)

def calculadora(num1:float, num2:float,operacion):
    if operacion == '+':
        return f"La operacion seleccionada es suma y el resultado es: {num1 +num2}"
    elif operacion == '-':
        return f"La operacion seleccionada es resta y el resultado es: {num1 -num2}"
    elif operacion == '*':
        return f"La operacion seleccionada es multiplicacion y el resultado es: {num1 *num2}"
    elif operacion == '/':
        return f"La operacion seleccionada es division y el resultado es: {num1 /num2}"
    else:
        return "Error al seleccionar los numeros y la operacion"

if __name__ == "__main__":

    opciones=input("Por favor, ingresa la funcion que deseas utilizar: saludo, contador, calculadora: " )
    if opciones == "saludo":
        print(saludar())
    elif opciones == "contador":
        try:
            numero = int(input("Ingresa un número entero positivo: "))
            contador_numeros(numero)
        except ValueError:
            print("Por favor, ingresa un número entero válido: ")
    elif opciones == "calculadora":
        numero1 = int(input("Ingresa el numero 1: "))
        numero2 = int(input("Ingresa el numero 2: "))
        operacion = input("Ingresa la operacion a utilizar en la calculadora (+,-,/,*): ")
        print(calculadora(numero1, numero2, operacion))






