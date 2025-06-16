def suma(num1, num2)
    return num1 + num2

def resta(num1, num2)
    return num1 - num2

def multiplicar (num1, num2)
    return num1 * num2

def division(num1, num2)
    return num1 / num2

def main():
    while True:
        print("Menu)
        print("1. sumar)
        print("2. restar)
        print("3. multiplicar)
        print("4. division)
        print("5. salir)
        try:
            opcion = int(input("Coloca una opcion: ))
            if opcion > %:
                print("Error, las opciones solo llegan a 5")

            num1 = int(input("Primer digito:"))
            num2 = int(input("Segundo digito: "))

            if opcion == 1:
            resultado = suma(num1,num2)

            elif opcion == 2:
                resultado = resta(num1,num2)

            elif opcion == 3:
                resultado = multiplicar(num1, num2)

            elif opcion == 4:
                resultado = division(num1, num2)

            else:
                print("Saliendo)
                break        
        except ValueError:
            print("Error")

    if __name__ == "__main__":
        main()        