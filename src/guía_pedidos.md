# "EL BUEN SABOR" GUÍA DE USUARIO
#### 1. Clonar el repositorio:
- Abrir la terminal o consola de comandos.
- Navega hasta el directorio donde se desea clonar el repositorio.
- Ejecutar el comando: git clone (https://github.com/hacUPB/prog-2420-eval-u3-Maria160306.git).

#### 2. Ejecutar el programa:
- Navegar al directorio del proyecto con: cd "pedidos_restaurante".
- Ejecutar el programa con: "python main.py",
- Esto iniciará el programa y mostrará el menú principal en la terminal.

#### 3. Uso del programa:
1. Registrar Cliente.
Cuando un nuevo cliente llega al restaurante, selecciona la opción 1 para registrar al cliente. Se pedirá que se ingresen los siguientes datos:
- Nombre del cliente.
- Teléfono del cliente.
- Número de mesa.
2. Agregar Pedido.
Una vez registrado el cliente, se agrega uno o varios pedidos a su cuenta seleccionando la opción 2, para agregar un pedido:
- Ingresar el nombre del cliente registrado.
- Seleccionar los productos del menú disponibles para agregar a su pedido.
- Cuando termine de agregar pedidos, escribe fin para finalizar.
3. Ver Resumen de Pedidos y Factura.
Seleccionar la opción 3 para ver los pedidos actuales y generar una factura para un cliente específico. Se mostrará:
- Nombre del cliente y mesa.
- Lista de pedidos realizados.
- El total a pagar por los productos pedidos.
4. Eliminar Pedido.
Si se necesita eliminar un pedido de un cliente, se selecciona la opción 4. Se pedirá:
- Nombre del cliente.
- Eligir el pedido que se desea eliminar seleccionando el número correspondiente.
- El pedido se eliminará y se actualizará la lista de pedidos.
5. Generar Resumen Total.
Para ver un resumen de todos los pedidos realizados en el restaurante durante el turno o el día, se selecciona la opción 5. El programa mostrará:
- Lista de todos los clientes y sus pedidos.
- El total recaudado por el restaurante en base a todos los pedidos realizados.
6. Salir
- Para salir del programa, se selecciona la opción 6. Esto finalizará la ejecución del sistema.

#### 4. Ejemplo de uso:
1. Paso 1: Registrar al Cliente.
- Seleccionas la opción "1. Registrar Cliente".
- Ingresas el nombre del cliente: Ana Pérez.
- Ingresas el número de teléfono: 3128348009.
- Ingresas el número de mesa: 5.
Resultado: El sistema registra al cliente con su información.
2. Paso 2: Agregar un Pedido.
- Seleccionas la opción "2. Agregar Pedido".
- El sistema muestra el menú del restaurante con sus precios.
- El cliente pide una Pizza y una Malteada.
- Ingresas los nombres de los productos uno a uno.
Resultado: El sistema agrega los productos al pedido de Ana.
3. Paso 3: Ver Resumen de Pedido y Factura.
- Seleccionas la opción "3. Ver Resumen de Pedidos y Factura".
- Ingresas el nombre de Ana para ver su pedido.
Resultado: El sistema muestra:
Cliente: Ana Pérez
Mesa: 5
Pedidos: Pizza - $12.000, Malteada - $5.000
Total a pagar: $17.000
4. Paso 4: Finalizar el Pedido.
- Una vez que se genera la factura y se revisa el pedido, el cliente puede pagar y terminar el proceso.
5. Paso 5: Resumen Total.
- Al final del día, seleccionas la opción "5. Generar Resumen Total" para ver el total de ingresos de todos los clientes y pedidos.
Por ejemplo, si "Ana Pérez" fue el único cliente del día, el resumen total mostrará:
Total de ingresos: $17.000
6. Paso 6: Salir.


