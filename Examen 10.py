import os
import json # Importamos el módulo json, que nos proporciona funciones para trabajar con archivos JSON
import random
import time
from colorama import Fore, init

# Funciones de uso general

def clear_console():
    '''Limpiar la consola'''
    os.system('cls')

def guardar_en_archivo(): # Función finalizada


   archivo_escritura = open('bbdd_cinema.json', 'w')  # Abrimos el archivo en modo escritura ('w').  
   json.dump(bbdd_cinema, archivo_escritura) # Se “vuelcan” los datos de un objeto Python (la lista bbdd_cinema) en un archivo en formato JSON.
   archivo_escritura.close() # cerramos el archivo para asegurarnos de que los datos se escriban correctamente y liberar los recursos asociados al archivo.

def main_menu(): # Función finalizada
    """Esta función muestra el menú principal y en función 
    de la elección del usuario deriva a las funciones correspondientes"""
    print ()
    
    init ()
    print(Fore.BLUE + "*" * 50)
    print (" Bienvenidos a Cinema ".center(50,"-"))
    print (" Menú Principal ".center(50,"-"))
    print("*" * 50)
    print (Fore.RESET + " ")

    print ("1 - Para ABM de películas")
    print ("2 - Calificación de películas")
    print ("3 - Reportes y estadísticas")
    print ("4 - Salir")
    opcion = input('Ingrese su opción (1 -4): ')
    match opcion:
        case "1":
            abm_peliculas ()
        case "2":
            calificacion_peliculas()
        case "3":
            reportes_estadisticas()
        case "4":
            print ()
            print (" Hasta luego ".center (50,"-"))
            print ()
            time.sleep(5) # Espera unos segundos
            clear_console() # Limpia la consola
        case _:
            print ("Opcón inválida, inténtelo de nuevo")
            main_menu ()

def solicitar_dato (mensaje):
    """Esta función valida que ingrese algún dato"""
    while True:
        entrada = input (mensaje)
        if entrada.strip ():
            return entrada
        else:
            print ("Entrada inválida, por favor ingrese un valor no vacío")

def solicitar_numero(mensaje):
    """Esta función valida que ingrese algún número"""
    while True:
        entrada = input(mensaje)
        if entrada.strip():  # Verifica que la entrada no esté vacía
            try:
                numero = int(entrada)  # Intenta convertir la entrada a un número
                return numero
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número.")
        else:
            print("Entrada inválida. Por favor, ingrese un valor no vacío.")

# Funciones del menú principal

def abm_peliculas (): # Función finalizada
    """Esta función muestra el menú de ABM y en función 
    de la elección del usuario deriva a las funciones correspondientes"""
    print ()
    from colorama import Fore, init
    init ()
    print(Fore.RED + "*" * 50)
    print (" Menú de ABM ".center(50,"-"))
    print("*" * 50)
    print (Fore.RESET + " ")

    print ("1 - Para agregar película")
    print ("2 - Modificar película existente")
    print ("3 - Baja de película")
    print ("4 - Volver")
    opcion = input('Ingrese su opción: ')
    match opcion:
        case "1":
            alta_pelicula ()
        case "2":
            modificar_pelicula()
        case "3":
            baja_pelicula()
        case "4":
            main_menu ()
        case _:
            print ("Opcón inválida, inténtelo de nuevo")
            abm_peliculas (bbdd_cinema)

def calificacion_peliculas (): # Función finalizada
    """La calificación de títulos se realizará de manera aleatoria en tandas de 10 iteraciones. Se irán
listando al azar la ficha completa de una película. Las calificaciones posibles serán números del 1 al 10, 
con una opción para saltar la película si el usuario no desea calificarla.
La forma de mostrar los datos y los mensajes al usuario, quedan a criterio del equipo de desarrollo."""

    print ()
    from colorama import Fore, init
    init ()
    print(Fore.YELLOW + "*" * 50)
    print (" Calificación de películas ".center(50,"-"))
    print("*" * 50)
    print()
    print ("Vas a ver distintas películas para que puedas calificar")
    print (Fore.RESET + " ")

    maximo_id = bbdd_cinema[int (len (bbdd_cinema) -1)]["id"]
