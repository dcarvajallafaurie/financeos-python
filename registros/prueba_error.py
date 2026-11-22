# entrada datos

while True:

    try:
        edad = int(input("Ingrese edad: "))

        if edad > 0:
            print("Edad registrada con exito Tu edad es: ", edad)
            break
        else:
            print("Corrija su edad.")


    except ValueError:
        print("Solo digite numeros.")







