# "EL BUEN SABOR" - SISTEMA DE GESTIÓN DE CLIENTES Y PEDIDOS
Este proyecto consiste en la creación de un sistema de gestión de pedidos y clientes para un restaurante. El programa permitirá registrar clientes, gestionar sus pedidos y obtener resúmenes de ventas diarias, ayudando a mejorar la eficacia y organización del restaurante.
La gestión eficiente de pedidos y clientes es esencial para asegurar un servivio fluido en un restaurante, la automatización de la gestión de clientes y pedidos mejora significativamente el servicio. Este programa asegura que los pedidos estén bien organizados, reduciendo errores y mejorando la satisfacción del cliente.
### Alcance:
1. Registro de clientes con sus datos básicos (nombre, teléfono, mesa).
2. Gestión de pedidos asociados a cada cliente.
3. Posibilidad de actualizar o eliminar pedidos.
4. Visualización de pedidos por cliente.
5. Resumen total del día (clientes atendidos, pedidos realizados y monto total de los pedidos).
### Estructuras de datos utilizadas:
1. Diccionarios: Para almacenar los datos de los clientes y sus pedidos asociados.
2. Listas: Para almacenar los pedidos y detalles de cada cliente.
3. Diccionario para el menú: Un diccionario para almacenar los nombres de los productos y sus precios.
### Pseudocódigo:
```
Inicio
   Definir un diccionario vacío para almacenar clientes
   Definir un menú de restaurante con platillos y precios

   Mostrar menú principal
   Mientras la opción no sea "Salir":
      Imprimir "1. Registrar Cliente"
      Imprimir "2. Agregar Pedido"
      Imprimir "3. Ver Resumen"
      Imprimir "4. Eliminar Pedido"
      Imprimir "5. Generar Resumen Total"
      Leer opción

      Si opción = "Registrar Cliente":
         Pedir datos del cliente (nombre, teléfono, mesa)
         Almacenar datos en el diccionario de clientes
         Imprimir "Cliente registrado con éxito"

      Si opción = "Agregar Pedido":
         Pedir nombre del cliente
         Si el cliente existe:
            Mostrar el menú de platillos
            Pedir detalles del pedido (nombre del platillo)
            Agregar el pedido a la lista de pedidos del cliente
            Imprimir "Pedido agregado"
         Si no:
            Mostrar mensaje "Cliente no encontrado"

      Si opción = "Ver Resumen":
         Pedir nombre del cliente
         Si el cliente existe:
            Mostrar la lista de pedidos del cliente
            Calcular el total de los pedidos
            Imprimir "Total a pagar: [total]"
         Si no:
            Mostrar mensaje "Cliente no encontrado"

      Si opción = "Eliminar Pedido":
         Pedir nombre del cliente
         Si el cliente existe:
            Mostrar lista de pedidos
            Pedir cuál pedido eliminar
            Eliminar el pedido de la lista del cliente
            Imprimir "Pedido eliminado"
         Si no:
            Mostrar mensaje "Cliente no encontrado"

      Si opción = "Generar Resumen Total":
         Para cada cliente en el diccionario de clientes:
            Mostrar el nombre del cliente y sus pedidos
            Calcular y mostrar el total a pagar por cada cliente

   Fin Mientras
   Imprimir "Saliendo del programa... Gracias por utilizar el sistema."
Fin
```