#    print (maximo_id)
    encontrado = False
    indice = 0
    numero_aleatorio = int (random.randint(0, maximo_id))

    while indice < len(bbdd_cinema) and encontrado == False:
        if bbdd_cinema[indice]["id"] == numero_aleatorio:
            print()
            print(f"{bbdd_cinema[indice]["id"]} - {bbdd_cinema[indice]["Titulo"]} - {bbdd_cinema[indice]["Calificacion"]}")            
            desea_calificar = input ("Desea calificar esta película? S / N : ").upper()
            print()

            if desea_calificar == "S":
                nueva_calificion = int ( input("Ingrese calificación de 1 a 10: "))

                while nueva_calificion < 1 or nueva_calificion > 10:
                    print("Calificación no válida. Intente de nuevo.")
                    nueva_calificion = int ( input("Ingrese calificación de 1 a 10: "))

                if bbdd_cinema[indice]["Calificacion"] == 0:
                    bbdd_cinema [indice]["Calificacion"] = nueva_calificion
                else:
                    bbdd_cinema_previo = bbdd_cinema [indice]["Calificacion"]
                    bbdd_cinema [indice]["Calificacion"] = (bbdd_cinema [indice]["Calificacion"] + bbdd_cinema_previo) / 2

                guardar_en_archivo ()
            encontrado = True
       
        indice = indice + 1

#    if encontrado == False:
#        calificacion_peliculas ()

    continua_calificacion = input ("Desea seguir calificando películas? S / N : ").upper()
    print()
    if continua_calificacion == "S":
        calificacion_peliculas ()
    else:
        abm_peliculas()

def reportes_estadisticas (): # Función en desarrolllo
    """Esta función muestra el menú de Reportes y Estadísticas y en función 
    de la elección del usuario deriva a las funciones correspondientes"""
    print ()
    from colorama import Fore, init
    init ()
    print(Fore.RED + "*" * 50)
    print (" Menú de Reportes y estadísticas ".center(50,"-"))
    print("*" * 50)
    print (Fore.RESET + " ")
    print ()

    print ("1 - Listado de películas")
    print ("2 - Películas de mayor puntaje")
    print ("3 - Volver")
    opcion = input('Ingrese su opción: ')
    match opcion:
        case "1":
            listado_peliculas ()
        case "2":
            pelicula_mayor_puntaje()
        case "3":
            main_menu ()
        case _:
            print ("Opcón inválida, inténtelo de nuevo")
            abm_peliculas ()

# Funciones del menú ABM

# Funciones del menú ABM - Modificar

