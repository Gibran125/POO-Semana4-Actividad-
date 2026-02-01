def menu():
    print("--- MENU ---")
    print("1. Saludar")
    print("2. Salir")
    opcion = input("Seleccione una opcion:")
    return opcion

while True:
    choice = menu()
    if choice == "1":
        print("Hola estas usando una CLI en Phyton. ")
    elif choice == "2":
        break
    else:
        print("Opcion invalida.")