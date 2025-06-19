libros = []
ventas = []
editorales = ("planeta ", "anagrama ", "penguin ramdom house")

def registrar_libro():
    codigo = int(input("codigo del libro: "))
    titulo = input("titulo: ")
    autor = input("autor: ")
    
    print(" editoriales disponibles:")
    for i in range(len(editorales)):
        print(f"{i+1}. {editorales[i]}")
    cod_editorial = int(input("seleccione un editorial: "))
    editoral = editorales[cod_editorial-1]
    
    precio = float(input("precio del libro: "))
    stock = int (input("cantidad de stock:"))
    
    
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
    codigo = int(input("codigo del libro que desa comprar: "))
    for libro in libros:
        if libro['codigo'] == codigo:
            print(f"titulo: {libro['titulo']}, stock: {libro['stock']}")
            cantidad = int(input("cantidad a comprar: "))
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