def alta_pelicula (): # Función finalizada
    """Esta función permite dar de alta una película
    CUIDADO QUE ID NO SE MODIFICA POR EL USUARIO"""
    generos_permitidos = ["Acción", "Animación", "Comedia", "Drama", "Ciencia ficción", "Terror", "Suspenso", "Romántica","fin"] # Agrego "fin" para terminar el bucle
    clasificaciones_permitidas = ["ATP", "PG", "PG-13", "R", "NC-17"]
    print ()
    from colorama import Fore, init
    init ()
    print(Fore.RED + "*" * 50)
    print (" Alta de película ".center(50,"-"))
    print("*" * 50)
    print (Fore.RESET + " ")
    print ()
    ingreso = "S"
    contador = 0
    while ingreso == "S":
        contador += 1
 #      Genera el ID de la próxima pelicula
        id_pelicula_a_agregar = bbdd_cinema[int (len (bbdd_cinema) -1)]["id"] + 1

        titulo_a_agregar = solicitar_dato("Ingrese el título de la película: ").upper()

        # Validación del género
        print("Géneros permitidos: Acción, Animación, Comedia, Drama, Ciencia ficción, Terror, Suspenso, Romántica")
        
        genero_a_agregar = [] # Creamos una lista vacía para almacenar los datos ingresados
        while True:
            dato = solicitar_dato("Ingresa un dato (o 'fin' para terminar): ")
            while dato not in generos_permitidos:
                print("Género no válido. Intente de nuevo.")
                dato = input("Ingrese el género de la película: ")
            if dato.lower() == 'fin':
                break  # Terminamos el bucle si el usuario ingresa 'fin'

            genero_a_agregar.append(dato)  # Agregamos el dato a la lista


        duracion_a_agregar = solicitar_numero("Ingrese la duración en minutos: ")
        sinopsis_a_agregar = solicitar_dato("Ingrese la sinopsis de la película: ")
        pais_origen_a_agregar = solicitar_dato("Ingrese el país de origen: ")
        idioma_a_agregar = solicitar_dato("Ingrese el idioma: ")
        calificacion_a_agregar = int (0)


        disponible_a_agregar = solicitar_dato('Ingrese si el título se encuentra disponible (True) o no (False): ').capitalize()
        while disponible_a_agregar != "True" and nuevo_valor != "False":  
            nuevo_valor = solicitar_dato ("++ Dato Incorrecto ++ Ingres True o False: ").capitalize ()

        # Validación de la clasificación
        print("Clasificaciones permitidas: ATP, PG, PG-13, R, NC-17")
        clasificacion_a_agregar = solicitar_dato("Ingrese la clasificación de la película: ").upper()
        while clasificacion_a_agregar not in clasificaciones_permitidas:
            print("Clasificación no válida. Intente de nuevo.")
            clasificacion_a_agregar = solicitar_dato("Ingrese la clasificación de la película: ").upper()
        
        pelicula_a_agregar = { "id" : id_pelicula_a_agregar,
                                "Titulo"  : titulo_a_agregar,
                                "Genero" : genero_a_agregar,
                                "Duracion" : duracion_a_agregar,
                                "Sinopsis" : sinopsis_a_agregar,
                                "Pais de origen" : pais_origen_a_agregar,
                                "Idioma" : idioma_a_agregar,
                                "Clasificacion" : clasificacion_a_agregar,
                                "Calificacion" : calificacion_a_agregar,
                                "Disponible" : disponible_a_agregar,
                                }
        bbdd_cinema.append  (pelicula_a_agregar)
        print ()
        guardar_en_archivo()
        print ("Ingresó correctamente ", titulo_a_agregar , "al catálogo")
        print ()
        ingreso = input ("Ingrese ´S´ para continuar o ´N´ para fianlizar: ").upper ()
    print ("Agregaste" , contador, "películas al catálogo")

    #Solo para priuebas va esta parte, despues hay que ver como agregarla al diccionario

    print (pelicula_a_agregar)
    print ()
    time.sleep (2)
    abm_peliculas ()    
    
def modificar_pelicula (): # Función finalizada
    """Esta función abre al usuario el menún para Modificar Películas"""
    print ()
    from colorama import Fore, init
    init ()
    print(Fore.GREEN + "*" * 50)
    print (" Modificar pélicula existente ".center(50,"-"))
    print("*" * 50)
    print (Fore.RESET + " ")
    print ()
    print ("1 - Buscar po ID")
    print ("2 - Buscar por Título")
    print ("3 - Volver")
    opcion = input('Ingrese su opción: ')
    match opcion:
        case "1":
            id_buscar = int(input("ID a buscar: "))
            modificar_pelicula_por_id (id_buscar)
        case "2":
            modificar_pelicula_por_titulo ()
        case "3":
            abm_peliculas ()
        case _:
            print ("Opcón inválida, inténtelo de nuevo")
            abm_peliculas ()

def modificar_pelicula_por_id (id): # Fuunción finalizada
    """Esta funcione permite cambiar algun dato de la lista de películas, tiene que tener 
    como dato de ingreso es el ID de la pelicula y luego da un menú con todos los campos que se puedena cambiar.
    Lo único que no permite cambiar es la calificación, ya que es en base a los usuarios"""
