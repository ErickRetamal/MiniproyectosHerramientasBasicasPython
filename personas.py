##############################################################
from random import randint
from platos import Comestible, Bebestible
## Si necesita agregar imports, debe agregarlos aquí arriba ##

### INICIO PARTE 2.1 ###
class Persona:
    def __init__(self,nom):
        self.nombre = nom
    pass
### FIN PARTE 2.1 ###

### INICIO PARTE 2.2 ###
class Repartidor(Persona):
    def __init__(self, nom,tiempo):
        super().__init__(nom)
        self.tiempo_entrega = tiempo
        self.energia = randint(75,100)
    
    def obtener_factor(self,pedido):
        factor_tamaño = 0
        factor_velocidad  = 0
        if len(pedido) <= 2:
            factor_tamaño = 5
            factor_velocidad = 1.25
        elif len(pedido) >=3 :
            factor_tamaño = 15
            factor_velocidad = 0.85
            return (factor_tamaño,factor_velocidad)

    def repartir(self,pedido):
        obtener = self.obtener_factor(pedido)
        t,v = obtener
        self.energia -= t
        demora = self.tiempo_entrega * v
        return (demora)
### FIN PARTE 2.2 ###

### INICIO PARTE 2.3 ###
class Cocinero(Persona):
    def __init__(self, nom,hab):
        super().__init__(nom)
        self.habilidad = hab
        self.energia = randint(50,80)
    
    def cocinar(self,informacion_plato):
        a,b = informacion_plato
        if "Bebestible" in informacion_plato:
            self.consumo = Bebestible(a)
            self.disminuir_energia
            self.calcular_fcalidad
        elif "Comestible" in informacion_plato:
            self.consumo = Comestible(a)
            self.energia -= 15
            self.calcular_fcalidad
        return (self.consumo)
    
    def calcular_fcalidad (self):
        if self.consumo.dificultad > self.habilidad:
            self.consumo.calidad = self.consumo.calidad * 0.7
        elif self.consumo.dificultad < self.habilidad:
            self.consumo.calidad -= self.consumo.calidad * 1.5
        pass 
            
    def disminuir_energia(self):
        if self.bebestible.tamaño == "pequeño":
            self.energia -= 5
        elif self.bebestible.tamaño == "mediano":
            self.energia -= 8
        elif self.bebestible.tamaño == "grande":
            self.energia -= 10
        pass


    pass 
### FIN PARTE 2.3 ###

### INICIO PARTE 2.4 ###
class Cliente(Persona):
    def __init__(self, nom,pla):
        super().__init__(nom)
        self.platos_preferidos = pla

    def recibir_pedido(self,pedido,demora):
        calificacion = 10
        if len(pedido) < len(self.platos_preferidos) or demora >= 20:
            calificacion = calificacion/2
        for p in pedido:
            if p.calidad >= 11:
                calificacion += 1.5
            elif p.calidad <= 8:
                calificacion -= 3
            else:
                calificacion
        return (calificacion) 
    pass
### FIN PARTE 2.4 ###


if __name__ == "__main__":

    ### Código para probar que tu clase haya sido creada correctamente  ###
    ### Corre directamente este archivo para que este código se ejecute ###
    try:
        PLATOS_PRUEBA = {
        "Jugo Natural": ["Jugo Natural", "Bebestible"],
        "Empanadas": ["Empanadas", "Comestible"],
        }
        un_cocinero = Cocinero("Cristian", randint(1, 10))
        un_repartidor = Repartidor("Tomás", randint(20, 30))
        un_cliente = Cliente("Alberto", PLATOS_PRUEBA)
        print(f"El cocinero {un_cocinero.nombre} tiene una habilidad: {un_cocinero.habilidad}")
        print(f"El repatidor {un_repartidor.nombre} tiene una tiempo de entrega: {un_repartidor.tiempo_entrega} seg")
        print(f"El cliente {un_cliente.nombre} tiene los siguientes platos favoritos:")
        for plato in un_cliente.platos_preferidos.values():
            print(f" - {plato[1]}: {plato[0]}")
    except TypeError:
        print("Hay una cantidad incorrecta de argumentos en algún inicializador y/o todavía no defines una clase")
    except AttributeError:
        print("Algún atributo esta mal definido y/o todavia no defines una clase")
