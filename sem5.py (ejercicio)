lista_clientes = [
    ["nelson", "rincon", "112473321"],
    ["juan", "marquez", "32581236"],
    ["maria", "perez", "1232443"]
]

def mostrar_clientes():
    print("Lista de Clientes:")
    for i, cliente in enumerate(lista_clientes):
        print(f"{i + 1}. Nombre: {cliente[0]}, Apellido: {cliente[1]}, Cédula: {cliente[2]}")

def agregar_cliente():
    nombre = input("Ingrese el nombre: ")
    apellido = input("Ingrese el apellido: ")
    cedula = input("Ingrese la cédula: ")
    lista_clientes.append([nombre, apellido, cedula])
    print("Cliente agregado exitosamente.")

def eliminar_cliente():
    mostrar_clientes()
    try:
        indice = int(input("Ingrese el número del cliente a eliminar: ")) - 1
        if 0 <= indice < len(lista_clientes):
            lista_clientes.pop(indice)
            print("Cliente eliminado correctamente.")
        else:
            print("Número inválido.")
    except ValueError:
        print("Entrada no válida.")

def buscar_cliente():
    cedula = input("Ingrese la cédula del cliente a buscar: ")
    encontrado = False
    for cliente in lista_clientes:
        if cliente[2] == cedula:
            print(f"Cliente encontrado: Nombre: {cliente[0]}, Apellido: {cliente[1]}, Cédula: {cliente[2]}")
            encontrado = True
            break
    if not encontrado:
        print("Cliente no encontrado.")

def menu():
    while True:
        print("\nMenú Principal:")
        print("1. Mostrar clientes")
        print("2. Agregar cliente")
        print("3. Eliminar cliente")
        print("4. Buscar cliente por cédula")
        print("5. Salir")
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            mostrar_clientes()
        elif opcion == "2":
            agregar_cliente()
        elif opcion == "3":
            eliminar_cliente()
        elif opcion == "4":
            buscar_cliente()
        elif opcion == "5":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")

menu()
