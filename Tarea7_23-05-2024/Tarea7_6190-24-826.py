# Definimos nuestras funciones

#Funciones para realizar las conversiones
#Longitud (1) -------> Primera opcion del menu
def mi_a_km(millas):# Millas a metros
    return millas * 1.60934

def km_a_mi(kilometros): # Metros a millas
    return kilometros / 1.60934

#Volumen (2) -------> Segunda opcion del menu
def m3_a_pie3(m3):# Metros cubicos a pies cubicos
    return m3 * 35.3147

def pie3_a_m3(pie3):# Pies cubicos a metros cubicos
    return pie3 / 35.3147

#Longitud (3) -------> Tercera opcion del menu
def pies_a_metros(pies):# Pies a metros
    return pies * 0.3048

def metros_a_pies(metros):# Metros a pies
    return metros / 0.3048

def yardas_a_metros(yardas):# Yardas a metros
    return yardas * 0.9144

def metros_a_yardas(metros):# Metros a yardas
    return metros / 0.9144

def pies_a_yardas(pies):# Pies a yardas
    return pies / 3

def yardas_a_pies(yardas):# Yardas a pies
    return yardas * 3

# Funcion para mi menu
def menu ():
    print("Selecciona el tipo de conversión que deseas realizar")
    print("1. Conversión de Longitud entre Millas y Kilometros: ")
    print("2. Conversión de Volumen entre m3 y ft3: ")
    print("3. Conversión de Longitud entre pies, metros y yardas: ")
    print("4. Salir")

#Funciones para el submenu
def submenuLongitud(): # Millas y Kilometros
    print("Seleccione la conversión que desea realizar")
    print("a. Millas a Kilometros: ")
    print("b. Kilometros a millas: ")

def submenuVolumen(): #Metros cubicos y pies cubicos 
    print("Seleccione la conversión que desea realizar")
    print("a. m3 a ft3: ")
    print("b. ft3 a m3: ")

def submenuftmyd(): #Pies, metros y yardas
    print("Seleccione la conversión que desea realizar")
    print("a. Pies a metros: ")
    print("b. Metros a pies: ")
    print("c. Yardas a metros: ")
    print("d. Metros a yardas: ")
    print("e. Pies a yardas: ")
    print("f. Yardas a pies")

def main():
    while True:
        menu()
        opcion = input("Ingrese la opción que desea: ")
        #Subemu funcionamiento
        if opcion == '1':
            submenuLongitud()
            subopcion = input("Ingrese una opcion: ")
            if subopcion == 'a':
                millas = float(input("Ingrese millas: "))
                print(f"{millas} millas son {mi_a_km(millas)} kilómetros.")
            elif subopcion == 'b':
                kilometros = float(input("Ingrese  kilómetros: "))
                print(f"{kilometros} kilómetros son {km_a_mi(kilometros)} millas.")
        elif opcion == '2':
            submenuVolumen()
            subopcion = input("Ingrese una opcion: ")
            if subopcion == 'a':
                m3 = float(input("Ingrese m3: "))
                print(f"{m3} m3 son {m3_a_pie3(m3)} pie3.")
            elif subopcion == 'b':
                pie3 = float(input("Ingrese pie3: "))
                print(f"{pie3} pie3 son {pie3_a_m3(pie3)} m3.")
        elif opcion == '3':
            submenuftmyd()
            subopcion = input("Ingrese una opción: ")
            if subopcion == 'a':
                pies = float(input("Ingrese pies: "))
                print(f"{pies} pies son {pies_a_metros(pies)} metros.")
            elif subopcion == 'b':
                metros = float(input("Ingrese metros: "))
                print(f"{metros} metros son {metros_a_pies(metros)} pies.")
            elif subopcion == 'c':
                yardas = float(input("Ingrese yardas: "))
                print(f"{yardas} yardas son {yardas_a_metros(yardas)} metros.")
            elif subopcion == 'd':
                metros = float(input("Ingrese metros: "))
                print(f"{metros} metros son {metros_a_yardas(metros)} yardas.")
            elif subopcion == 'e':
                pies = float(input("Ingrese pies: "))
                print(f"{pies} pies son {pies_a_yardas(pies)} yardas.")
            elif subopcion == 'f':
                yardas = float(input("Ingrese yardas: "))
                print(f"{yardas} yardas son {yardas_a_pies(yardas)} pies.")
        elif opcion == '4':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida, por favor intente de nuevo.")

if __name__ == "__main__":
    main()
