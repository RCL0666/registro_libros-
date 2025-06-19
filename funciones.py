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