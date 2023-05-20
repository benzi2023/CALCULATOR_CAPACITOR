import math

def calcular_banco_capacitores(capacidad_total, capacidad_individual, voltaje):
    num_capacitores = math.ceil(capacidad_total / capacidad_individual)
    capacidad_total_real = num_capacitores * capacidad_individual

    # Cálculo de potencias
    potencia_activa = (capacidad_total_real / 1000000) * (voltaje ** 2)
    potencia_reactiva = (capacidad_total_real / 1000000) * (voltaje ** 2) * math.sin(math.acos(0.9))
    potencia_aparente = math.sqrt((potencia_activa ** 2) + (potencia_reactiva ** 2))

    # Cálculo de carga, tensión y amperaje
    carga = potencia_activa / potencia_aparente
    tension = voltaje
    amperaje = potencia_activa / voltaje

    # Cálculo de velocidad de descarga y carga
    resistencia_descarga = float(input("Ingrese el valor de resistencia de descarga en ohmios: "))
    resistencia_carga = float(input("Ingrese el valor de resistencia de carga en ohmios: "))

    velocidad_descarga = resistencia_descarga * capacidad_total_real / 1000000
    velocidad_carga = resistencia_carga * capacidad_total_real / 1000000

    return num_capacitores, capacidad_total_real, potencia_activa, potencia_reactiva, potencia_aparente, carga, tension, amperaje, velocidad_descarga, velocidad_carga

# Ingreso de valores
capacidad_total = float(input("Ingrese la capacidad total deseada en microfaradios: "))
capacidad_individual = float(input("Ingrese la capacidad individual de cada capacitor en microfaradios: "))
voltaje = float(input("Ingrese el voltaje en voltios: "))

# Cálculo del banco de capacitores
num_capacitores, capacidad_total_real, potencia_activa, potencia_reactiva, potencia_aparente, carga, tension, amperaje, velocidad_descarga, velocidad_carga = calcular_banco_capacitores(capacidad_total, capacidad_individual, voltaje)

# Impresión de resultados
print("Número de capacitores requeridos:", num_capacitores)
print("Capacidad total real del banco:", capacidad_total_real, "microfaradios")
print("Potencia Activa:", potencia_activa, "Watts")
print("Potencia Reactiva:", potencia_reactiva, "VAR")
print("Potencia Aparente:", potencia_aparente, "VA")
print("Carga:", carga)
print("Tensión:", tension, "voltios")
print("Amperaje:", amperaje, "Amperios")
print("Velocidad de Descarga:", velocidad_descarga, "C/s")
print("Velocidad de Carga:", velocidad_carga, "C/s")
