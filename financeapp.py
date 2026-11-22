# ================
# FINANCEAPP V1
# ================

# Funciones

import json

def calcular_total(lista):
    return sum(lista)


def cargar_datos():
    try:
        with open("financeos_data.json", "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
            return datos
    except FileNotFoundError:
        return {
            "ingresos": [],
            "gastos": [],
            "categorias": []
        }

def guardar_datos(datos):
    with open("financeos_data.json", "w", encoding="utf-8") as archivo:
        json.dump(datos, archivo, indent=4, ensure_ascii=False)
    

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

print("===== FINANCE OS =====")

datos = cargar_datos()

cantidad_ingresos = pedir_cantidad("ingresos")
ingresos = registrar_ingresos(cantidad_ingresos)
datos["ingresos"].extend(ingresos)

cantidad_gastos = pedir_cantidad("gastos")
gastos, categorias = registrar_gastos(cantidad_gastos)
datos["gastos"].extend(gastos)
datos["categorias"].extend(categorias)

guardar_datos(datos)

# Cálculos

total_ingresos = calcular_total(datos["ingresos"])
total_gastos = calcular_total(datos["gastos"])
disponible = total_ingresos - total_gastos


# Resumen

print("\n===== RESUMEN FINANCIERO =====")
print("Ingresos registrados:", datos["ingresos"])
print("Total de ingresos: $", total_ingresos)

print("\nGastos registrados:")
for i in range(len(datos["gastos"])):
    categoria = datos["categorias"][i].capitalize()
    gasto = datos["gastos"][i]
    print(f"{categoria}: ${gasto}")

print("Total de gastos: $", total_gastos)
print("Dinero disponible: $", disponible)

# Resumen

print("\n===== RESUMEN FINANCIERO =====")
print("Ingresos registrados:", ingresos)
print("Total de ingresos: $", total_ingresos)

print("\nGastos registrados:")
for i in range(len(gastos)):
    print(f"{categorias[i].capitalize()}: ${gastos[i]}")

print("Total de gastos: $", total_gastos)
print("Dinero disponible: $", disponible)