# Sistema de Gestión de Pedidos y Clientes para el Restaurante "El Buen Sabor".

# Menú del restaurante.
menu = {
    "ensalada cesar": 8.500,
    "pizza": 12.000,
    "hamburguesa": 10.000,
    "spaguetti": 11.500,
    "pollo": 9.000,
    "tacos": 7.500,
    "sopa": 6.000,
    "malteadas": 5.000,
    "torta de chocolate": 7.000,
    "café": 2.000
}

# Función para mostrar el menú.
def mostrar_menu():
    print("\n---- Menú ----")
    for producto, precio in menu.items():
        print(f"{producto.capitalize()}: ${precio:.3f}")
    print("\n")

# Función para registrar un nuevo cliente.
def registrar_cliente(clientes):
    nombre = input("Ingresa el nombre del cliente: ").strip().lower()
    telefono = input("Ingresa el teléfono del cliente: ").strip()
    mesa = input("Ingresa el número de mesa: ").strip()

    # Se almacena la información del cliente en un diccionario.
    clientes[nombre] = {"teléfono": telefono, "mesa": mesa, "pedidos": []}
    print(f"Cliente {nombre.capitalize()} registrado con éxito.")

# Función para agregar un pedido a un cliente existente.
def agregar_pedido(clientes):
    """
    Agrega un pedido a la lista de pedidos de un cliente.
    Verifica si el cliente está registrado antes de agregar el pedido.
    """
    nombre = input("Ingresa el nombre del cliente: ").strip().lower()
    
    if nombre in clientes:
        mostrar_menu()  # Muestra el menú
        while True:
            pedido = input("Ingresa el nombre del producto que deseas agregar (o 'fin' para terminar): ").strip().lower()
            
            if pedido == 'fin':
                break

            if pedido in menu:
                clientes[nombre]['pedidos'].append(pedido)
                print(f"Pedido '{pedido.capitalize()}' agregado para {nombre.capitalize()}.")
            else:
                print("Producto no disponible, por favor elija de la lista.")
    else:
        print("Cliente no encontrado.")

# Función para ver el resumen de pedidos de un cliente específico y generar la factura.
def generar_resumen(clientes):
    """
    Muestra los pedidos de un cliente específico si está registrado.
    También calcula y muestra el total de la factura.
    """
    nombre = input("Ingresa el nombre del cliente para ver el resumen: ").strip().lower()
    
    if nombre in clientes:
        print(f"\nCliente: {nombre.capitalize()} | Mesa: {clientes[nombre]['mesa']}")
        if clientes[nombre]['pedidos']:
            total = 0
            print("Pedidos:")
            for pedido in clientes[nombre]['pedidos']:
                precio = menu[pedido]
                total += precio
                print(f"  - {pedido.capitalize()} - ${precio:.3f}")
            print(f"\nTotal a pagar: ${total:.3f}")
        else:
            print("No hay pedidos para este cliente.")
    else:
        print("Cliente no encontrado.")

# Función para eliminar un pedido de la lista de un cliente.
def eliminar_pedido(clientes):
    """
    Elimina un pedido de la lista de un cliente.
    Verifica si el cliente está registrado y si el índice del pedido es válido.
    """
    nombre = input("Ingresa el nombre del cliente: ").strip().lower()
    
    if nombre in clientes:
        print(f"Pedidos actuales de {nombre.capitalize()}: {clientes[nombre]['pedidos']}")
        # Mostrar lista de pedidos con índices
        for i, pedido in enumerate(clientes[nombre]["pedidos"]):
            print(f"{i}. {pedido.capitalize()}")
        
        indice = int(input("Ingresa el número del pedido que deseas eliminar (0 para el primero): "))
        
        if 0 <= indice < len(clientes[nombre]["pedidos"]):
            eliminado = clientes[nombre]["pedidos"].pop(indice)
            print(f"Pedido '{eliminado.capitalize()}' eliminado.")
        else:
            print("Índice de pedido no válido.")
    else:
        print("Cliente no encontrado.")

# Función para generar el resumen total de todos los pedidos del restaurante.
def generar_resumen_total(clientes):
    """
    Genera el resumen total de todos los pedidos realizados por todos los clientes.
    Calcula el monto total recaudado por el restaurante.
    """
    total_restaurante = 0
    print("\n---- Resumen Total del Restaurante ----")
    
    for cliente, info in clientes.items():
        if info['pedidos']:
            total_cliente = 0
            print(f"\nCliente: {cliente.capitalize()} | Mesa: {info['mesa']}")
            print("Pedidos:")
            for pedido in info['pedidos']:
                precio = menu[pedido]
                total_cliente += precio
                print(f"  - {pedido.capitalize()} - ${precio:.3f}")
            print(f"Total de {cliente.capitalize()}: ${total_cliente:.3f}")
            total_restaurante += total_cliente
    
    print(f"\nMonto total recaudado por el restaurante: ${total_restaurante:.3f}")

# Función principal que muestra el menú y llama a las funciones correspondientes.
def menu_principal():
    """
    Menú principal del sistema de gestión de clientes y pedidos.
    Ofrece las opciones para registrar clientes, agregar pedidos, ver y eliminar pedidos, y generar resúmenes.
    """
    clientes = {}  # Diccionario para almacenar los datos de los clientes

    while True:
        print("\n---- Menú Principal ----")
        print("1. Registrar Cliente")
        print("2. Agregar Pedido")
        print("3. Ver Resumen de Pedidos y Factura")
        print("4. Eliminar Pedido")
        print("5. Generar Resumen Total")
        print("6. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == "1":
            registrar_cliente(clientes)
        elif opcion == "2":
            agregar_pedido(clientes)
        elif opcion == "3":
            generar_resumen(clientes)
        elif opcion == "4":
            eliminar_pedido(clientes)
        elif opcion == "5":
            generar_resumen_total(clientes)
        elif opcion == "6":
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el menú principal cuando se inicia el programa
if __name__ == "__main__":
    menu_principal()
