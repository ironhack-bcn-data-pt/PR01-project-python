{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Tic Tac Toe Blanca Monreal - Data Analytics - Ironhack June 2020"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Explicación clase Partida:\n",
    "\n",
    "Atributos:\n",
    "- Tenemos un tablero vacío formado por una lista de listas\n",
    "- Hemos guardado en una lista de listas todas las combinaciones de coordenadas que crearían una ganadora\n",
    "- Tenemos las fichas guardadas también como atributos\n",
    "- Hemos creado como atributos ciertas variables que vamos a ir necesitando a lo largo de la ejecución\n",
    "\n",
    "Métodos:\n",
    "- Init (por defecto): se asigna una de las fichas disponibles a cada jugadora e indica que hasta que no se termine la partida, se continua ejecutando las acciones descritas en meter_ficha.\n",
    "- dibuja_tablero: se despliega el tablero con las actualizaciones de las jugadas\n",
    "- meter_ficha: vemos a quién le toca jugar a través del Operator; se recoge la referencia de la coordenada donde la jugadora quiere colocar ficha; se guarda la coordenada en un histórico de tiradas y se valida que la tirada en concreto sea posible.\n",
    "- partida_terminada: se contrasta si la lista historial de coordenadas es igual a alguna de listas con la de opciones_ganadoras, ordenadas alfabéticamente para contrastarlas eficientemente."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "ExecuteTime": {
     "start_time": "2020-07-11T07:21:09.062Z"
    },
    "code_folding": []
   },
   "outputs": [],
   "source": [
    "class Partida:\n",
    "\n",
    "    tablero = [[\"A\", \"B\", \"C\"], [\"D\", \"E\", \"F\"], [\"G\", \"H\", \"I\"]]\n",
    "    opciones_ganadoras = [[\"A\", \"D\", \"G\"], [\"B\", \"E\", \"H\"], [\"C\", \"F\", \"I\"], [\"A\", \"B\", \"C\"], [\"D\", \"E\", \"F\"], [\"G\", \"H\", \"I\"], [\"A\", \"E\", \"I\"], [\"C\", \"E\", \"G\"]]\n",
    "    turno = 0\n",
    "    fichafacilitada = [\"X\", \"O\"]\n",
    "    j = {}\n",
    "    histori_partida = []\n",
    "    partida_terminada = 0\n",
    "\n",
    "    def __init__(self):\n",
    "        for i in self.fichafacilitada:\n",
    "            self.j[i] = Jugadoras(i)\n",
    "        while self.p_terminada() == 0:\n",
    "            self.dibuja_tablero()\n",
    "            self.meter_ficha()\n",
    "\n",
    "\n",
    "    def dibuja_tablero(self):\n",
    "        for i in self.tablero:\n",
    "            print(i)\n",
    "\n",
    "    def meter_ficha(self):\n",
    "        self.turno += 1\n",
    "        jugadora = self.turno % 2\n",
    "        tirada = input(\"En qué casilla te gustaría colocar tu ficha {}? \".format(self.fichafacilitada[jugadora]))\n",
    "        self.j[self.fichafacilitada[jugadora]].histori_tirada.append(tirada)\n",
    "        self.histori_partida.append(tirada)\n",
    "        jugada_ok = 0\n",
    "        for i in range(len(self.tablero)):\n",
    "            for j in range(len(self.tablero[i])):\n",
    "                if self.tablero[i][j] == tirada:\n",
    "                    self.tablero[i][j] = self.fichafacilitada[jugadora]\n",
    "                    jugada_ok = 1\n",
    "        if jugada_ok == 0:\n",
    "            if len(self.histori_partida)>=9:\n",
    "                print(\"Ya no quedan casillas libres, la partida ha terminado, habéis empatado. Hay que estar más frescas.\")\n",
    "                self.partida_terminada = 1\n",
    "            else:\n",
    "                print(\"Casilla ocupada, tienes que estar más atenta\")\n",
    "\n",
    "    def p_terminada(self):\n",
    "        for i in self.fichafacilitada:\n",
    "            lj = self.j[i].histori_tirada\n",
    "            lj.sort()\n",
    "            for j in self.opciones_ganadoras:\n",
    "                lg = j\n",
    "                lg.sort()\n",
    "                if lj == lg:\n",
    "                    self.partida_terminada = 1\n",
    "                    print(\"Felicidades, has ganado <3\")\n",
    "        return self.partida_terminada"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Explicación clase Jugadoras:\n",
    "Atributos:\n",
    "- No hay\n",
    "\n",
    "Métodos:\n",
    "- Init (por defecto): se recoge el nombre de cada jugadora; se le asigna una de las fichas creadas en el init de partida y una lista de histótico de tiradas.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "ExecuteTime": {
     "start_time": "2020-07-11T07:21:09.668Z"
    }
   },
   "outputs": [],
   "source": [
    "class Jugadoras:\n",
    "\n",
    "    def __init__(self, fichafacilitada):\n",
    "        self.nombre = input(\"Quién quiere jugar con las fichas {}? \".format(fichafacilitada))\n",
    "        self.ficha = fichafacilitada\n",
    "        self.histori_tirada = []\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Activación del juego:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "ExecuteTime": {
     "start_time": "2020-07-11T07:21:10.688Z"
    }
   },
   "outputs": [],
   "source": [
    "p = Partida()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.6"
  },
  "toc": {
   "base_numbering": 1,
   "nav_menu": {},
   "number_sections": true,
   "sideBar": true,
   "skip_h1_title": false,
   "title_cell": "Table of Contents",
   "title_sidebar": "Contents",
   "toc_cell": false,
   "toc_position": {},
   "toc_section_display": true,
   "toc_window_display": false
  },
  "varInspector": {
   "cols": {
    "lenName": 16,
    "lenType": 16,
    "lenVar": 40
   },
   "kernels_config": {
    "python": {
     "delete_cmd_postfix": "",
     "delete_cmd_prefix": "del ",
     "library": "var_list.py",
     "varRefreshCmd": "print(var_dic_list())"
    },
    "r": {
     "delete_cmd_postfix": ") ",
     "delete_cmd_prefix": "rm(",
     "library": "var_list.r",
     "varRefreshCmd": "cat(var_dic_list()) "
    }
   },
   "types_to_exclude": [
    "module",
    "function",
    "builtin_function_or_method",
    "instance",
    "_Feature"
   ],
   "window_display": false
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
