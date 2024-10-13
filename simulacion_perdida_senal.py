# Parámetros iniciales
potencia_inicial_mw = 55  # Potencia inicial de la antena en miliwatts
num_repeticiones = 10  # Número de veces que se repite el proceso
porcentajes = [100, 90, 80, 70, 60, 50, 40, 30, 20, 10]  # Porcentajes para cada repetición

# Lista para almacenar los resultados
resultados = []

# Potencia inicial para la primera repetición
potencia_actual = potencia_inicial_mw

# Iterar a través de cada porcentaje para calcular la potencia respectiva
for i in range(num_repeticiones):
    # Almacenar el resultado actual antes de hacer la regla de tres
    resultados.append((i + 1, potencia_actual, porcentajes[i]))

    # Calcular la potencia para la siguiente iteración usando la regla de tres
    if i < num_repeticiones - 1:  # Evitar el cálculo para la última repetición
        potencia_actual = potencia_actual * (porcentajes[i + 1] / 100)

# Mostrar los resultados de la pérdida de señal
print("Repetición | Potencia (mW) | Porcentaje (%)")
for resultado in resultados:
    print(f"     {resultado[0]}       |    {resultado[1]:.2f} mW   |   {resultado[2]}%")
