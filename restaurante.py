##############################################################
from secrets import choice
from personas import Cocinero, Repartidor
from platos import Comestible, Bebestible
## Si necesita agregar imports, debe agregarlos aquí arriba ##


### INICIO PARTE 3 ###
class Restaurante:
    def __init__(self,nom,pl,coci,repa):
        self.nombre = nom
        self.platos = pl
        self.cocineros = coci
        self.repartidores = repa
        self.calificacion = 0
        pass

    def recibir_pedidos(self,clientes):
        pedido = []
        for cli in clientes:
            for pla in cli.platos_preferidos:
                if pla[1]=="Comestible":
                        instancia_comestible=Comestible(pla[0])
                        #print(instancia_comestible)
                        #print(f"Esta es la instancia :{instancia_comestible.nombre}")
                        pedido.append(instancia_comestible)
                elif pla[1]=="Bebestible":
                    instancia_comestible=Bebestible(pla[0])
                    #print(instancia_comestible)
                    #print(f"Esta es la instancia :{instancia_comestible.nombre}")
                    pedido.append(instancia_comestible)
            self.repartir_pedido(cli,pedido)
        calificacion_final = self.calificacion / len(clientes)
        pass

    def repartir_pedido (self,cliente,pedido):
        self.repartidores
        self.repartidor = choice(self.repartidores)
        if self.repartidor.energia > 15:
            demora = self.repartidor.repartir(pedido)
            calificacion =cliente.recibir_pedido(pedido,demora)
        else:
            estado = self.cambiar_repartidor(self)
            if estado == "false":
                lista = []
                calificacion = cliente.recibir_pedido(lista,0)
        self.calificacion = calificacion
        pass

    def cambiar_repartidor (self):
        repartidor = self.repartidores[0].energia
        for r in range(len(self.repartidores)):
            repartidor1 = self.repartidores[r].energia
            if  repartidor1 > repartidor.energia:
                repartidor = self.repartidores[r]
                estado = "true"
            else:
                estado = "false"
        return (estado)


      #if repartidor.energia < 15:

        pass     
    def cocinar_plato(self,plato):
        cocinero = choice(self.cocineros)
        pedido = []
        Platonococinado = ""
        if "Bebestible" in plato:
            if cocinero.energia >= 10:
                cocinero.cocinar(plato)
                pedido = plato
            else:
                cocinero = choice(self.cocineros)
                if cocinero.energia <15:
                    Platonococinado = "No se pudo cocinar su plato"
                    pedido = Platonococinado
        elif "Comestible" in plato:
            if cocinero.energia >= 15:
                cocinero.cocinar(plato)                
                pedido = plato
            else:
                cocinero = choice(self.cocineros)
                if cocinero.energia <15:
                    Platonococinado = "No se pudo cocinar su plato"
                    pedido = Platonococinado
        return (pedido)
                    
        


### FIN PARTE 3 #


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Pepsi": ["Pepsi", "Bebestible"],
        "Mariscos": ["Mariscos", "Comestible"],
        }
        un_restaurante = Restaurante("Bon Appetit", PLATOS_PRUEBA, [], [])
        print(f"El restaurante {un_restaurante.nombre}, tiene los siguientes platos:")
        for plato in un_restaurante.platos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
