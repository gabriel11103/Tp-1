import random

print(" B I E N V E N I D O")
print("           AL       ")
print("  JUEGO DE LOS DADOS")

print("                            ")

print("****************************")
print("R E G L A S")
print("****************************")

print("                            ")

print("El juego consta de 2 rondas, la primera se tratara de tirar 3 dados, si los valores son los mismos en los tres "
      "sumas 6 puntos, si solamente 2 dan iguales y uno diferente, ganas la posibilidad de tirar nuevamente ese dado, "
      "en caso que nuevamente salga distinto a los demas, sumas 3 puntos, caso contrario sumas 6")

print("                                                   ")

print("La segunda rondara involucrara su suerte, ya que se tratara de apostar todo sus puntos anteriores y lanzar "
      "nuevamente los dados, solamente que ahora se tomara en cuenta si la suma de los dados es par o impar, el resultado"
      "deberan suponerlo ustedes, ademas podran duplicar sus puntos si todos los dados son de la paridad que eligieron.")

print("                                                 ")

print("por ultimo si en los tres dados sacaste valores diferentes se tomara como 0 puntos para el jugador.")

print("                                      ")

print("!!!!!BUENA SUERTE Y DIVIERTETE!!! ")

print("                                     ")

print("lets Go!¡Vamos a jugar un rato!")

print("               ")

nom1 = input("JUGADOR 1 INGRESE SU NOMBRE: ")
nom2 = input("JUGADOR 2 INGRESE SU NOMBRE: ")

print("               ")

print("°°°°°°°°°°°°°°°°°°°°°°°°°")
print("Es hora de jugar ", nom1)
print("°°°°°°°°°°°°°°°°°°°°°°°°°")

print("               ")

Tirada1 = 0
Tirada2 = 0
tiro_adicional = 0
D1 = random.randint(1, 6)
D2 = random.randint(1, 6)
D3 = random.randint(1, 6)


print("               ")

print("      ¡MUCHA SUERTE!      ")

print("               ")

print("|| ¡PRIMERA RONDA! ||")

print("               ")

################################################################

input("presiona enter para conocer el resultado de tus dados:")

print("               ")

print("Tus resultados son los siguientes: ", D1, ",", D2, ",", D3)

print("----------")

################################################################
# si todos los dados son iguales
if D1 == D2 == D3:
    print("!MUY BIEN!!GANASTE + 6 PUNTOS!")
    print("No tenes tiros adicionales, pasa a la ronda 2")
    Tirada1 = 6
    Tirada2 = 0
else:
    # si todos los dados son diferentes
    if D1 != D2 and D2 != D3 and D1 != D3:
        print("Mala suerte, no ganaste puntos... :(")
        print("No tienes tiros adicionales")
        Tirada1 = 0
        Tirada2 = 0
    else:
        # si el primer dado da diferente a los demas
        if D1 != D2 and D1 != D3:
            print("!Estuviste cerca de tener los tres dados iguales!, pero .... ¡Ahora tienes otra chance!.")
            print("Vuelve a tirar el primer dado!")
            input("Presione enter para tener el valor del tiro adicional")
            tiro_adicional = random. randint(1, 6)
            print("El valor del segundo tiro  es: ", tiro_adicional)
        else:
            # si el segunda dado da diferente a los demas
            if D2 != D1 and D2 != D3:
                print("!Estuviste casi de tener los tres dados iguales!, pero .... ¡Ahora tienes otra chance!.")
                print("Vuelve a tirar el segundo dado!")
                input("Presione enter para tener el valor del tiro adicional")
                tiro_adicional = random. randint(1, 6)
                print("El valor del segundo tiro  es: ", tiro_adicional)
            else:
                # si el tercer dado da diferente a los demas
                if D3 != D1 and D3 != D2:
                    print("!Estuviste casi de tener los tres dados iguales!, pero .... ¡Ahora tienes otra chance!.")
                    print("Vuelve a tirar el Tercer dado!")
                    input("Presione enter para tener el valor del tiro adicional")
                    tiro_adicional = random. randint(1, 6)
                    print("El valor del segundo tiro  es: ", tiro_adicional)
                    print()
                    # si el tiro adicional del dado 2 da igual a los demas
                    if tiro_adicional == D1 and tiro_adicional == D3:
                        print("!FELICITACIONES!. Ahora si ganaste + 6 PUNTOS")
                        Tirada1 = 6
                        Tirada2 = 0
                    else:
                        # si el tiro adicional del dado 3 da igual a los demas
                        if tiro_adicional == D2 and tiro_adicional == D1:
                            print("!FELICITACIONES!. Ahora si ganaste + 6 PUNTOS")
                            Tirada1 = 6
                            Tirada2 = 0
                        else:
                            # si el tiro adicional del dado 1 da igual a los demas
                            if tiro_adicional == D2 and tiro_adicional == D3:
                                print("!FELICITACIONES!. Ahora si ganaste + 6 PUNTOS")
                                Tirada1 = 6
                                Tirada2 = 0

        # si el tiro adicional del dado 1 da diferente a los demas
        if tiro_adicional != D2 and tiro_adicional != D3:
            print("Tuviste mala suerte no dieron iguales")
            print("Ganaste + 3 PUNTOS")
            Tirada1 = 0
            Tirada2 = 3
        else:
            # si el tiro adicional de dado 2 da diferente a los demas
            if tiro_adicional != D1 and tiro_adicional != D3:
                print("Tuviste mala suerte no dieron iguales")
                print("Ganaste + 3 PUNTOS")
                Tirada1 = 0
                Tirada2 = 3
            else:
                # si el tira adicional de dado 3 da  diferente a los demas
                if tiro_adicional != D1 and tiro_adicional != D2:
                    print("Tuviste mala suerte no dieron iguales")
                    print("Ganaste + 3 PUNTOS")
                    Tirada1 = 0
                    Tirada2 = 3
            

