BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[39m'

import time
import random
puntaje = random.randint (5,15)

iniciar_trivia = True
intentos=0

#pantalla de bienvenida
print (CYAN+"Hola amig@, bienvenid@ a mi trivia de cultura general".center(50, "=") +RESET)

print (MAGENTA+"Pondremos a prueba tus conocimientos".center(50, ".") +RESET)

print (GREEN+"\nComenzaras con ",puntaje," puntos, Obtienes 10 puntos por cada pregunta adivinada y pierdes 5 puntos si fallas la pregunta."+RESET)

#verificamos el nombre
while True:
    try:
        nombre = str(input(BLUE+"\nCual es tu nombre: "+RESET))
    except ValueError:
        print(RED+"\nDebes escribir un nombre."+RESET)
        continue
    if len(nombre) <= 0:
        print(RED+"\n¡No ha escrito un nombre ! Inténtelo de nuevo."+RESET)
        continue
    elif len(nombre) >10:
       print(RED+"\n¡Ha escrito un nombre muy largo! Inténtelo de nuevo"+RESET)
    
      
    else:
        break
print(GREEN+"\nHola",nombre+RESET) 
#salimos depues de verificar el nombre


#iniciamos el juego
while iniciar_trivia == True:
  intentos += 1
  
  print("\nIntento número:", intentos)
  input("Presiona Enter para empezar a jugar")
  
  print(MAGENTA+"Hola", nombre.upper(), "responde las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Enter' para enviar tu respuesta:\n"+RESET)
  time.sleep(2)
  print ("1) ¿cual es el simbolo del cobre?\n")
  time.sleep(1)
  print (BLUE+"a) HG ")
  time.sleep(1)
  print ("b) CU")
  time.sleep(1)
  print ("c) O")
  time.sleep(1)
  print ("d) RS"+RESET)
  time.sleep(1)
# Almacenamos la respuesta del usuario en la variable "respuesta_1"
  respuesta_1 = input("\nTu respuesta:\n--> ").lower()

  while respuesta_1 not in ("a", "b", "c", "d"):
        respuesta_1 = input(RED+"\nDebes responder a, b, c o d. Ingresa nuevamente tu respuesta: \n--> "+RESET).lower()

  if respuesta_1 == "a":
     puntaje = puntaje - 5
     print(RED+"\nIncorrecto!", nombre, ", HG no es el simbolo del cobre")
     print("Tu puntaje actual es", puntaje,"\n"+RESET)
  elif respuesta_1 == "c":
      puntaje = puntaje - 5
      print(RED+"\nIncorrecto!", nombre, ", O no es el simbolo del cobre"+RESET)
      print ("Tu puntaje actual es", puntaje,"\n")
  elif respuesta_1 == "d":
      puntaje = puntaje - 5
      print(RED+"\nIncorrecto!", nombre, "RS no es el simbolo del cobre"+RESET)
      print ("\nTu puntaje actual es", puntaje)
  else:
      puntaje = puntaje + 10
      print(GREEN +"\n⭐ Correcto!⭐, Muy bien", nombre,"!\n"+RESET)
      print("Tu puntaje actual es", puntaje)
      time.sleep(2)
 # Pregunta 2
  print ("\n2) ¿Cual fue el primer satelite artificial\n enviado al espacio?\n")
  time.sleep(1)
  print (BLUE+"a) Apollo")
  time.sleep(1)
  print ("b) Sputnik")
  time.sleep(1)
  print ("c) Skilab")
  time.sleep(1)
  print ("d) Explorer"+RESET)
  time.sleep(1)
  time.sleep(2) # Espera 2 segundos antes de continuar.

# Almacenamos la respuesta del usuario en la variable "respuesta_2"
  respuesta_2 = input("\nTu respuesta: \n--> ").lower()

  while respuesta_2 not in ("a", "b", "c", "d"):
    respuesta_2 = input(RED+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: \n--> "+RESET).lower()

  if respuesta_2 == "a":
    puntaje = puntaje - 5
    print(RED+"\nIncorrecto!", nombre, ", Apollo no fue el primer satelite artificial enviado al espacio"+RESET)
    print("\nTu puntaje actual es", puntaje)
  elif respuesta_2 == "d":
    puntaje = puntaje - 5
    print(RED+"\nIncorrecto!", nombre, ",Explorer no fue el primer satelite artificial enviado al espacio\n"+RESET)
    print("\nTu puntaje actual es", puntaje)
  elif respuesta_2 == "c":
    puntaje = puntaje - 5
    print(RED+"\nIncorrecto!", nombre, ",Skilab no fue el primer satelite artificial enviado al espacio\n"+RESET)
    print("\nTu puntaje actual es", puntaje)
  else:
    puntaje = puntaje + 10
    print(GREEN+"\n⭐ Correcto!⭐, Muy bien", nombre,     "!\n"+RESET)
    print("Tu puntaje actual es", puntaje)
    
#Pregunta 3
  print ("\n1) ¿Cuantas cuerdas tiene un violin?\n")
  time.sleep(1)
  print (BLUE+"a) 4")
  time.sleep(1)
  print ("b) 3")
  time.sleep(1)
  print ("c) 5")
  time.sleep(1)
  print ("d) 6"+RESET)
  time.sleep(2) # Espera 2 segundos antes de continuar.

# Almacenamos la respuesta del usuario en la variable "respuesta_3"
  respuesta_3 = input("\nTu respuesta: \n--> ").lower()

  while respuesta_3 not in ("a", "b", "c", "d","z"):
   respuesta_3 = input(RED+"Debes responder a, b, c o d. Ingresa nuevamente tu respuesta: \n--> "+RESET).lower()

  if respuesta_3 == "b":
    puntaje = puntaje - 5
    print(RED+"\nIncorrecto!", nombre, "Totalmente incorrecto! ..."+RESET)
    print("\nTu puntaje actual es", puntaje)
  elif respuesta_3 == "c":
    puntaje = puntaje - 5
    print(RED+"\nIncorrecto!", nombre, "Estubiste cerca"+RESET)
    print("\nTu puntaje actual es", puntaje)
  elif respuesta_3 == "d":
    puntaje = puntaje - 5
    print(RED+"\nIncorrecto!", nombre, "Totalmente incorrecto"+RESET)
    print("\nTu puntaje actual es", puntaje)
  elif respuesta_3 == "z":
    puntaje = puntaje + 999
    print(CYAN+"Sorpresa!", nombre, ",Descubriste el mensaje sopresa secreto y te regalamos 100 puntos"+RESET)
    print("\nTu puntaje actual es", puntaje)
  else:
    puntaje = puntaje + 10
    print(GREEN+"\n⭐ Correcto!⭐, Muy bien", nombre,     "!\n"+RESET)
    print("Tu puntaje actual es", puntaje)

  preguntas =["1.¿Cual es el simbolo del cobre?","2.¿Cual fue el primer satelite artificial enviado al espacio","3.¿Cuantas cuerdas tiene un violin?"]
  
  print(GREEN+"\nImprimiendo todas tus respuestas para obtener tu puntaje final\n"+RESET)
  respuestas= [respuesta_1,respuesta_2,respuesta_3,]
  
  for number in range(0,3):
   print ("\nLa pregunta es: \n", preguntas[number],"\nLa respuesta que marcaste es: ",respuestas[number])
  input (CYAN+"\nPresione enter para continuar"+RESET)
  
  print (GREEN+"Gracias", nombre, " por jugar mi trivia, alcanzaste", puntaje, " puntos"+RESET)
  time.sleep(3)
  print(BLUE+"\n¿Deseas intentar la trivia nuevamente?"+RESET)
  repetir_trivia = input("Ingresa 'si' para repetir, o cualquier tecla para finalizar: ").lower()
  if repetir_trivia != "si":  
   print(GREEN+"\nEspero" ,nombre, "que te lo hayas pasado genial,y hasta pronto!"+RESET)
   iniciar_trivia = False 