# Defino los generos y clasificaciones válidas
    generos_permitidos = ["Acción", "Animación", "Comedia", "Drama", "Ciencia ficción", "Terror", "Suspenso", "Romántica","fin"] # Agrego fin para salir del bucle
    clasificaciones_permitidas = ["ATP", "PG", "PG-13", "R", "NC-17"]

    encontrado = False
    for peli in bbdd_cinema:
        if peli ["id"] == id:
            encontrado = True
            print ()
            print ("Hemos encontrado la película que deseas modificar, el contenido actual es : ")
            print (peli)
            print ()
            print ("¿Qué deseas modificar?")
            print ("1 - Título")
            print ("2 - Género")
            print ("3 - Duración")
            print ("4 - Sinópsis")
            print ("5 - País de origen")
            print ("6 - Idioma")
            print ("7 - Clasificación")
            print ("8 - Disponible")
            print ("9 - Volver")
            opcion = input('Ingrese su opción: ')
            print ()
            match opcion:
                case "1":
                    print ("El dato actual es: ", peli ["Titulo"])
                    print ()
                    nuevo_valor = solicitar_dato('Ingrese El título modificado: ').upper()                
                    peli ["Titulo"] = nuevo_valor       
                case "2":
                    # Validación del género
                    print ()
                    print ("El dato actual es: ", peli ["Genero"])
                    print () 
                    print("Géneros permitidos: Acción, Animación, Comedia, Drama, Ciencia ficción, Terror, Suspenso, Romántica")
                    genero = [] # Creamos una lista vacía para almacenar los datos ingresados

                    # Pedimos al usuario que ingrese los datos uno por uno

                    while True:
                        dato = solicitar_dato("Ingresa un dato (o 'fin' para terminar): ")
                        while dato not in generos_permitidos:
                            print("Género no válido. Intente de nuevo.")
                            dato = solicitar_dato("Ingrese el género de la película: ")
                        if dato.lower() == 'fin':
                            break  # Terminamos el bucle si el usuario ingresa 'fin'

                        genero.append(dato)  # Agregamos el dato a la lista

            
                    peli ["Genero"] = genero
                case "3":
                    print ("El dato actual es: ", peli ["Duracion"])
                    print ()
                    nuevo_valor = solicitar_numero('Ingrese la duración modificada: ')      
                    peli ["Duracion"] = nuevo_valor
                case "4":
                    print ("El dato actual es: ", peli ["Sinopsis"])
                    print ()
                    nuevo_valor = solicitar_dato('Ingrese la sinópsis modificada: ')  
                    peli ["Sinopsis"] = nuevo_valor
                case "5":
                    nuevo_valor = solicitar_dato('Ingrese el país de origen modificado: ')  
                    peli ["Pais de origen"] = nuevo_valor
                case "6":
                    print ("El dato actual es: ", peli ["Idioma"])
                    print ()
                    nuevo_valor = solicitar_dato('Ingrese el idioma modificado: ')  
                    peli ["Idioma"] = nuevo_valor
                case "7":
                # Validación de la clasificación
                    print ("El dato actual es: ", peli ["Clasificacion"])
                    print ()
                    print("Clasificaciones permitidas: ATP, PG, PG-13, R, NC-17")
                    nuevo_valor = input("Ingrese la clasificación de la película modificada: ").upper()
                    while nuevo_valor not in clasificaciones_permitidas:
                        print("Clasificación no válida. Intente de nuevo.")
                        nuevo_valor = solicitar_dato("Ingrese la clasificación de la película: ").upper()
                    peli ["Clasificacion"] = nuevo_valor
                case "8":
                    print ("El dato actual es: ", peli ["Disponible"])
                    print ()
                    nuevo_valor = solicitar_dato('Ingrese si el título se encuentra disponible (True) o no (False): ').capitalize()
                    while nuevo_valor != "True" and nuevo_valor != "False":  
                        nuevo_valor = solicitar_dato ("++ Dato Incorrecto ++ Ingres True o False: ").capitalize ()
                    peli ["Disponible"] = nuevo_valor                
                case "9":
                    print ("Volvemos al menú ABM")
                    time.sleep (2)
                    abm_peliculas ()                          
                case _:
                    print ("Opcón inválida, inténtelo de nuevo")
                    abm_peliculas ()
            print ()
            guardar_en_archivo()
            print("Se realizó el cambio solicitado")
            print ()
            print (peli)
            print ()
            abm_peliculas ()
    
#Si no se encontró el ID
    if encontrado == False:
        print ()
        print(f'El ID {id} no existe en la lista de productos.')
        modificar_pelicula ()

