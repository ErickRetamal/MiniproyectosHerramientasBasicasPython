import csv

def cargar_datos():
    Opokemon = open("MP1\pokemon.csv")
    ListaPokemon = list(Opokemon)
    ListaPokemon2=[]

    for filatextopokemon in ListaPokemon:
        filapokemon= filatextopokemon.split(",")
        ListaPokemon2.append(filapokemon)

    del filatextopokemon, filapokemon, ListaPokemon
    #Creacion Listado de tipos de pokemon
    tipos_pokemon = [] #Lista de tipos de pokemon
    for i in range(len(ListaPokemon2)):
        if ListaPokemon2[i][2] not in tipos_pokemon:
            tipo = ListaPokemon2[i][2]
            tipos_pokemon.append(tipo)  
                    
    tipos_pokemon.remove("tipo")
    del i,tipo
    #Fin creacion listado de tipos pokemon

    #Creacion diccionario pokemon por tipo
    pokemon_por_tipo = {}

    for j in range(len(tipos_pokemon)):
        PokemonTipo = []
        for k in range(len(ListaPokemon2)):
            if ListaPokemon2[k][2]==tipos_pokemon[j]:
                PokemonTipo.append(ListaPokemon2[k][0])
        Pokemonset=set(PokemonTipo)
        PokemonTipo=list(Pokemonset)
        pokemon_por_tipo[tipos_pokemon[j]]= PokemonTipo
    del j, k,Pokemonset, PokemonTipo
    #Fin creacion diccionario pokemon por tipo

    #DICCIONARIO INFO_POKEMON
    #Variables Diccionario INFO_POKEMON
    info_pokemon = {}
    IdPokemon = []
    VariablesPokemon = []
    ValoresPokemon = []
    #---------------------------------------------------------------------------------------------------#
    #Añadimos todos los id pokemon a la lista
    for p in range(len(ListaPokemon2)):
        if ListaPokemon2[p][0] not in IdPokemon:
            id = ListaPokemon2[p][0]
            IdPokemon.append(id)
    IdPokemon.remove("id")
    del p,id
    #Fin añadir id pokemon a la lista
    #---------------------------------------------------------------------------------------------------#
    #Añadir Variables pokemon
    VariablesPokemon = ListaPokemon2[0][1:7]
    VariablesPokemon[5] = "generacion"
    #Fin Variables pokemon
    #---------------------------------------------------------------------------------------------------#
    #Inicio añadir Valores
    ListaPokemon2.pop(0)
    for k in range(len(ListaPokemon2)):
        if ListaPokemon2[k][1:7] not in ValoresPokemon:
            ValoresPokemon.append(ListaPokemon2[k][1:7])
    for saltodelinea in ValoresPokemon:#limpiar saltos de lineas ---->n\
        saltodelinea[-1]=saltodelinea[-1].strip()
    #Fin añadir Valores
    #---------------------------------------------------------------------------------------------------#
    #Armado del diccionario
    diccionario2 = []
    for c in range(len(ValoresPokemon)):
        diccionario2.append(dict(zip(VariablesPokemon, ValoresPokemon[c])))
    info_pokemon= dict(zip(IdPokemon, diccionario2))
    #Fin Armado del diccionario
    #---------------------------------------------------------------------------------------------------#
    #for k in range(len(Info_pokemon)):
    #Fin Diccionario INFO_POKEMON
    tupla = (tipos_pokemon, pokemon_por_tipo, info_pokemon)
    return (tupla)
    # Parte 1: Cargar los datos
   

# Parte 2: Completar las consultas


def obtener_ataque_y_defensa(nombre_pokemon):
    tipos_pokemon, pokemon_por_tipo, info_pokemon = cargar_datos()
    atkdef = ()
    for id_ in info_pokemon:
            validador = info_pokemon[id_]["nombre"]
            if nombre_pokemon == validador:
                atk_ = info_pokemon[id_]["ataque"]
                def_ = info_pokemon[id_]["defensa"]
                atkdef = (atk_,def_)
    return atkdef

def filtrar_y_ordenar(tipo_pokemon, criterio):
    tipos_pokemon, pokemon_por_tipo, info_pokemon = cargar_datos()
    listadopokemon = []
    ordenados = []
    ordenados1 = []
    for id_ in info_pokemon:
        validador = info_pokemon[id_]["tipo"]
        if tipo_pokemon == validador:
            listadopokemon.append(info_pokemon[id_])
    for y in range(len(listadopokemon)):
        ordenados = listadopokemon[y]
        ordenados = ordenados.values()
        ordenados = list(ordenados)
        ordenados1.append(ordenados)
    #ordenados3.append(ordenados2)
    #ordenados1.sort(reverse=True)
    for h in range(len(ordenados1)):    
        ordenados1[h][2] = int(ordenados1[h][2])
        ordenados1[h][3] = int(ordenados1[h][3])
        ordenados1[h][4] = int(ordenados1[h][4])

    if criterio == "ataque":
        filtro = sorted(ordenados1, key = lambda criterio1 : criterio1[3], reverse=True)
    elif criterio == "defensa":
        filtro = sorted(ordenados1, key = lambda criterio1 : criterio1[4], reverse=True)
    elif criterio == "hp":
        filtro = sorted(ordenados1, key = lambda criterio1 : criterio1[2], reverse=True)
    else:
        print("no existe ese criterio")
    filtro1 = []
    for j in range(len(filtro)):
        if filtro[j][0] not in filtro1:
            filtro1.append(filtro[j][0])
        
    #ordenados1.sort(reverse=True)
    return filtro1
    

