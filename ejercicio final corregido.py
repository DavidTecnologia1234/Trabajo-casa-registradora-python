# Un print sencillo para indicar que se debe poner el numero exacto de clientes
print("Hola bienvenido a la hora pico recuerda que se debe ingresar el numero exacto de clientes que se desea atender")

# Se crea una lista donde se van a guardar los diccionarios de cada cliente
clientes = []

# Otra lista para solo guardar los totales de los clientes
lista_totales = []

# Se pide el numero de pedidos como entero
numero_pedidos = int(input("Ingrese el numero de clientes:"))

# Se define el precio de cada producto
jugo = 10000
tinto = 5000
cafe = 7500
empanada = 3500
almojabana = 4500
#se define la funcion para que nos haga la suma de los datos en la lista
def mostrar_total(lista):

    total = sum(lista)

    print(f"Total de dinero recaudado con todos los pedidos: ${total}")
#funcion para imprimir la lista
def todos_datos(datos):

    print(datos)
# Uso de while porque no se saben cuantos clientes se van a ingresar
while numero_pedidos > 0:

    numero_pedidos = numero_pedidos - 1

    # El total del cliente empieza en 0
    total_cliente = 0

    # Se pide el nombre del cliente
    cliente = str(input("Ingrese el nombre del cliente:"))

    # Se crea un diccionario para guardar los datos de este cliente
    datos_cliente = {
        "nombre": cliente
    }

    # Menu 1: tipo de bebida
    eleccion_menu_1 = int(input("Menu 1 tipo de bebida: Elija 1 para jugo natural($10000), Elija 2 para bebida caliente:"))

    if eleccion_menu_1 == 1:

        # Se guarda la bebida en el diccionario
        datos_cliente["bebida"] = "jugo"
        datos_cliente["precio_bebida"] = jugo

        # Se suma el precio al total
        total_cliente += jugo

        # Menu 2: acompañamiento
        eleccion_menu_2 = int(input("Menu 2 acompañamiento: Elija 1 para una empanada($3500), Elija 2 para una almojabana($4500):"))

        if eleccion_menu_2 == 1:

            datos_cliente["acompanamiento"] = "empanada"
            datos_cliente["precio_acompanamiento"] = empanada

            total_cliente += empanada

        elif eleccion_menu_2 == 2:

            datos_cliente["acompanamiento"] = "almojabana"
            datos_cliente["precio_acompanamiento"] = almojabana

            total_cliente += almojabana

    elif eleccion_menu_1 == 2:

        # Se elige el tipo de bebida caliente
        opcion_2_menu_1 = int(input("Dentro de las bebidas calientes hay dos opciones: Elija 1 para tinto tradicional($5000), Elija 2 para café latte con almendras ($7500):"))

        if opcion_2_menu_1 == 1:

            datos_cliente["bebida"] = "tinto"
            datos_cliente["precio_bebida"] = tinto

            total_cliente += tinto

        elif opcion_2_menu_1 == 2:

            datos_cliente["bebida"] = "cafe"
            datos_cliente["precio_bebida"] = cafe

            total_cliente += cafe

        # Menu 2: acompañamiento
        eleccion_menu_2 = int(input("Menu 2 acompañamiento: Elija 1 para una empanada($3500), Elija 2 para una almojabana($4500):"))

        if eleccion_menu_2 == 1:

            datos_cliente["acompanamiento"] = "empanada"
            datos_cliente["precio_acompanamiento"] = empanada

            total_cliente += empanada

        elif eleccion_menu_2 == 2:

            datos_cliente["acompanamiento"] = "almojabana"
            datos_cliente["precio_acompanamiento"] = almojabana

            total_cliente += almojabana

    # Se guarda el total dentro del diccionario
    datos_cliente["total"] = total_cliente

    # Se agrega el diccionario completo a la lista de clientes
    clientes.append(datos_cliente)

    # Se guarda el total en la lista de totales
    lista_totales.append(total_cliente)

#finalmente el imprime el total de dinero de todos los pedidos con la funcion que esta al principio
mostrar_total(lista_totales)

# Se pregunta si desea ver los clientes
imprimir_final = int(input("Si deseas ver todos los datos de los clientes ingresados presiona (1) sino presiona cualquier otro numero para terminar el proceso:"))

if imprimir_final == 1:
    #se usa la funcion del principio para imprimir la lista
    todos_datos(clientes)
else: print("Gracias por usar la plataforma para la hora pico")