print("----------")

resultados_ronda_1_jugador_1 = Tirada1 + Tirada2

input()

print("               ")
print("°°°°°°°°°°°°°°°°°°°°°°°°°")
print("Jugador: ", nom1)
print("Tus puntos totales en esta ronda son: ", resultados_ronda_1_jugador_1)
print("°°°°°°°°°°°°°°°°°°°°°°°°°")
input("Presione enter para siguiente turno")
print("               ")

#################################################################

print("               ")

print("°°°°°°°°°°°°°°°°°°°°°°°°°")
print("Es hora de jugar ", nom2)
print("°°°°°°°°°°°°°°°°°°°°°°°°°")

print("               ")

D1 = random.randint(1, 6)
D2 = random.randint(1, 6)
D3 = random.randint(1, 6)

print("               ")

print("      ¡MUCHA SUERTE!      ")

print("               ")

print("|| ¡PRIMERA RONDA! ||")

print("               ")

################################################################

input("presione enter para conocer tu resultados")

print("               ")

print("Tus resultados son los siguientes: ", D1, ",", D2, ",", D3)

print("----------")

################################################################
# si los tres dado dan iguales
if D1 == D2 == D3:
    print("!MUY BIEN!!GANASTE + 6 PUNTOS!")
    print("No tenes tiros adicionales, pasa a la ronda 2")
    Tirada1 = 6
    Tirada2 = 0
