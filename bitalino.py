import numpy as np
import matplotlib.pyplot as plt

# Función para leer los datos del archivo y extraer la señal EMG
def load_emg_data(filename):
    with open(filename, 'r') as file:
        # Saltar el encabezado
        lines = file.readlines()
        start_data = False
        emg_data = []

        for line in lines:
            # Comenzamos a leer los datos después del encabezado
            if "EndOfHeader" in line:
                start_data = True
                continue
            if start_data:
                # Leer cada línea de datos y tomar el valor de la columna "A1" (última columna en este caso)
                columns = line.strip().split()
                emg_data.append(int(columns[-1]))  # "A1" es la última columna

    return np.array(emg_data)

# Cargar los datos EMG
filename = r"C:\Users\Pablo\Desktop\EMG_Ali 27.10.2024.txt"
emg_data = load_emg_data(filename)

# Configuración para la gráfica
sampling_rate = 1000  # Según el encabezado, la tasa de muestreo es de 1000 Hz
time = np.linspace(0, len(emg_data) / sampling_rate, len(emg_data))  # Vector de tiempo

# Graficar la señal EMG
plt.figure(figsize=(10, 5))
plt.plot(time, emg_data, label="Señal EMG", color='blue')
plt.title("Lectura de Señal EMG desde Bitalino")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()
plt.show()