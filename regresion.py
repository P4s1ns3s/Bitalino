import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Función para simular los datos de 60 pacientes y realizar regresión lineal
def emg_fatigue_regression():
    # Simulación de datos para 60 pacientes
    np.random.seed(0)  # Semilla para reproducibilidad
    num_patients = 60
    # Simulación de la amplitud media de EMG al inicio y al final (por ejemplo)
    # Datos ficticios: amplitud EMG inicial y final (escala de 0 a 100 para simplificación)
    initial_amplitude = np.random.uniform(40, 80, num_patients)  # Amplitud al inicio
    final_amplitude = initial_amplitude + np.random.uniform(5, 20, num_patients)  # Amplitud al final aumenta con fatiga

    # Diferencia en amplitud (para observar el cambio en la fatiga)
    amplitude_difference = final_amplitude - initial_amplitude

    # Crear y ajustar el modelo de regresión lineal
    X = initial_amplitude.reshape(-1, 1)  # Variable independiente (amplitud inicial)
    y = amplitude_difference  # Variable dependiente (cambio en amplitud)

    model = LinearRegression()
    model.fit(X, y)

    # Predicción de la regresión
    y_pred = model.predict(X)

    # Métrica R^2
    r2 = r2_score(y, y_pred)
    print(f"Coeficiente de determinación R^2: {r2:.2f}")
    print(f"Pendiente (coeficiente): {model.coef_[0]:.2f}")
    print(f"Intersección: {model.intercept_:.2f}")

    # Gráfica de los resultados
    plt.figure(figsize=(10, 6))
    plt.scatter(initial_amplitude, amplitude_difference, color="blue", label="Datos de pacientes")
    plt.plot(initial_amplitude, y_pred, color="red", label="Regresión Lineal")
    plt.xlabel("Amplitud EMG Inicial")
    plt.ylabel("Cambio en Amplitud EMG (Fatiga)")
    plt.title("Regresión Lineal de Cambios en EMG para Medir Fatiga Muscular")
    plt.legend()
    plt.grid(True)
    plt.show()

# Llamada a la función para ver la regresión
emg_fatigue_regression()