import streamlit as st  # Biblioteca para la creación de aplicaciones web interactivas
from tabulate import tabulate  # Biblioteca para formatear tablas
import pandas as pd  # Biblioteca para manipulación y análisis de datos
import matplotlib.pyplot as plt
import numpy as np


# Definición de la función de bisección para encontrar raíces de ecuaciones
def bisection(f, a, b, tol, n):
    # Lista para almacenar los resultados de cada iteración
    resultados = []

    # Verificación del intervalo inicial
    if a > b:
        st.warning("Advertencia: El extremo izquierdo del intervalo no puede ser mayor que el extremo derecho.")
        # Mensaje de advertencia si el intervalo está mal definido (a > b)
        return None
    if f(a) * f(b) >= 0:
        st.warning("Advertencia: La función no cambia de signo en el intervalo dado.")
        # Mensaje de advertencia si el intervalo no es válido para aplicar la bisección
        return None

    # Inicialización de variables
    e_abs = abs(b - a)  # Diferencia absoluta entre los extremos del intervalo
    i = 1  # Inicialización del contador de iteraciones

    # Bucle principal de la bisección
    while i <= n and e_abs > tol:
        c = (a + b) / 2  # Punto medio del intervalo

        # Verificación si se encontró una solución exacta
        if f(c) == 0:
            st.success("¡Solución encontrada en x=" + str(c) + "!")
            # Mensaje de éxito si se encuentra una solución exacta
            break

        # Actualización de los extremos del intervalo según el cambio de signo
        if f(a) * f(c) < 0:
            b = c
            c_t = a
        else:
            a = c
            c_t = b

        e_abs = abs(c_t - c)  # Actualización del error absoluto

        # Almacenamiento de los resultados de la iteración actual
        if i != 1:
            resultados.append([i, a, c, b, f(c), e_abs])
        else:
            resultados.append([i, a, c, b, f(c), ""])

        # Comprobación de la convergencia
        if e_abs < tol:
            st.success("¡Solución encontrada en x=" + str(c) + ", Iteración:" + str(i) + "!")
            # Mensaje de éxito si se encuentra la solución dentro de la tolerancia especificada
            break
        i += 1

    # Mensaje si no se encuentra solución dentro del número de iteraciones especificado
    if i > n:
        st.error(
            "Error: Solución no encontrada para la tolerancia " + str(tol) + ". Iteraciones utilizadas: " + str(i - 1))

    # Creación de un DataFrame con los resultados (aunque no se está utilizando actualmente)
    pd.DataFrame(resultados, columns=['Iteraciones', 'a', 'xm', "b", "f(xm)", "Error"])

    # Impresión de los resultados formateados en una tabla usando la biblioteca 'tabulate'
    st.write(tabulate(resultados, headers=["Iteraciones", "a", "xm", "b", "f(xm)", "Error"], tablefmt="github",
                      floatfmt=(".0f", ".10f", ".10f", ".10f")))


def grafico_biseccion(input_function, expr_with_numpy, limit):
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
