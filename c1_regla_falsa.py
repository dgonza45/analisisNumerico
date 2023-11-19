import streamlit as st  # Importa la biblioteca Streamlit para crear aplicaciones web interactivas
from tabulate import tabulate  # Importa la biblioteca Tabulate para formatear y mostrar tablas
import matplotlib.pyplot as plt
import numpy as np


# Definición de la función para el método de la regla falsa
def false_position(f, a, b, tol, n):
    resultados = []  # Lista para almacenar los resultados de cada iteración

    # Verificación de condiciones iniciales
    if a > b:
        st.warning("Advertencia: El extremo izquierdo del intervalo no puede ser mayor que el extremo derecho.")
        # Mensaje de advertencia si el intervalo está mal definido (a > b)
        return None
    if f(a) * f(b) >= 0:
        st.warning("Advertencia: La función no cambia de signo en el intervalo dado.")
        # Mensaje de advertencia si el intervalo no es válido para aplicar la bisección
        return None

    e_abs = abs(b - a)  # Inicializa la variable de error absoluto
    i = 1  # Inicializa el contador de iteraciones

    # Cálculo de la primera aproximación utilizando el método de la falsa posición
    c = a - (f(a) * (b - a)) / (f(b) - f(a))

    # Bucle de iteraciones
    while i <= n:
        c_1 = c  # Almacena el valor anterior de 'c'

        # Almacena los resultados de la iteración actual en la lista 'resultados'
        resultados.append([i, '%.10f' % a, b, c_1, f(c_1), e_abs])

        # Verifica si se ha encontrado la raíz exacta
        if f(c_1) == 0:
            st.success("¡Solución encontrada en x=" + str(c) + "!")
            # Mensaje de éxito si se encuentra una solución exacta
            break

        # Actualiza los extremos del intervalo basándose en el método de la falsa posición
        if f(a) * f(c) < 0:
            b = c_1
        else:
            a = c_1

        # Calcula la siguiente aproximación utilizando el método de la falsa posición
        c = a - (f(a) * (b - a)) / (f(b) - f(a))

        # Verifica la convergencia comparando el error absoluto con la tolerancia
        if e_abs < tol:
            st.success("¡Solución encontrada en x=" + str(c) + ", Iteración:" + str(i) + "!")
            # Mensaje de éxito si se encuentra la solución dentro de la tolerancia especificada
            break

        # Actualiza el error absoluto para la siguiente iteración
        e_abs = abs(c_1 - c)

        # Actualiza el contador de iteraciones
        i += 1

    # Muestra un mensaje si no se encuentra solución dentro de las iteraciones dadas
    if i > n:
        st.error(
            "Error: Solución no encontrada para la tolerancia " + str(tol) + ". Iteraciones utilizadas: " + str(i - 1))

    # Muestra los resultados en forma de tabla usando la biblioteca Tabulate
    st.write(tabulate(resultados, headers=["Iteraciones", "a", "b", "xm", "f(m)", "Error"], tablefmt="github",
                      floatfmt=(".0f", ".10f", ".10f", ".10f")))


def grafico_regla_falsa(input_function, expr_with_numpy, limit):
    x = np.linspace(-8, 8, 1000)
    y = eval(expr_with_numpy)  # Evaluar la expresión matemática
    fig, ax = plt.subplots(figsize=(8, 6))  # Ajustar el tamaño de la figura aquí
    if limit != 0:
        limn = limit * -1
        ax.set_ylim([limn, limit])
    ax.plot(x, y, color='red', label='Función')
    ax.axhline(0, color='black', linestyle='-', linewidth=1)
    ax.axvline(0, color='black', linestyle='-', linewidth=1)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(f"Gráfico de la Función: {input_function}")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
