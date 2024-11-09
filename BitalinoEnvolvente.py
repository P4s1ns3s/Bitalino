   import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import butter, filtfilt, hilbert

# Función para leer los datos del archivo y extraer la señal EMG
def load_emg_data(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        start_data = False
        emg_data = []

        for line in lines:
            if "EndOfHeader" in line:
                start_data = True
                continue
            if start_data:
                columns = line.strip().split()
                emg_data.append(int(columns[-1]))  # "A1" es la última columna

    return np.array(emg_data)

# Función para aplicar un filtro de paso banda a la señal EMG
def bandpass_filter(data, lowcut, highcut, fs, order=4):
    nyquist = 0.5 * fs
    low = lowcut / nyquist
    high = highcut / nyquist
    b, a = butter(order, [low, high], btype='band')
    filtered_data = filtfilt(b, a, data)
    return filtered_data

# Función para calcular la envolvente de la señal EMG
def calculate_envelope(data):
    # Rectificación (valor absoluto)
    rectified_signal = np.abs(data)
    # Suavizado usando la transformada de Hilbert para obtener la envolvente
    analytic_signal = hilbert(rectified_signal)
    envelope = np.abs(analytic_signal)
    return envelope

# Cargar los datos EMG
filename = r"C:\Users\Pablo\Desktop\EMG_Ali 27.10.2024.txt"
emg_data = load_emg_data(filename)

# Parámetros para el filtrado
sampling_rate = 1000  # Tasa de muestreo en Hz
lowcut = 20  # Frecuencia de corte baja en Hz
highcut = 450  # Frecuencia de corte alta en Hz

# Aplicar el filtro de paso banda
filtered_emg = bandpass_filter(emg_data, lowcut, highcut, sampling_rate)

# Calcular la envolvente de la señal EMG filtrada
envelope = calculate_envelope(filtered_emg)

# Crear el vector de tiempo
time = np.linspace(0, len(emg_data) / sampling_rate, len(emg_data))

# Graficar la señal EMG original, filtrada y su envolvente
plt.figure(figsize=(12, 8))

# Señal original
plt.subplot(3, 1, 1)
plt.plot(time, emg_data, label="Señal EMG sin filtrar", color='blue')
plt.title("Señal EMG Original, Filtrada y Envolvente")
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()

# Señal filtrada
plt.subplot(3, 1, 2)
plt.plot(time, filtered_emg, label="Señal EMG Filtrada", color='green')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()

# Envolvente de la señal filtrada
plt.subplot(3, 1, 3)
plt.plot(time, envelope, label="Envolvente de la Señal EMG", color='red')
plt.xlabel("Tiempo (s)")
plt.ylabel("Amplitud")
plt.legend()
plt.grid()

plt.tight_layout()
plt.show()
