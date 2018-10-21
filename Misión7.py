# Autor: Luisa Fernanda Arellano Alvarado A01377974
# Misión 07 ciclos con while

def dividir(divisor, dividendo):
    valor = 0 # acumulador
    numero = 0
    while dividendo - divisor >= valor: # Mientras la diferencia del divisor y el dividendo sea mayor o igual al divisor el programa seguira restando valores
        numero = numero + 1
        valor = divisor * numero
    print(dividendo,"/", divisor,"=",numero,"sobra",dividendo-valor)


def encontrarMayor():

    print("Teclea una serie de numeros para encontrar el mayor")
    NumMayor = 0 # acumulador
    valores = int(input("Teclea un número [-1 para salir]:"))
    if valores == -1 or valores <= 0: # si los valores que el usuario teclea se encuentran entre -1 y 0 le aparecera el siguiente mensaje en la pantalla
        print("No tengo suficiente información")


    else: # si no ejecutara esta instrucción, el usuario teclea los numeros que quiere y al finalizar el codigo le lanza el mayor de estos

        while valores != -1:
            if valores > NumMayor:

                NumMayor = valores
            valores = int(input("Teclea un número [-1 para salir]:"))
        print("El mayor es:", NumMayor)

def menu():
    print("Misión 07. Ciclos while")
    print("Autor: Luisa Fernanda Arellano Alvarado ")
    print("Matricula: A01377974")
    print("1. Calcular divisiones ")
    print("2. Encontrar el mayor ")
    print("3. salir")
    opcion = int(input("Teclea tu opción:"))
    return opcion

def main():
# mientras el usario no quiera salirse del programa (opción 3) podra jugar con la 1 y 2 con sus diversos componentes
    opcion = menu()
    while opcion != 3:
        if opcion == 1:
            dividendo = int(input("Teclea un número:"))
            divisor = int(input("Teclea otro número: "))
            dividir(divisor, dividendo)
            opcion = menu()

        elif opcion == 2:
            encontrarMayor()
            opcion = menu()
# Si el usuario desea salir
        elif opcion > 3 or opcion <= 0:
            print("Error, teclea 1, 2 o 3")
            opcion = menu()

    print("Gracias por utilizar este programa, regresa pronto")


# llamamos a la funcion
main()