def estadisticas (lista):
    maximo = max(lista)
    minimo = min(lista)
    promedio = (sum(lista) / len(lista))
    diccestadisticas = {"max":maximo, "min": minimo, "prom": promedio}
    #ordenados1.sort(reverse=True)
    return diccestadisticas



def obtener_estadisticas(tipo_pokemon, criterio):
    tipos_pokemon, pokemon_por_tipo, info_pokemon = cargar_datos()
    listadopokemon = []
    ordenados = []
    ordenados1 = []
    for id_ in info_pokemon:
        validador = info_pokemon[id_]["tipo"]
        if tipo_pokemon == validador:
            listadopokemon.append(info_pokemon[id_])
    for y in range(len(listadopokemon)):
        ordenados = listadopokemon[y]
        ordenados = ordenados.values()
        ordenados = list(ordenados)
        ordenados1.append(ordenados)
    #ordenados3.append(ordenados2)
    #ordenados1.sort(reverse=True)
    for h in range(len(ordenados1)):    
        ordenados1[h][2] = int(ordenados1[h][2])
        ordenados1[h][3] = int(ordenados1[h][3])
        ordenados1[h][4] = int(ordenados1[h][4])
    if criterio == "ataque":
        papaya = []
        for m in range(len(ordenados1)):
            papaya.append(ordenados1[m][3])
        filtro = estadisticas(papaya)
    elif criterio == "defensa":
        papaya = []
        for m in range(len(ordenados1)):
            papaya.append(ordenados1[m][4])
        filtro = estadisticas(papaya)
    elif criterio == "hp":
        papaya = []
        for m in range(len(ordenados1)):
            papaya.append(ordenados1[m][2])
        filtro = estadisticas(papaya)
    else:
        print("no existe ese criterio")
    return filtro


def solicitar_accion():
    print("\n¿Qué desea hacer?\n")
    print("[0] Revisar estructuras de datos")
    print("[1] Obtener ataque y defensa de un pokemon")
    print("[2] Filtrar y ordenar pokemons")
    print("[3] Obtener estadísticas de pokemons")
    print("[4] Salir")

    eleccion = input("\nIndique su elección (0, 1, 2, 3, 4): ")
    while eleccion not in "01234":
        eleccion = input("\nElección no válida.\nIndique su elección (0, 1, 2, 3, 4): ")
    eleccion = int(eleccion)
    return eleccion


def revisar_estructuras(tipos_pokemon, pokemon_por_tipo, info_pokemon):
    print("\nTipos de pokemon:")
    for tipo in tipos_pokemon:
        print(f"    - {tipo}")

    print("\nId de pokemons por tipo:")
    for tipo in pokemon_por_tipo:
        print(f"    Tipo: {tipo}")
        for id_ in pokemon_por_tipo[tipo]:
            print(f"        - {id_}")

    print("\nInformación de cada pokemon:")
    for id_ in info_pokemon:
        print(f"    Id: {id_}")
        for llave in info_pokemon[id_]:
            print(f"        - {llave}: {info_pokemon[id_][llave]}")


def solicitar_nombre():
    nombre = input("\nIngrese el nombre del pokemon: ")
    return nombre


def solicitar_tipo_y_criterio():
    tipo = input("\nIndique el tipo de pokemon: ")
    criterio = input("\nIndique el criterio (hp, ataque, defensa): ")
    return tipo, criterio


def main():
    datos_cargados = True
    try:
        tipos_pokemon, pokemon_por_tipo, info_pokemon = cargar_datos()
    except TypeError as error:
        if 'cannot unpack non-iterable NoneType object' in repr(error):
            print("\nTodavía no puedes ejecutar el programa ya que no has cargado los datos\n")
            datos_cargados = False
    if datos_cargados:
        salir = False
        print("\n********** ¡Bienvenid@! **********")
        while not salir:
            accion = solicitar_accion()

            if accion == 0:
                revisar_estructuras(tipos_pokemon, pokemon_por_tipo, info_pokemon)

            elif accion == 1:
                nombre_pokemon = solicitar_nombre()
                ataque, defensa = obtener_ataque_y_defensa(nombre_pokemon)
                print(f"\nObteniendo ataque y defensa de {nombre_pokemon}")
                print(f"    - Ataque: {ataque}")
                print(f"    - Defensa: {defensa}")

            elif accion == 2:
                tipo, criterio = solicitar_tipo_y_criterio()
                nombres_pokemon = filtrar_y_ordenar(tipo, criterio)
                print(f"\nNombres de pokemon tipo {tipo} ordenados segun {criterio}:")
                for nombre in nombres_pokemon:
                    print(f"    - {nombre}")

            elif accion == 3:
                tipo, criterio = solicitar_tipo_y_criterio()
                estadisticas = obtener_estadisticas(tipo, criterio)
                print(f"\nEstadísticas de {criterio} de pokemon tipo {tipo}:")
                print(f"    - Máximo: {estadisticas['max']}")
                print(f"    - Mínimo: {estadisticas['min']}")
                print(f"    - Promedio: {estadisticas['prom']}")

            else:
                salir = True
        print("\n********** ¡Adiós! **********\n")


if __name__ == "__main__":
    main()
