from funciones import *


while True:
    print("""===libreria virtual ===
    1. registrar libro
    2. ver catalago
    3. vender libro
    4.ver ventas
    5. salir...""")
    
    opcion=input(" seleccione una opcion:")
    if opcion == "1":
        registrar_libro()
    elif opcion == "2":
        ver_catalago()
    elif opcion == "3":
        vender_libros()
    elif opcion == "4":
        pass
    elif opcion == "5":
        print("gracias por visitar la libreria virtual")
        break
    else:
        print("opcion incorrecta")