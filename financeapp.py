# ================
# FINANCEAPP V1
# ================

# Funciones

def calcular_total(lista):
    return sum(lista)


def pedir_cantidad(tipo):
    while True:
        try:
            cantidad = int(input(f"Digite la cantidad de {tipo}: "))

            if cantidad > 0:
                return cantidad
            else:
                print("Ingrese un número mayor que 0.")

        except ValueError:
            print("Solo ingrese números enteros.")


def registrar_ingresos(cantidad):
    ingresos = []

    for i in range(cantidad):
        while True:
            try:
                numero = int(input(f"Digite el valor del ingreso #{i + 1}: "))

                if numero > 0:
                    ingresos.append(numero)
                    break
                else:
                    print("Ingrese un valor mayor que 0.")

            except ValueError:
                print("Solo ingrese números enteros.")

    return ingresos


def registrar_gastos(cantidad):
    gastos = []
    categorias = []

    for i in range(cantidad):
        print(f"\nGasto #{i + 1}")

        while True:
            try:
                valor = int(input("Digite el valor del gasto: "))

                if valor > 0:
                    gastos.append(valor)
                    break
                else:
                    print("Ingrese un valor mayor que 0.")

            except ValueError:
                print("Solo ingrese números enteros.")

        categoria = input(
            "Digite la categoría del gasto "
            "(por ejemplo: comida, transporte, servicios): "
        )

        while categoria.strip() == "":
            print("La categoría no puede quedar vacía.")
            categoria = input("Digite la categoría del gasto: ")

        categorias.append(categoria.strip().lower())

    return gastos, categorias


# Registro de datos

print("===== FINANCEAPP =====")

cantidad_ingresos = pedir_cantidad("ingresos")
ingresos = registrar_ingresos(cantidad_ingresos)

cantidad_gastos = pedir_cantidad("gastos")
gastos, categorias = registrar_gastos(cantidad_gastos)


# Cálculos

total_ingresos = calcular_total(ingresos)
total_gastos = calcular_total(gastos)
disponible = total_ingresos - total_gastos


# Resumen

print("\n===== RESUMEN FINANCIERO =====")
print("Ingresos registrados:", ingresos)
print("Total de ingresos: $", total_ingresos)

print("\nGastos registrados:")
for i in range(len(gastos)):
    print(f"{categorias[i].capitalize()}: ${gastos[i]}")

print("Total de gastos: $", total_gastos)
print("Dinero disponible: $", disponible)