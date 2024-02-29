def saludar():
    nombre = input("Por favor, ingresa tu nombre: ")
    return f"Hola {nombre}, bienvenido"

def contador_numeros(numero):
    if numero < 1:
        print("Por favor, ingresa un número entero positivo.")
        return
    for i in range(1, numero + 1):
        print(i)

if __name__ == "__main__":
    try:
        numero = int(input("Ingresa un número entero positivo: "))
        contador_numeros(numero)
    except ValueError:
        print("Por favor, ingresa un número entero válido.")






