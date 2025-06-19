libros = []
ventas = []
editorales = ("planeta ", "anagrama ", "penguin ramdom house")

def registrar_libro():
    codigo = validar_codigo()
    titulo = input("titulo: ")
    autor = input("autor: ")
    
    print(" editoriales disponibles:")
    for i in range(len(editorales)):
        print(f"{i+1}. {editorales[i]}")
    cod_editorial = int(input("seleccione un editorial: "))
    editoral = editorales[cod_editorial-1]
    
    precio = validar_precio()
    stock = validar_entero_positivo()
    
    
    libro = {
        "codigo": codigo,
        "titulo": titulo,
        "autor": autor,
        "editorial": editoral,
        "precio": precio,
        "stock": stock
    }
    libros.append(libro)
    print("libro registrado correctamente. ")
    
def ver_catalago():
    if not libros :
        print("no hay libros en el catalogo")
    else:
        for libro in libros: 
            print(f"codigo: {libro['codigo']}")
            print(f"titulo: {libro['titulo']}")
            print(f"autor: {libro['autor']}")
            print(f"editorial: {libro['editorial']}")
            print(f"precio: {libro['precio']}")
            print(f"stock: {libro['stock']}")

def vender_libros():
    codigo = validar_codigo_unico(input("codigo del libro a comprar: "))
    for libro in libros:
        if libro['codigo'] == codigo:
            print(f"titulo: {libro['titulo']}, stock: {libro['stock']}")
            cantidad = validar_entero_positivo("cantidad a comprar: ")
            if cantidad <= libro['stock']:
                libro['stock'] -= cantidad
                total = cantidad * libro['precio']
                venta ={
                    "titulo ": libro['titulo'],
                    "precio": cantidad,
                    "editorial": total
                }
                ventas.append(venta)
                print (f" comprar realizar por ${total}")
                return
            else:
                print("no hay suficiente stock")
                return
        else:
            print("libro no encontrado")
            
def ver_ventas():
    if not ventas:
        print("no hay ventas")
    else:
        for venta in ventas:
            print(f"titulo: {venta['titulo']}")
            print(f"precio: {venta['precio']}")
            print(f"editorial: {venta['editorial']}")

def validar_codigo():
    while True:
        cod=input("Ingrese codigo del libro:")
        if cod.isdigit() and int (cod) >= 1:
            return int(cod)
        print (" ERROR: el codigo debe ser un numero entero mayor o igual a 1.")

def validar_codigo_unico(codigo ):
    for libro in libros:
        if libro['codigo'] == codigo:
            print("ERROR: ya existe un libro con ese codigo")
            return False
    return True

def validar_precio():
    while True:
        try:
            precio = float(input("Ingrese precio del libro:"))
            if precio > 0:
                return precio
            else:
                print("ERROR: el precio debe ser mayor a 0")
        except ValueError:
            print("ERROR: debe ingresar un numero decimal valido")
            
def validar_entero_positivo(mensaje="ingrese un numero" ):
    while True:
        num = input(mensaje)
        if num.isdigit() and int(num) > 0:
            return int(num)
        print("ERROR: deve ingresar un numero entero mayor a 0.")
        