else:
    # si los tres dados dan distinto
    if D1 != D2 and D2 != D3 and D1 != D3:
        print("Mala suerte, no ganaste puntos... :(")
        print("No tienes tiros adicionales")
        Tirada1 = 0
        Tirada2 = 0
    else:
        # si el primer dado da diferente a los demas
        if D1 != D2 and D1 != D3:
            print("!Estuviste cerca de tener los tres dados iguales!, pero .... ¡Ahora tienes otra chance!.")
            print("Vuelve a tirar el primer dado!")
            input("presione enter para tener el valor del tiro adicional")
            tiro_adicional = random. randint(1, 6)
            print("El valor del segundo tiro  es: ", tiro_adicional)
        else:
            # si el segundo dado da diferente a los demas
            if D2 != D1 and D2 != D3:
                print("!Estuviste cerca de tener los tres dados iguales!, pero .... ¡Ahora tienes otra chance!.")
                print("Vuelve a tirar el segundo dado!")
                input("presione enter para tener el valor del tiro adicional")
                tiro_adicional = random. randint(1, 6)
                print("El valor del segundo tiro  es: ", tiro_adicional)
            else:
                # si el tercer dado da diferente a los demas
                if D3 != D1 and D3 != D2:
                    print("!Estuviste cerca de tener los tres dados iguales!, pero .... ¡Ahora tienes otra chance!.")
                    print("Vuelve a tirar el Tercer dado!")
                    input("presione enter para tener el valor del tiro adicional")
                    tiro_adicional = random. randint(1, 6)
                    print("El valor del segundo tiro  es: ", tiro_adicional)
                    print()
                    # si el tiro adicional del dado 2 dai igual a los demas
                    if tiro_adicional == D1 and tiro_adicional == D3:
                        print("!FELICITACIONES!. Ahora si ganaste + 6 PUNTOS")
                        Tirada1 = 6
                        Tirada2 = 0
                    else:
                        # si el tiro adicional del dado 3 dai igual a los demas
                        if tiro_adicional == D2 and tiro_adicional == D1:
                            print("!FELICITACIONES!. Ahora si ganaste + 6 PUNTOS")
                            Tirada1 = 6
                            Tirada2 = 0
                        else:
                            # si el tiro adicional del dado 1 dai igual a los demas
                            if tiro_adicional == D2 and tiro_adicional == D3:
                                print("!FELICITACIONES!. Ahora si ganaste + 6 PUNTOS")
                                Tirada1 = 6
                                Tirada2 = 0

        # si el tiro adicional de dado 1 da diferente a los demas
        if tiro_adicional != D2 and tiro_adicional != D3:
            print("Tuviste mala suerte no dieron iguales")
            print("Ganaste + 3 PUNTOS")
            Tirada1 = 0
            Tirada2 = 3
        else:
            # si el tiro adicional de dado 2 da diferente a los demas
            if tiro_adicional != D1 and tiro_adicional != D3:
                print("Tuviste mala suerte no dieron iguales")
                print("Ganaste + 3 PUNTOS")
                Tirada1 = 0
                Tirada2 = 3
            else:
                # si el tiro adicional de dado 3 da diferente a los demas
                if tiro_adicional != D1 and tiro_adicional != D2:
                    print("Tuviste mala suerte no dieron iguales")
                    print("Ganaste + 3 PUNTOS")
                    Tirada1 = 0
                    Tirada2 = 3


print("----------")

resultados_ronda_1_jugador_2 = Tirada1 + Tirada2

input()

print("               ")
print("°°°°°°°°°°°°°°°°°°°°°°°°°")
print("Jugador: ", nom2)
print("Tus puntos totales en esta ronda son: ", resultados_ronda_1_jugador_2)
print("°°°°°°°°°°°°°°°°°°°°°°°°°")
input("Presione enter para pasar a la etapa final")

print("               ")

if resultados_ronda_1_jugador_1 > resultados_ronda_1_jugador_2:
    print("!!!!!IMPORTANTE!!!!!!")
    print("Parece que", nom1, " va ganando, pero no te rindas", nom2, " la segunda ronda lo decidira todo")
else:
    print("!!!!!IMPORTANTE!!!!!")
    print("Parece que", nom2, " va ganando, pero no te rindas", nom1, " la segunda ronda lo decidira todo")
print()
print("                     ")
print("||  !SEGUNDA RONDA!  ||")
print("                     ")

print("°°°°°°°°°°°°°°°°°°°°°°°°°")
print("Estas Listo?!!!!! ", nom1)
print("°°°°°°°°°°°°°°°°°°°°°°°°°")

print("               ")
D1 = random.randint(1, 6)
D2 = random.randint(1, 6)
D3 = random.randint(1, 6)
dados = D1, D2, D3
suma = D1 + D2 + D3
print("               ")
elementos = ("Par", "Impar")
print("!!Preparate para apostar, los puntos que obtuviste en la anterior ronda fueron:", resultados_ronda_1_jugador_1, "",
      "Tenlos en mente para esta ronda!!")
print(" Es hora de apostar, elije si la suma de los dados es:")

print("\t1- Par\n\t2- Impar")
opcion_nro_jugador1 = int(input('Realiza tu seleccion:'))

opcion_jugador1 = elementos[opcion_nro_jugador1 - 1]
print("Tu eleccion fue:", opcion_jugador1)
print()
puntuacion = 0
par = suma % 2 == 0
impar = suma % 2 >= 0
print("--------------")
print("Los dados que obtuviste fueron =========>", dados)
print("--------------")
print("Su suma fue ============================>", suma)
print("--------------")
if suma % 2 == 0 and opcion_jugador1 == "Par" \
        or suma % 2 != 0 and opcion_jugador1 == "Impar":
    print("Parece que la suerte esta de tu lado, haz logrado sumar el valor mas alto de tus dados a tu puntaje maximo")
    puntuacion = resultados_ronda_1_jugador_1 + max(dados)
else:
    print("Lo lamento, parece que los dados no estan de tu parte......", nom1)
    puntuacion = resultados_ronda_1_jugador_1 - min(dados)

