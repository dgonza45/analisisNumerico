import streamlit as st  # Biblioteca para crear aplicaciones web interactivas
from tabulate import tabulate  # Biblioteca para formatear y mostrar tablas
import matplotlib.pyplot as plt
import numpy as np


def fixed_point(f1, g, x0, tol, itermax):
    iterations = 0  # Inicializar el contador de iteraciones
    resultados = [[iterations, x0,  g(x0), f1(x0), "NA"]]  # Inicializar la lista de resultados
    # con la condición inicial

    # Iniciar bucle de iteraciones
    while iterations <= itermax:
        x1 = g(x0)  # Calcular el próximo punto usando la función g
        error = abs(x1 - x0)  # Calcular el error absoluto entre puntos consecutivos
        x0 = x1  # Actualizar el punto actual
        iterations += 1
        resultados.append([iterations, x0, g(x0), f1(x0), error])

        # Añadir los resultados de la iteración actual a la lista

        # Verificar si se alcanzó la tolerancia indicada y salir del bucle si es así
        if error < tol:
            st.success("Solución encontrada con éxito!")
            break

    # Mostrar un mensaje si la solución no se encuentra después de las iteraciones máximas
    if iterations > itermax:
        st.warning("Solución no encontrada. Iteraciones utilizadas: {}".format(iterations))

    # Mostrar los resultados en formato de tabla usando la biblioteca tabulate
    st.write(tabulate(resultados, headers=["Iteraciones", "Xi", "g(xi)", "f(x)", "Error"], tablefmt="github",
                      floatfmt=(".10f", ".10f", ".10f")))


def grafico_punto_fijo_fx(input_function_f, expr_with_numpy_f, limit):
    x = np.linspace(-8, 8, 1000)
    y = eval(expr_with_numpy_f)  # Evaluar la expresión matemática
    fig, ax = plt.subplots(figsize=(8, 6))  # Ajustar el tamaño de la figura aquí
    if limit != 0:
        limn = limit * -1
        ax.set_ylim([limn, limit])
    ax.plot(x, y, color='blue', label='Función')
    ax.axhline(0, color='black', linestyle='-', linewidth=1)
    ax.axvline(0, color='black', linestyle='-', linewidth=1)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(f"Gráfico de la Función: {input_function_f}")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)


def grafico_punto_fijo_gx(input_function_g, expr_with_numpy_g, limit):
    x = np.linspace(-8, 8, 1000)
    y = eval(expr_with_numpy_g)
    fig, ax = plt.subplots(figsize=(8, 6))  # Ajustar el tamaño de la figura aquí
    if limit != 0:
        limn = limit * -1
        ax.set_ylim([limn, limit])
    ax.plot(x, y, color='red', label='Función')
    ax.axhline(0, color='black', linestyle='-', linewidth=1)
    ax.axvline(0, color='black', linestyle='-', linewidth=1)
    ax.set_xlabel("x")
    ax.set_ylabel("g(x)")
    ax.set_title(f"Gráfico de la Función: {input_function_g}")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)


def grafico_punto_fijo_fxgx(expr_with_numpy_f, expr_with_numpy_g, limit):
    x = np.linspace(-8, 8, 1000)
    y1 = eval(expr_with_numpy_f)  # Evaluar la expresión matemática para f(x)
    y2 = eval(expr_with_numpy_g)  # Evaluar la expresión matemática para g(x)
    fig, ax = plt.subplots(figsize=(8, 6))  # Ajustar el tamaño de la figura aquí
    if limit != 0:
        limn = limit * -1
        ax.set_ylim([limn, limit])
    ax.plot(x, y1, color='blue', label='Función f(x)')
    ax.plot(x, y2, color='red', label='Función g(x)')
    ax.axhline(0, color='black', linestyle='-', linewidth=1)
    ax.axvline(0, color='black', linestyle='-', linewidth=1)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x), g(x)")
    ax.set_title(f"Gráfico de f(x) y g(x)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
