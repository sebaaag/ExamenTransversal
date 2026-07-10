peliculas = {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}

cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}

def leer_opcion():
    try:
        opcion = int(input("Ingrese una opcion: "))
        if opcion >= 1 and opcion <= 6:
            return opcion
        else:
            print("Ingrese una opcion valida")
            return None
    except ValueError:
        print("Ingrese una opcion valida")

def cupos_genero(peliculas, cartelera, genero):
    total_cupos = 0
    genero_buscado = genero.strip().lower()
    
    for cod, datos in peliculas.items():
        if datos[1].lower() == genero_buscado:
            if cod in cartelera:
                total_cupos += cartelera[cod][1]
    print(f"El total de cupos disponibles es: {total_cupos}")

def busqueda_precio(peliculas, cartelera, p_min, p_max):
    resultados = []
    
    for cod, datos_cartelera in cartelera.items():
        precio = datos_cartelera[0]
        cupos = datos_cartelera[1]
        
        if p_min <= precio <= p_max and cupos > 0:
            if cod in peliculas:
                titulo = peliculas[cod][0]
                resultados.append(f"{titulo}--{cod}")
    if resultados:
        resultados.sort()
        print(f"Las peliculas encontradas son: {resultados}")
    else:
        print("No hay peliculas en ese rango de precios")

def buscar_codigo(cartelera, codigo):
    cod_buscado = codigo.strip().upper()
    for cod in cartelera.keys():
        if cod.upper() == cod_buscado:
            return True
    return False

def obtener_codigo_real(cartelera, codigo):
    cod_buscado = codigo.strip().upper()
    for cod in cartelera.keys():
        if cod.upper() == cod_buscado:
            return cod
    return codigo

def actualizar_precio(cartelera, codigo, nuevo_precio):
    if buscar_codigo(cartelera, codigo):
        cod_real = obtener_codigo_real(cartelera, codigo)
        cartelera[cod_real][0] = nuevo_precio
        return True
    return False

def validar_codigo(peliculas, codigo):
    if not codigo.strip():
        return False
    cod_buscado = codigo.strip().upper()
    for cod in peliculas.keys():
        if cod.upper() == cod_buscado:
            return False
    return True

def validar_titulo(titulo):
    return bool(titulo.strip())

def validar_genero(genero):
    return bool(genero.strip())

def validar_duracion(duracion_str):
    try:
        duracion = int(duracion_str)
        return duracion > 0
    except ValueError:
        return False

def validar_clasificacion(clasificacion):
    return clasificacion.strip().upper() in ['A', 'B', 'C']

def validar_idioma(idioma):
    return bool(idioma.strip())

def validar_es_3d(es_3d_str):
    return es_3d_str.strip().lower() in ['s', 'n']

def validar_precio_(precio_str):
    try:
        precio = int(precio_str)
        return precio > 0
    except ValueError:
        return False

def validar_cupos(cupos_str):
    try:
        cupos = int(cupos_str)
        return cupos >= 0
    except ValueError:
        return False


def agregar_pelicula(peliculas, cartelera, codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    if buscar_codigo(cartelera, codigo):
        return False
    
    cod_final = codigo.strip().upper()
    bool_3d = True if es_3d.strip().lower() == 's' else False
    
    peliculas[cod_final] = [
        titulo.strip(),
        genero.strip().lower(),
        int(duracion),
        clasificacion.strip().upper(),
        idioma.strip(),
        bool_3d
    ]
    
    cartelera[cod_final] = [int(precio), int(cupos)]
    return True

def eliminar_pelicula(peliculas, cartelera, codigo):
    if buscar_codigo(cartelera, codigo):
        cod_real = obtener_codigo_real(cartelera, codigo)
        del peliculas[cod_real]
        del cartelera[cod_real]
        return True
    return False

while True:
    print("\n===== Menu principal =====")
    print("1. Cupos por genero")
    print("2. Busqueda de peliculas por rango de precio")
    print("3. Actualizar precio de la pelicula")
    print("4. Agregar pelicula")
    print("5. Eliminar pelicula")
    print("6. Salir")
    print("=============================")
    
    opcion = leer_opcion()
    if opcion is None:
        continue
    
    if opcion == 1:
        genero = input("Ingrese genero a consultr: ")
        cupos_genero(peliculas, cartelera, genero)
        
    elif opcion == 2:
        while True:
            try:
                p_min = int(input("Ingrese precio minimo: "))
                p_max = int(input("Ingrese precio maximo"))
                if p_min >=0 and p_max >= 0 and p_min <= p_max:
                    busqueda_precio(peliculas, cartelera, p_min, p_max)
                    break
                else:
                    print("Deben ser valores positivos")
            except ValueError:
                print("Debe ingresar valores enteros")
    
    elif opcion == 3:
        while True:
            codigo = input("Ingrese codigo de pelicula:")
            try:
                nuevo_precio = int(input("Ingrese nuevo precio: "))
                if nuevo_precio <= 0:
                    print("El precio debe ser un numero entero mayor a cero")
                    continue
            except ValueError:
                print("Debe ingresar un valor entero que sea valido")
                continue
            if actualizar_precio(cartelera, codigo, nuevo_precio):
                print("Precio actualiazado")
            else:
                print("El codigo no existe")
            
            otro = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
            if otro != 's':
                break
    
    elif opcion == 4:
        codigo = input("Ingrese codigo de pelicula: ")
        titulo = input("Ingrese titulo: ")
        genero = input("Ingrese genero: ")
        duracion = input("Ingrese duracion (en minutos): ")
        clasificacion = input("Ingrese clasificacion: ")
        idioma = input("Ingrese idioma: ")
        es_3d = input("¿Es 3D? (s/n): ")
        precio= input("Ingrese precio: ")
        cupos = input("Ingrese cupos: ")
        
        if not validar_codigo(peliculas, codigo):
            print("Error, el codigo no existe")
        elif not validar_titulo(titulo):
            print("Error, el titulo no puede estar vacio")
        elif not validar_genero(genero):
            print("error, el genero no puede estar vacio")
        elif not validar_duracion(duracion):
            print("Error, la duracion debe ser mayor a cero")
        elif not validar_clasificacion(clasificacion):
            print("Error, a clasifiacion debe ser 'A', 'B', o 'C' ")
        elif not validar_idioma(idioma):
            print("Error, el idioma no puede estar vaco")
        elif not validar_es_3d(es_3d):
            print("Erro, debe ingresar 's' o 'n'")
        elif not validar_precio_(precio):
            print("Error, el precio debe ser mayor a zero")
        elif not validar_cupos(cupos):
            print("Error, los cupos deben ser igual o mayor a cero")
        else:
            if agregar_pelicula(peliculas, cartelera, codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
                print("Pelicula agregada")
            else:
                print("El codigo ya existe")
    
    elif opcion == 5:
        codigo = input("Ingrese el codigo de la pelicula que desea eliminar: ")
        if eliminar_pelicula(peliculas, cartelera, codigo):
            print("Pelicula eliminada")
        else:
            print("El codigo no existe")
            
    elif opcion == 6:
        print("Programa finalizado")
        break