def modificar_pelicula_por_titulo ():  # Función finalizada
    """Esta funcione permite cambiar algun dato de la lista de películas, tiene que tener 
    como dato de ingreso es el Título de la pelicula (o una parte). HArá un listado de peliculas y pedirá que ingrese el ID correspondiente
    Lo único que no permite cambiar es la calificación, ya que es en base a los usuarios"""

    titulo_a_buscar = input("Ingrese el Título a buscar: ").upper() # Puede ingresar una palabra y dará una lista con todas las peliculas que contenga esa palabra
    lista_de_encontrados = [] # Creo una nueva lista con las coincidencias
    for peli in bbdd_cinema:
        if titulo_a_buscar in peli["Titulo"]:
            lista_de_encontrados.append (peli)
    
    if len(lista_de_encontrados) == 0:
        print ()
        print ("*** No se encontró la película ***")
        time.sleep (2)
        abm_peliculas()

    print ()
    print ("|  ID  |            Título             |   Género   ") # Encabezados de la tabla
    print ("+------+-------------------------------+------------------------> ") # Línea divisoria

    # Iterar sobre los datos e imprimir cada fila
    for i in lista_de_encontrados:
        print(f"| {i['id']:4} | {i['Titulo']:28}  | {i['Genero']}")
    print ()
    indice_seleccionado = int(input ("Indique el índice de la pelicula a modificar: "))
    modificar_pelicula_por_id (indice_seleccionado)

def baja_pelicula ():  # Función finalizada

    """Esta función abre al usuario el menún para dar de baja Películas"""
    print ()
    from colorama import Fore, init
    init ()
    print(Fore.GREEN + "*" * 50)
    print (" Baja de pélicula existente ".center(50,"-"))
    print("*" * 50)
    print (Fore.RESET + " ")
    print ()
    print ("1 - Buscar po ID")
    print ("2 - Buscar por Título")
    print ("3 - Volver")
    opcion = input('Ingrese su opción: ')
    match opcion:
        case "1":
            id_buscar = int(input("ID a buscar: "))
            baja_pelicula_por_id (id_buscar)
        case "2":
            baja_pelicula_por_titulo ()
        case "3":
            abm_peliculas ()
        case _:
            print ("Opcón inválida, inténtelo de nuevo")
            abm_peliculas ()

# Funciones del menú ABM - Baja

def baja_pelicula_por_id (id): # Función finalizada
    """Esta función permite eliminar una película de la lista películas, tiene que tener 
    como dato de ingreso es el ID de la pelicula"""
    encontrado = False
    for peli in bbdd_cinema:
        if peli ["id"] == id:
            print ()
            print ("La película que deseas dar de baja es:")
            print ("Título: " , peli ["Titulo"])
            print ("Género: ", peli ["Genero"])
            print ("Pais de origen: ", peli ["Pais de origen"])     
            print()       
            validador = input ("Escriba S para dar de baja o N para volver: ").upper()
            if validador == "S":
                bbdd_cinema.remove (peli)
                encontrado = True
                print ()
                print ("La película se ha eliminado")
                print ()
                guardar_en_archivo ()
                time.sleep (2)
               
            baja_pelicula ()

    if encontrado == False:
        print ()
        print ("La pelicula no se encontró")
        print()
        baja_pelicula ()
       

def baja_pelicula_por_titulo (): # Función finalizada
    """Esta funcione permite eliminar una pelicula de la lista de películas, tiene que tener 
    como dato de ingreso es el Título de la pelicula"""

    titulo_a_buscar = input("Ingrese el Título a dar de baja: ").upper() # Puede ingresar una palabra y dará una lista con todas las peliculas que contenga esa palabra
    lista_de_encontrados = [] # Creo una nueva lista con las coincidencias
    for peli in bbdd_cinema:
        if titulo_a_buscar in peli["Titulo"]:
            lista_de_encontrados.append (peli)
    
    if len(lista_de_encontrados) == 0:
        print ()
        print ("*** No se encontró la película ***")
        time.sleep (2)
        baja_pelicula ()

    print ()
    print ("|  ID  |            Título             |   Género   ") # Encabezados de la tabla
    print ("+------+-------------------------------+------------------------> ") # Línea divisoria

    # Iterar sobre los datos e imprimir cada fila
    for i in lista_de_encontrados:
        print(f"| {i['id']:4} | {i['Titulo']:28}  | {i['Genero']}")
    print ()
    indice_seleccionado = int(input ("Indique el índice de la pelicula a dar de baja: "))
    baja_pelicula_por_id (indice_seleccionado)

