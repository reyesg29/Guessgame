import random 
def humanguess():
    number=random.randrange(0,10)
    print(number)

    numero= -1

    while numero!=number:

        numero=int(input("Introduce un numero"))

        if number==numero:
            print(f"Felicidades ganaste, el numero era  {numero}")
        elif numero>number:
            print(f"El numero que escogio es mayor {numero}")
        else:
            print(f"El numero que escogio es menor {numero}")
        

def computerGuess():
    bandera = False
    minimo=0
    maximo=1000
    number=minimo
    

    while(bandera == False):
        if (minimo>number):
            minimo=number
        elif(maximo<number):
            maximo=number
        else:
            number = random.randrange(minimo,maximo) #es el de la computadora
            print (number)
            print("Este es el número en el que pensaste?")
            opc= input("Si -- No:  ").lower()
            if( opc == "no"): #no es el numero
                print("Tu numero es mayor o menor al mio?")
                opc2 = input("Ingresa si es Mayor -- Menor: ").lower()
                if (opc2 == "menor"): #En caso que es menor
                    maximo=number
                else: #En caso que es mayor
                    minimo=number
            else:
                print("El juego se acabo, adivine su numero") # encontro el numero
                bandera = True
                
computerGuess()