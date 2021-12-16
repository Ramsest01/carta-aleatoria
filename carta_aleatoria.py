#Proyecto I - Simulacion y Modelos
#
#Integrantes 
#Estefano Ramos 
#V-26.778.542
#
#Wuilmer Pulgar
#V-26625192

import random

#Funcion que imprime en consola, el resultado de una simulacion de escojer de forma aleatoria una de las 40 cartas de la baraja espanola
def carta_Aleatoria():

    cartas={
        0:"Uno",
        1:"Dos",
        2:"Tres",
        3:"Cuatro",
        4:"Cinco",
        5:"Seis",
        6:"Siete",
        7:"Diez",
        8:"Once",
        9:"Doce"
    }

    pintas={
        0:"Espadas",
        1:"Oro",
        2:"Copas",
        3:"Bastos"
    } 

    #La probabilidad de que salga una carta de la baraja es 1/40
    #La probabilidad de que sea un numero del 1-7 o del 10-12 es de 1/10
    #La probbabilidad de de cada pinta es de 1/4
    #Como el numero de una carta es "independiente" de la pinta 
    # o que  todas las pintas entan relacionadas a los mismos numeros
    #podemos decir que 
    #La probabilidad de sacar una carta es de 1/10 * 1/4 = 1/40

    print(f"Tu carta es: El { cartas.get( random.randint(0, 9) ) } de { pintas.get( random.randint(0, 3) ) }")

carta_Aleatoria()