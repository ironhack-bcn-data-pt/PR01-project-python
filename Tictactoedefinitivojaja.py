class Partida:

    tablero = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    opciones_ganadoras = [["A", "D", "G"], ["B", "E", "H"], ["C", "F", "I"], ["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["A", "E", "I"], ["C", "E", "G"]]
    turno = 0
    fichafacilitada = ["X", "O"]
    j = {}
    histori_partida = []
    partida_terminada = 0

    def __init__(self):
        for i in self.fichafacilitada:
            self.j[i] = Jugadoras(i)
        while self.p_terminada() == 0:
            self.dibuja_tablero()
            self.meter_ficha()


    def dibuja_tablero(self):
        for i in self.tablero:
            print(i)

    def meter_ficha(self):
        self.turno += 1
        jugadora = self.turno % 2
        tirada = input("En qué casilla te gustaría colocar tu ficha {}? ".format(self.fichafacilitada[jugadora]))
        self.j[self.fichafacilitada[jugadora]].histori_tirada.append(tirada)
        self.histori_partida.append(tirada)
        jugada_ok = 0
        for i in range(len(self.tablero)):
            for j in range(len(self.tablero[i])):
                if self.tablero[i][j] == tirada:
                    self.tablero[i][j] = self.fichafacilitada[jugadora]
                    jugada_ok = 1
        if jugada_ok == 0:
            if len(self.histori_partida)>=9:
                print("Ya no quedan casillas libres, la partida ha terminado, habéis empatado. Hay que estar más frescas.")
                self.partida_terminada = 1
            else:
                print("Casilla ocupada, tienes que estar más atenta")

    def p_terminada(self):
        for i in self.fichafacilitada:
            lj = self.j[i].histori_tirada
            lj.sort()
            for j in self.opciones_ganadoras:
                lg = j
                lg.sort()
                if lj == lg:
                    self.partida_terminada = 1
                    print("Felicidades, has ganado <3")
        return self.partida_terminada


class Jugadoras:

    def __init__(self, fichafacilitada):
        self.nombre = input("Quién quiere jugar con las fichas {}? ".format(fichafacilitada))
        self.ficha = fichafacilitada
        self.histori_tirada = []


#Código para arrancar:
#if __name__ == "__main__":
    #game()



p = Partida()
