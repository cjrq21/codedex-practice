while True:
    print("¡Hola, mundo!")
    print("Presione 1 para terminar o 2 para repetir '¡Hola, mundo!'")
    opcion = input("Ingrese su opción: ")
    if opcion == '1':
        print("Programa terminado.")
        break
    elif opcion == '2':
        continue
    else:
        print("Opción no válida. Inténtelo de nuevo.")