print()
if D1 % 2 == 0 and D2 % 2 == 0 and D3 % 2 == 0 and opcion_jugador1 == "Par" or \
        D1 % 2 != 0 and D2 % 2 != 0 and D3 % 2 != 0 and opcion_jugador1 == "Impar":
    print("Parece que los milagros te ocurren, la paridad que elegiste es igual a la de tus dados, duplicas el resultado")
    bonificacion = puntuacion * 2
else:
    print("Tanta suerte no tuviste, no ganaste una bonificacion")

    bonificacion = puntuacion

print()
resultados_ronda_2_jugador_1 = bonificacion
# resultados del jugador 1 en la ronda 2
print("tus resultados", nom1, " en esta ronda fueron", resultados_ronda_2_jugador_1)
input('Presiona enter para continuar con el jugador 2')

print("°°°°°°°°°°°°°°°°°°°°°°°°°")
print("Estas Listo?!!!!! ", nom2)
print("°°°°°°°°°°°°°°°°°°°°°°°°°")

print("               ")
D1 = random.randint(1, 6)
D2 = random.randint(1, 6)
D3 = random.randint(1, 6)
dados = D1, D2, D3
suma = D1 + D2 + D3
print("               ")
elementos = ("Par", "Impar")
print("!!Preparate para apostar, los puntos que obtuviste en la anterior ronda fueron:", resultados_ronda_1_jugador_2, "",
      "Tenlos en mente para esta ronda!!")
print(" Es hora de apostar, elije si la suma de los dados es:")

print('\t1- Par\n\t2- Impar')
opcion_nro_jugador2 = int(input('Realiza tu seleccion:'))

opcion_jugador2 = elementos[opcion_nro_jugador2 - 1]
print("Tu eleccion fue:", opcion_jugador2)
print()
puntuacion = 0
par = suma % 2 == 0
impar = suma % 2 >= 0
print("--------------")
print("Los dados que obtuviste fueron =========>", dados)
print("--------------")
print("Su suma fue ============================>", suma)
print("--------------")

# si los dados dan de acuerdo a la eleccion.
if suma % 2 == 0 and opcion_jugador2 == "Par" \
        or suma % 2 != 0 and opcion_jugador2 == "Impar":
    print("Parece que la suerte esta de tu lado, haz logrado sumar el valor mas alto de tus dado a tu puntaje maximo")
    puntuacion = resultados_ronda_1_jugador_2 + max(dados)
else:
    print("Lo lamento, parece que los dados no estan de tu parte......", nom2)
    puntuacion = resultados_ronda_1_jugador_2 - min(dados)

print()
# para la paridad de los dados
if D1 % 2 == 0 and D2 % 2 == 0 and D3 % 2 == 0 and opcion_jugador2 == "Par" or \
        D1 % 2 != 0 and D2 % 2 != 0 and D3 % 2 != 0 and opcion_jugador2 == "Impar":
    print("Parece que los milagros te  ocurren, la paridad que elegiste es igual a la de tus dados, duplicas el resultado")
    bonificacion = puntuacion * 2
else:
    print("Tanta suerte no tuviste, no ganaste una bonificacion")

    bonificacion = puntuacion

print()
resultados_ronda_2_jugador_2 = bonificacion
# resultados del jugador 2 de la ronda 2
print("tus resulados", nom2, " en esta ronda fueron", resultados_ronda_2_jugador_2)
print("--------------")
input()
print("Llego la hora del conteo final")
print()
# en caso de que ambos empataran.
if resultados_ronda_2_jugador_1 == resultados_ronda_2_jugador_2:
    print("¡¡¡Parece que empataron, ambos tuvieron el mismo puntaje final!!! ")
else:
    # En caso que el jugador 1 gane el juego.
    if resultados_ronda_2_jugador_1 > resultados_ronda_2_jugador_2:
        print("Enhorabuena", nom1, "has ganado el juego, por otro lado, mala suerte", nom2, " parece que no ganaste, suerte para la proxima")
    else:
        print("Enhorabuena", nom2, "has ganado el juego, por otro lado, mala suerte", nom1, " parece que no ganaste, suerte para la proxima")
print("los resultados de ambos fueron:")
print()
# resultados de ambos jugadores.
print("los resultados de", nom1, "fueron", resultados_ronda_2_jugador_1)
print()
print("los resultados de", nom2, "fueron", resultados_ronda_2_jugador_2)

print("**************************************************")
print("!!!!!Nos vemos la proxima vez que quieran jugar!!!")
print("**************************************************")
input()
