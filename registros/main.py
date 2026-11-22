
# FINANCEOS - Sistema financiero personal

# Solicitar ingresos
ingresos = int(input("Ingresos: "))


while ingresos < 0:
    print("Error: los ingresos no pueden ser negativos.")
    ingresos = int(input("Ingresa nuevamente tus ingresos: "))

# Solicitar gastos
gastos = int(input("Gastos: "))


while gastos < 0:
    print("Error: los gastos no pueden ser mayores a los ingresos o negativos.")
    gastos = int(input("Ingresa nuevamente tus gastos: "))

# Operaciones
disponible = ingresos - gastos

print("Disponible:", disponible)

# Condicionales

if disponible > 0:
    print("Balance positivo. Tienes dinero disponible.")

elif disponible < 0:
    print("Balance negativo. Tus gastos superan tus ingresos.")

else:
    print("Balance en cero. Tus ingresos son iguales a tus gastos.")