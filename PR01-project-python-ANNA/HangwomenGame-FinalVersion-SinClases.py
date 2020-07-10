#!/usr/bin/env python
# coding: utf-8

# # Hangwomen Game

# In[1]:


import random
import os
import emoji


# #### Imprimimos el dibujo de la guillotina para mostrando los fallos del jugador y sabe si está ahoraco o vivo

# In[2]:



vivo = ["    +---+",
        "        |",
        "        |",
        "        |",
        "        |",
        "        |",
        "        |",
        "        |",        
        "   ======"]

ahorcado = ["    +---+",
            "    |   |",
            "    0   |",
            "   /|\  |",
            "    |   |",
            "   / \  |",
            "        |",
            "        |",
            "   ======"]


# #### Iniciamos el juego, donde el jugador deberá adivinar la palabra pensada

# In[3]:


def juego():
    
    #preparar juego#
    
    #Declaramos palabra que el jugador deberá adivinar
    palabras=["COPAZO","IRONHACK","PYTHON","GARBANZOS"]
    palabra=list(random.choice(palabras))
    
    #almacenamos letras que el jugador mencionadas
    letras_todas=[]
    
    #almacenamos contador de fallos
    fallos=1

    #imprimir "_" por cada pablabra secreta, que luego se substituirán por las letras mencionadas que están en la palabra secreta
    resultado= []
    for i in range(len(palabra)):
        resultado.append("_")

    #iniciar juego#
    while True:
        os.system("clear")
        
        #dar bienvenida y imprimir por cada partida el resumen de los fallos y palabras mencionadas
        print("Welcome to 'HangWomen'")
        print("Save the person from a grim fate! Guess each letter of the word to save her. \n")
        print("Let's start! \n")
        print(emoji.emojize(":backhand_index_pointing_down:")) 
        print(f"\n- Hint: your word has {len(palabra)} letters")
        print(f"- Fallos totales:{fallos-1}")
        print(f"- Letras mencionadas:{letras_todas}")


        #visibilidad permanente de fallos en la imagen.
        for i in range(fallos):
            print(ahorcado[i])
        for i in range(len(vivo)-fallos):
            print(vivo[i+fallos])

        print()


        #visibilidad permanente de resultado (letras acerdadas)
        print("   ", end=" ")
        for i in resultado:
            print(i, end=" ")

        print()
        print()

        #comprobamos si jugador ha hacertado palabra o si a temrinado sus intendos
        if resultado== palabra:
            print("YEAH! You've saved the person from a grim fate")
            break

        if fallos>6:
            print("Oops.. She is dead!",emoji.emojize(":skull:"))
            print("your words was","".join(palabra))
            break

        #piensa letra
        while True:
            letra= input("Guess a letter: ")
            letra_jugador=letra.upper()

            #aseguramos que el input sea letra (no espacio u otros elementos) ·error
            if len(letra_jugador) != 1:
                  print("Oops, make sure you chose a word")
            elif letra_jugador in letras_todas:
                  print("Oops, you already mention this word")
            elif letra_jugador not in "ABCDEFGHIJKLMNÑOPQRSTUVWXYZ":
                  print("Oops, make sure you chose a word")
            else:
                letras_todas.append(letra_jugador)
                break

        #validamos letra jugador en palabra y si es correcta la pnemos en la lista (substituyendo guíon)
        for i in range(len(palabra)):
            if palabra[i]==letra_jugador:
                resultado[i]=letra_jugador 

        if letra_jugador not in palabra:
            fallos+=1

        print()
        print()


# In[ ]:


juego()


# In[ ]:




