class AnimalCRUD:
    def __init__(self):
        self.animales = []
    
    def agregar_animal(self, nombre, especie, edad):
        self.animales.append((nombre, especie, edad))
        print(f"Animal {nombre} agregado correctamente.")
    
    def mostrar_animales(self):
        if not self.animales:
            print("No hay animales registrados.")
        else:
            print("Lista de animales:")
            for idx, (nombre, especie, edad) in enumerate(self.animales, 1):
                print(f"{idx}. Nombre: {nombre}, Especie: {especie}, Edad: {edad} años")
    
    def actualizar_animal(self, index, nuevo_nombre, nueva_especie, nueva_edad):
        if 0 <= index < len(self.animales):
            self.animales[index] = (nuevo_nombre, nueva_especie, nueva_edad)
            print("Animal actualizado correctamente.")
        else:
            print("Índice inválido.")
    
    def eliminar_animal(self, index):
        if 0 <= index < len(self.animales):
            eliminado = self.animales.pop(index)
            print(f"Animal {eliminado[0]} eliminado correctamente.")
        else:
            print("Índice inválido.")
    
    def ordenar_animales(self, criterio):
        if criterio == "nombre":
            self.animales.sort(key=lambda x: x[0])
        elif criterio == "especie":
            self.animales.sort(key=lambda x: x[1])
        elif criterio == "edad":
            self.animales.sort(key=lambda x: x[2])
        else:
            print("Criterio no válido.")
            return
        print(f"Animales ordenados por {criterio} correctamente.")
    
# Ejecución del menú
crud = AnimalCRUD()
while True:
    print("\nMenú CRUD de Animales")
    print("1. Agregar Animal")
    print("2. Mostrar Animales")
    print("3. Actualizar Animal")
    print("4. Eliminar Animal")
    print("5. Ordenar Animales")
    print("6. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del animal: ")
        especie = input("Ingrese la especie del animal: ")
        edad = int(input("Ingrese la edad del animal: "))
        crud.agregar_animal(nombre, especie, edad)
    elif opcion == "2":
        crud.mostrar_animales()
    elif opcion == "3":
        crud.mostrar_animales()
        index = int(input("Ingrese el número del animal a actualizar: ")) - 1
        nombre = input("Nuevo nombre: ")
        especie = input("Nueva especie: ")
        edad = int(input("Nueva edad: "))
        crud.actualizar_animal(index, nombre, especie, edad)
    elif opcion == "4":
        crud.mostrar_animales()
        index = int(input("Ingrese el número del animal a eliminar: ")) - 1
        crud.eliminar_animal(index)
    elif opcion == "5":
        criterio = input("Ingrese el criterio de ordenamiento (nombre, especie, edad): ")
        crud.ordenar_animales(criterio)
    elif opcion == "6":
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida, intente nuevamente.")
