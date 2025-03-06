BIENVENIDA = """
Bienvenido al taller de Don Juan.
Este programa gestionar un taller mecanico."""
INVENTARIO = "Estos son tus carros actuales:"
ACCIONES = """
Acciones:
1) Agregar un carro
2) Eliminar un carro
3) Ordenar tus carros
4) Salir
"""
INGRESA_CARRO_AGREGAR = """
Ingresa la marca del carro que deseas agregar: """
INGRESA_CARRO_ELIMINAR = """
Ingresa la marca del carro que deseas eliminar: """
ACTUALIZACION_EXITOSA = """
Inventario actualizado:"""
ENTRADA_INVALIDA = """
Dato inválida."""
DESPEDIDA = """
Gracias por usar el programa.
Espero te haya servido.
Adiós."""


carros = [ "Toyota", "Nissan", "Honda", "Volkswagen", "Chevrolet", "Audi"]

def iniciar_taller():
    print(BIENVENIDA)
    print(INVENTARIO)

    for carro in carros:
        print(carro.title())

    while True:
        print(ACCIONES)
        opc = input("Dime qué opción deseas realizar: ").strip()
        
        if opc == "1":
           
            while True:
                carro = input(INGRESA_CARRO_AGREGAR).strip().lower()
                if carro != "":
                    carros.append(carro)
                    print(ACTUALIZACION_EXITOSA)
                    for carro in carros:
                        print(carro.title())
                    break
                else:
                    print(ENTRADA_INVALIDA)
        elif opc == "2":
            
            while True:
                carro = input(INGRESA_CARRO_ELIMINAR).strip().lower()
                if carro != "":
                    if carro in carros:
                        carros.remove(carro)
                        print(ACTUALIZACION_EXITOSA)
                        for carro in carros:
                            print(carro.title())
                        break
                    else:
                        print("El modelo ingresado no está en el inventario.")
                else:
                    print(ENTRADA_INVALIDA)
        elif opc == "3":
            
            carros.sort()
            print(ACTUALIZACION_EXITOSA)
            for carro in carros:
                print(carro.title())
        elif opc == "4":
            
            print(DESPEDIDA)
            break
        else:
            print(ENTRADA_INVALIDA)

if __name__ == "__main__":
    iniciar_taller()
