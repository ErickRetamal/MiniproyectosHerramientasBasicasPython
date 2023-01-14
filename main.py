##############################################################
from random import seed,randint, choice, sample
import personas,restaurante

## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 4 ###

def crear_repartidores():
    Repartidores = [personas.Repartidor(choice(NOMBRES),randint(20,30)),
    personas.Repartidor(choice(NOMBRES),randint(20,30))]
    return(Repartidores)

def crear_cocineros():
    Cocineros = [personas.Cocinero(choice(NOMBRES),randint(1,10)),
    personas.Cocinero(choice(NOMBRES),randint(1,10)),
    personas.Cocinero(choice(NOMBRES),randint(1,10)),
    personas.Cocinero(choice(NOMBRES),randint(1,10)),
    personas.Cocinero(choice(NOMBRES),randint(1,10))]
    return (Cocineros)

def crear_clientes():
    listaplatos = INFO_PLATOS.keys()
    Clientes = [personas.Cliente(choice(NOMBRES), sample(list(INFO_PLATOS.values()),randint(1,5))),
    personas.Cliente(choice(NOMBRES),sample(listaplatos,k=randint(1,5))),
    personas.Cliente(choice(NOMBRES),sample(listaplatos,k=randint(1,5))),
    personas.Cliente(choice(NOMBRES),sample(listaplatos,k=randint(1,5))),
    personas.Cliente(choice(NOMBRES),sample(listaplatos,k=randint(1,5)))]
    return (Clientes)

def crear_restaurante():
    cocineros = crear_cocineros()
    repartidores = crear_repartidores()
    restaurant = restaurante.Restaurante("El Rincon del Gordo",INFO_PLATOS,cocineros,repartidores)
    return (restaurant)

### FIN PARTE 4 ###

################################################################
## No debe modificar nada de abajo en este archivo.
## Este archivo debe ser ejecutado para probar el funcionamiento
## de su programa orientado a objetos.
################################################################

INFO_PLATOS = {
    "Pepsi": ["Pepsi", "Bebestible"],
    "Coca-Cola": ["Coca-Cola", "Bebestible"],
    "Jugo Natural": ["Jugo Natural", "Bebestible"],
    "Agua": ["Agua", "Bebestible"],
    "Papas Duqueza": ["Papas Duqueza", "Comestible"],
    "Lomo a lo Pobre": ["Lomo a lo Pobre", "Comestible"],
    "Empanadas": ["Empanadas", "Comestible"],
    "Mariscos": ["Mariscos", "Comestible"],
}

NOMBRES = ["Amaia", "Cristian", "Maggie", "Pablo", "Catalina", "Juan", "Sergio"]

if __name__ == "__main__":

    ### Código para probar que tu miniproyecto esté funcionando correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    seed()
    restaurante = crear_restaurante() # Crea el restaurante a partir de la función crear_restaurante()
    clientes = crear_clientes() # Crea los clientes a partir de la función crear_clientes()
    if restaurante != None and clientes != None:
        restaurante.recibir_pedidos(clientes) # Corre el método recibir_pedidos(clientes) para actualizar la calificación del restaurante
        print(
            f"La calificación final del restaurante {restaurante.nombre} "
            f"es {restaurante.calificacion}"
        )
    elif restaurante == None:
        print("la funcion crear_restaurante() no esta retornando la instancia del restaurante")
    elif clientes == None:
        print("la funcion crear_clientes() no esta retornando la instancia de los clientes")
