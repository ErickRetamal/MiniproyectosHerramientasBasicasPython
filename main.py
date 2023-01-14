from operator import index
import parametros as p
import random


# NO MODIFICAR
class Rueda:
    def __init__(self):
        self.resistencia_actual = random.randint(*p.RESISTENCIA)
        self.resistencia_total = self.resistencia_actual
        self.estado = "Perfecto"

    def gastar(self, accion):
        if accion == "acelerar":
            self.resistencia_actual -= 5
        elif accion == "frenar":
            self.resistencia_actual -= 10
        self.actualizar_estado()

    def actualizar_estado(self):
        if self.resistencia_actual < 0:
            self.estado = "Rota"
        elif self.resistencia_actual < self.resistencia_total / 2:
            self.estado = "Gastada"
        elif self.resistencia_actual < self.resistencia_total:
            self.estado = "Usada"


# NO MODIFICAR
def seleccionar(vehiculos):
    for indice in range(len(vehiculos)):
        print(f"[{indice}] {str(vehiculos[indice])}")

    elegido = int(input())
    while elegido < 0 or elegido >= len(vehiculos):
        print("intentelo de nuevo.")
        elegido = int(input())

    vehiculo = vehiculos[elegido]
    print("Se seleccionó el vehículo", str(vehiculo))
    return vehiculo


# Parte 1: Definición de clases

class Automovil:
    def __init__(self,ki, a):
        self.__kilometraje = ki
        self.ano = a
        self.rueda = []
        self.aceleracion = 0
        self.velocidad = 0
    
    def avanzar(self,tiempo):
        self.__kilometraje += int(tiempo)*self.velocidad
        if self.velocidad == 0:
            print("No se ha podido avanzar debido a que la velocidad es 0")
        else:
            print(f"Se ha avanzado por:",tiempo,"segundos, a una velocidad de:",self.velocidad,"KM/h" )
        pass

    def acelerar(self,tiempo):
        self.aceleracion +=  float(tiempo)*0.5
        self.velocidad += (self.aceleracion*tiempo*3.6)
        self.avanzar(tiempo)
        self.aceleracion = 0
        pass
    def frenar(self,tiempo):
        self.aceleracion -= float(tiempo)*0.5
        freno = (int(tiempo)*3.6)
        self.velocidad += (self.aceleracion*freno)
        if self.velocidad <= 0:
            self.velocidad = 0
        self.avanzar(tiempo)
        self.aceleracion = 0
        pass

    def obtener_kilometraje(self):
        kilometros = self.__kilometraje
        return kilometros

    def reemplazar_rueda(self):
        reemplazo = self.rueda[0].resistencia_actual
        b = 0
        for a in range(len(self.rueda)):
            reemplazo1 = self.rueda[a].resistencia_actual
            if reemplazo > reemplazo1:
                reemplazo = reemplazo1
                b = int(a)
        self.rueda.pop(b)
        r = Rueda()
        self.rueda.append(r)
        pass

    def visualizar_ruedas(self):
        contador = 1
        for a in range(len(self.rueda)):
            print("La rueda n",contador,"tiene una resistencia actual de ",self.rueda[a].resistencia_actual,"y su estado es :", self.rueda[a].estado)
            contador = contador +1
    pass

class Moto(Automovil):
    def __init__(self, ki, a,ci):
        super().__init__(ki, a,ci)
        self.cilindrada = ci
        r1 = Rueda()
        r2 = Rueda()
        self.rueda.append(r1)
        self.rueda.append(r2)
        

    def acelerar(self,tiempo):
        Automovil.acelerar(self,tiempo)
        Rueda.gastar(self=self.rueda[0],accion="acelerar")
        Rueda.gastar(self=self.rueda[1],accion="acelerar")
    pass
    
    def frenar(self,tiempo):
        Automovil.frenar(self,tiempo)
        Rueda.gastar(self=self.rueda[0],accion="frenar")
        Rueda.gastar(self=self.rueda[1],accion="frenar")
    pass

    def __str__(self):
        return f"Moto del año {self.ano}."
    pass
    pass

class Camion(Automovil):
    def __init__(self, ki, a,carga):
        super().__init__(ki, a)
        self.carga = carga
        for j in range(6):
            self.rueda.append(Rueda())
    # Completar
    pass

    def acelerar(self,tiempo):
        Automovil.acelerar(self,tiempo)
        for a in range(len(self.rueda)):
            Rueda.gastar(self=self.rueda[a],accion="acelerar")
    pass
    
    def frenar(self,tiempo):
        Automovil.frenar(self,tiempo)
        for a in range(len(self.rueda)):
            Rueda.gastar(self=self.rueda[a],accion="frenar")
    pass

    def __str__(self):
        return f"Camión del año {self.ano}."


# Parte 2: Completar acciones

def accion(vehiculo, opcion):
    # Completar
    if opcion == 2:  # Acelerar
        tempo = (int(input("Indique tiempo de aceleracion: " )))
        vehiculo.acelerar(tempo)
        print(f"Se ha acelerado por:",tempo,"segundos, llegando a una velocidad de:",vehiculo.velocidad,"KM/h" )
        pass
    elif opcion == 3:  # Frenar
        tempo = (input("Indique tiempo para frenar: "))
        vehiculo.frenar(tempo)
        print(f"Se ha frenado por:",tempo,"segundos, llegando a una velocidad de:",vehiculo.velocidad,"KM/h" )
        pass
    elif opcion == 4:  # Avanzar
        tempo = (input("Indique tiempo para avanzar: "))
        vehiculo.avanzar(tempo)
        pass
    elif opcion == 5:  # Cambiar rueda
        vehiculo.reemplazar_rueda()
        print("Se ha reemplazado una rueda con exito")
        pass
    elif opcion == 6:  # Mostrar Estado
        print("Vehiculo año:", vehiculo.ano)
        print("Velocidad alcanzada:",vehiculo.velocidad)
        print("El Vehiculo tiene:",vehiculo.obtener_kilometraje(),"Kilometros")
        print(vehiculo.visualizar_ruedas())

def main():
    vehiculos = []
    # Parte 3: Completar código principal
    # Completar
    motina = Moto((random.randint(*p.KILOMETRAJE)),(random.randint(*p.ANO)),(random.randint(*p.CILINDRADA)))
    camionsino = Camion(random.randint(*p.KILOMETRAJE),random.randint(*p.ANO),random.randint(*p.CARGA))
    vehiculos.append(motina)
    vehiculos.append(camionsino)
    # NO MODIFICAR
    vehiculo = vehiculos[0]


    dict_opciones = {
        1: ("Seleccionar Vehiculo", seleccionar),
        2: ("Acelerar", accion),
        3: ("Frenar", accion),
        4: ("Avanzar", accion),
        5: ("Reemplazar Rueda", accion),
        6: ("Mostrar Estado", accion),
        0: ("Salir", None)
                    }

    opcion = -1
    while opcion != 0:

        for llave, valor in dict_opciones.items():
            print(f"{llave}: {valor[0]}")

        try:
            opcion = int(input("Opción: "))

        except ValueError:
            print("Ingrese opción válida.")
            opcion = -1

        if opcion != 0 and opcion in dict_opciones.keys():
            if opcion == 1:
                vehiculo = dict_opciones[opcion][1](vehiculos)
            else:
                dict_opciones[opcion][1](vehiculo, opcion)
        elif opcion == 0:
            pass
        else:
            print("Ingrese opción válida.")
            opcion = -1


if __name__ == "__main__":
    main()
