from datetime import date,datetime
import requests

#Día actual y fecha
today = date.today()
now = datetime.now()

#Creacción de funciones en el menú
def mostrar_menu(nombre, opciones): 
    for clave in sorted(opciones):
        print(f' {clave}) {opciones[clave][0]}')

#Fallo en el menú
def leer_opcion(opciones):
    while (a := input('Opción: ')) not in opciones:
        print('Opción incorrecta, vuelva a intentarlo.')
    return a
def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()
#Mostrar hora
    print()
    print(today)
print(now)

# incorporamos el parámetro para mostrar el nombre del menú
def generar_menu(nombre, opciones, opcion_salida):  
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(nombre, opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()

# Configuración del menú
def menu_principal():
    print("Bienvenido")
    print("Seleccione una opción: ")
    opciones = {
        '1': ('Consultar clima', submenu),
        '2': ('Salir', salir)
    }
# indicamos el nombre del menú y sus opciones
    generar_menu('Menú principal', opciones, '2')  

# Configuración del submenú
def submenu():
    opciones = {
        "a": ("En línea", funcionA),
        "b": ('Por bitacora', funcionB),
        "c": ("Volver al menú principal", salir)
    }
# indicamos el nombre del menú y sus opciones
    generar_menu("Submenú", opciones, "c")

# opciones ejecutadas
def funcionA():
   city = input("Enter a city: ")
   url = f"https://es.wttr.in/{city}"

   res = requests.get(url)
   print(res.text)

# Configuración del submenú
def submenu2():
    opciones = {
        "c": ("Volver al menú principal", salir)
    }
# indicamos el nombre del menú y sus opciones
    generar_menu("Submenú2", opciones, "c")

def funcionB():
    print("Has elegido consulta por bitacora")

def salir():
    print("Saliendo")

# iniciamos el programa mostrando el menú principal
if __name__ == '__main__':
    menu_principal() 