# Funciones del menú Reportes y estadísticas

def listado_peliculas (): # Función finalizada
    """ Lista las películas de la bas, pone el ID, Título, Duración, Calificación y Género"""
    print ()
    print ("|  ID  |            Título            | Duración | Calificación |   Género   ") # Encabezados de la tabla
    print ("+------+------------------------------+-----------+-------------+------------------------> ") # Línea divisoria

    # Iterar sobre los datos e imprimir cada fila
    for i in bbdd_cinema:
        print(f"| {i['id']:4} | {i['Titulo']:28} | {i['Duracion']:8} | {i['Calificacion']:12} | {i['Genero']}")
    print ()
    
    time.sleep (3)
    main_menu()


def pelicula_mayor_puntaje (): # Función finalizada
    print (" función en desarrollo") 
    """ Esta función ordena en una nueva lista.
    sorted(lista, key=lambda x: x['edad']) ordena la lista utilizando la clave Calificacion de cada diccionario como 
    el criterio de orden y lambda x: x[Calificacion] define una función lambda que toma un diccionario x y devuelve 
    el valor de la clave Calificacion de ese diccionario. Esta función lambda se utiliza como el argumento key de sorted(). 
    reverse=True especifica que queremos ordenar de mayor a menor.
    """
    
    listado_ordenado_por_puntaje = sorted(bbdd_cinema, key=lambda x:x ["Calificacion"], reverse= True)

    print ()
    print ("|  ID  |            Título            | Duración | Calificación |   Género   ") # Encabezados de la tabla
    print ("+------+------------------------------+-----------+-------------+------------------------> ") # Línea divisoria

    # Iterar sobre los datos e imprimir cada fila
    for i in listado_ordenado_por_puntaje:
        print(f"| {i['id']:4} | {i['Titulo']:28} | {i['Duracion']:8} | {i['Calificacion']:12} | {i['Genero']}")
    print ()
# Para imprimir barra de disponibilidad
    si = 0
    no = 0
    for i in bbdd_cinema:
        if i ["Disponible"] == "True":
            si = si + 1

        else:
            no = no + 1
    from colorama import Fore, init
    init ()
    print(Fore.CYAN)

    disponible_v = int((si / (si+no))*100)
    disponible_f = int (100-disponible_v)
    barra = '#' * disponible_v + '-' * disponible_f
    print(f"[{barra}] {disponible_v:.2f}% Disponible")
    print (Fore.RESET + " ")

    ir_menu_ppal = input ("Ponga S para ir al menu: ")
    if ir_menu_ppal != "":
        main_menu ()
    else:
        main_menu ()


# ******* Acá comienza el programa principal ********

calificacion = 0.00
disponible=True
archivo_lectura = open("bbdd_cinema.json" , "r") # Abrimos el archivo en modo escritura ('w'). Lo asignamos como objeto a la variable archivo_json
bbdd_cinema = json.load (archivo_lectura) # Leemos el contenido del archivo y lo cargamos en un diccionario bbdd_cinema
archivo_lectura.close() # Cerramos el archivo para asegurarnos de que los datos se escriban correctamente y liberar los recursos asociados al archivo.

print ()
print ("|  ID  |            Título            | Duración | Calificación |  Dispoibilidad !   Género   ") # Encabezados de la tabla
print ("+------+------------------------------+-----------+-------------+-----------------+------------------> ") # Línea divisoria

# Iterar sobre los datos e imprimir cada fila
for i in bbdd_cinema:
    print(f"| {i['id']:4} | {i['Titulo']:28} | {i['Duracion']:8} | {i['Calificacion']:12} | {i['Disponible']:8} | {i['Genero']}")
print ()

main_menu()




