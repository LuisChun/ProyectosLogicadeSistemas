listadenombres = [] # Se inicia la lista,(creamos la lista vacia en la cual se almacenara los nombres)

#Definimos nuestras Funciones
def agregarnombre(nombre_a_agregar): # Esta Funcion nos servira para poder agregar un nombre a nuestra lista
    listadenombres.append(nombre_a_agregar) # añade el nombre a la lista de nombres

def consultarnombre(nombre_a_consultar): # Si deseamos consultar un nombre de lo que ya agregamos.
    return nombre_a_consultar in listadenombres # La lista de nombres nos devuelve True si el nombre esta en la lista y  false si no esta el nombre.

def eliminarnombre(nombre_a_eliminar): # Funcion que nos servira para eliminar el nombre que deseamos de nuestra lista. 
    if nombre_a_eliminar in listadenombres: # Verifica si el nombre esta en la lista
        listadenombres.remove(nombre_a_eliminar) # Elimina el nombre
        return True # Nos devuelve True si el nombre fue eliminado
    return False # Si el nombre no estaba en la lista nos devuelve False

def modificarnombre(nombre_a_modificar, nuevo_nombre): # Si deseamos modificar algun nombre
    if nombre_a_modificar in listadenombres: # Verifica el nombre a modificar en la lista
        posicion = listadenombres.index(nombre_a_modificar) # Obtiene la posicion del nombre que deseamos eliminar de la lista
        listadenombres[posicion] = nuevo_nombre 
        return True# Si fue modificado nos devuelve TRUE
    return False # Si el nombre no estava en la lista nos devuelve FALSE

def mostrar_lista():# Funcion para imprimir la lista de nombre
    print(listadenombres)# Imprime la lista de nombres

def contar_nombre(nombre_a_contar): #Funcion para que nos cuente cuantas veces se repite algun nombre
    return listadenombres.count(nombre_a_contar) # Devuelve el numero de veces que aparece el nombre en la lista, (.count, sirve para realizar conteo)

def mostrar_menu(): # Realizamos un menu para que escoja la opcion a relizar
    print("1. Agregar un nombre")
    print("2. Consultar un nombre")
    print("3. Eliminar un nombre")
    print("4. Modificar un nombre")
    print("5. Mostrar la lista")
    print("6. Contar un nombre")
    print("7. Salir")
    opcion = int(input("Dame una opcion: ")) # Se solicita al usuario que ingrese una opcion del menu y la convierte a un entero.
    return opcion # Devuelve la opcion elegida por el usuario.

def mostrar_submenu_agregar():# Realice un submenu para la opcion 1.
    while True:
        nombre = input("Dame un nombre: ")
        agregarnombre(nombre)
        print("1. Seguir agregando nombres")
        print("2. Salir")
        subopcion = int(input("Brindame una opcion: "))
        if subopcion == 2:
            break

# Programa principal
while True:# Cree un bucle, para romperlo con un break
    op = mostrar_menu()
    if op == 1: # Si el usuario envia un 1 , significa que desea seguir agregando nombres
        mostrar_submenu_agregar()
    elif op == 2: # Si no que regrese al menu principal
        nombreabuscar = input("Dame un nombre a buscar: ")# Solicita al usuario que le brinde el nombre que desea buscar.
        if consultarnombre(nombreabuscar):# Solicita al usuario que le brinde el nombre que desea consultar.
            print("El nombre está en la lista")
        else:
            print("El nombre no está en la lista")
    elif op == 3:# Solicita al usuario que le brinde el nombre que desea borrar
        nombreaborrar = input("Dame un nombre a borrar: ")
        if eliminarnombre(nombreaborrar):
            print("El nombre fue eliminado")
        else:
            print("El nombre no estaba en la lista")
    elif op == 4:
        nombreamodificar = input("Dame un nombre a modificar: ")
        nuevonombre = input("Dame el nuevo nombre: ")
        if modificarnombre(nombreamodificar, nuevonombre):
            print("El nombre fue modificado")
        else:
            print("El nombre no estaba en la lista")
    elif op == 5:
        mostrar_lista()
    elif op == 6:
        nombreacontar = input("Dame un nombre a contar: ")
        cantidad = contar_nombre(nombreacontar)
        print(f"El nombre {nombreacontar} aparece {cantidad} veces en la lista")
    elif op == 7:
        break # Esta funcion sirve para romper el bucle que cree
    else:# De lo contrario si el usuario no ingresa una opcion valida que se brindo del menu, que le aparezca el siguiente mensaje,
        print("Opción no válida")