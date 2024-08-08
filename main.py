import json
from colorama import Fore, Style

def cargar():
    with open("info.json", 'r' ) as f:
        info=json.load(f)

def guardar(info):
    with open("info.json", 'w') as f:
        json.dump(info,f, indent=4)  

while True: 
    print(Fore.YELLOW + "=========================" + Style.RESET_ALL)
    print(Fore.GREEN + "   BIENVENDIDOS PANCAMP   " + Style.RESET_ALL)
    print(Fore.YELLOW + "=========================" + Style.RESET_ALL)
    print(Fore.GREEN + "        GESTION      " + Style.RESET_ALL)
    print(Fore.YELLOW + "1. Ventas" + Style.RESET_ALL)
    print(Fore.YELLOW + "2. Compras" + Style.RESET_ALL)
    print(Fore.YELLOW + "3. Generacion de informes" + Style.RESET_ALL)
    print(Fore.RED + "0. Salir" + Style.RESET_ALL) 
    print("")
    opcion=int(input("Selecciona una opcion: "))

    if opcion==0: #Salir del programa
        print(Fore.BLACK + "Gracias por comprar en PANCAMP" + Style.RESET_ALL)
        break

    elif opcion==1:
        print(Fore.GREEN + "---- VENTAS ----" + Style.RESET_ALL)
        info={
            "cliente":{
                "fecha_venta": input("Ingresa la fecha de venta: "),
                "mombre": input("Ingresa los nombres del cliente: "),
                "apellido": input("Ingresa los apellido del cliente: "),
                "direccion": input("Ingresa Direccion del cliente: "),
                "productos":{
                    "nombre_empleado": input("Ingresa el nombre del empleado que realizo la venta: "),
                    "nombre_producto": input("Ingresa el nombre del producto: "),
                    "cantidad_producto": int(input("Ingresa la cantidad del producto: ")),
                    "precio_producto": int(input("Ingresa el precio del producto: ")),
                }
                }
        }
        guardar(info)
        input(Fore.CYAN + "Presiona Enter para continuar..." + Style.RESET_ALL)

    elif opcion==2:
        print(Fore.GREEN + "---- COMPRAS ----" + Style.RESET_ALL)
        info={
            "proveedor":{
                "fecha_compra": input("Ingresa la fecha de compra: "),
                "mombre": input("Ingresa los nombres del proveedor: "),
                "numero_contacto": int(input("Ingresa el numero de contacto del proveedor: ")),
                "nombre_producto_comprado": input("Ingresa el nombre del producto: "),
                "cantidad_producto_comprado": int(input("Ingresa la cantidad del producto: ")),
                "precio_producto_comprado": int(input("Ingresa el precio de compra del producto: ")),
                }
        }
        guardar(info)
        input(Fore.CYAN + "Presiona Enter para continuar..." + Style.RESET_ALL)