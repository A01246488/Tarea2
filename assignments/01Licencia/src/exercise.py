def main():
    Edad=int(input("Ingresa tu edad:"))
    if Edad < 18:
        print("No cumples con los requisitos")
    if Edad > 17:
        while True:
            ID = input("¿Tienes identificación oficial? " "(s/n): ")
            if ID == "n":
                print("No cumple con los requisitos")
                break
            elif ID == "s":
                print("Trámite de licencia concedido")
                break
            else:
                print("Respuesta incorrecta")
                break
        
if __name__ == '__main__':
    main()
