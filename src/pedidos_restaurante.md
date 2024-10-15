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
### Pseudocódigo:
``` 
Inicio
   Mostrar menú principal
   Mientras la opción no sea "Salir"
      Si opción = "Registrar Cliente"
         Pedir datos del cliente (nombre, teléfono, mesa)
         Almacenar datos en el diccionario de clientes
      Si opción = "Agregar Pedido"
         Pedir nombre del cliente
         Si el cliente existe
            Pedir detalles del pedido
            Agregar pedido a la lista de pedidos del cliente
         Si no
            Mostrar mensaje de "Cliente no encontrado"
      Si opción = "Ver Resumen"
         Pedir nombre del cliente
         Si el cliente existe
            Mostrar la lista de pedidos del cliente
         Si no
            Mostrar mensaje de "Cliente no encontrado"
      Si opción = "Eliminar Pedido"
         Pedir nombre del cliente
         Si el cliente existe
            Mostrar lista de pedidos
            Pedir cuál pedido eliminar
            Eliminar el pedido de la lista del cliente
         Si no
            Mostrar mensaje de "Cliente no encontrado"
      Si opción = "Generar Resumen Total"
         Mostrar resumen de todos los clientes y sus pedidos
   Fin mientras
Fin 
```