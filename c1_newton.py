import streamlit as st
from tabulate import tabulate
import matplotlib.pyplot as plt
import numpy as np


def newton(f, df, p_0, tol, n):
    # Muestra información sobre la iteración 0 y el punto inicial
    st.success(f"Iteración: 0, En el punto inicial = {p_0}")

    # Inicializa una lista para almacenar los resultados de cada iteración.
    # La lista tiene la forma [iteración, Xi, f(Xi), error absoluto]
    resultados = [[0, p_0, f(p_0), ""]]

    # Inicializa el contador de iteraciones
    i = 1

    # Inicia un bucle que ejecuta el método de Newton hasta que se cumple el criterio de parada
    while i <= n:
        # Verifica si la derivada en el punto actual es igual a cero (evita división por cero)
        if df(p_0) == 0:
            st.error("Solución no encontrada. La derivada es igual a 0")
            break

        # Calcula el siguiente punto utilizando la fórmula del método de Newton
        p_1 = p_0 - (f(p_0)) / (df(p_0))

        # Calcula el error absoluto entre el punto anterior y el nuevo punto
        e_abs = abs(p_1 - p_0)

        # Almacena los resultados de la iteración actual en la lista de resultados
        resultados.append([i, p_1, f(p_1), e_abs])

        # Verifica si se cumple el criterio de parada (error absoluto menor que la tolerancia)
        if e_abs < tol:
            # Muestra un mensaje indicando la solución encontrada y la cantidad de iteraciones requeridas
            st.success(f"Solución encontrada en x = {p_1} --- En {i} iteraciones")
            break

        # Actualiza el punto anterior para la próxima iteración
        p_0 = p_1

        # Incrementa el contador de iteraciones
        i += 1

    # Si el bucle se ejecuta completamente sin encontrar una solución, muestra un mensaje
    if i > n:
        st.warning(f"Solución no encontrada para la tolerancia: {tol}. Iteraciones Utilizadas: {i - 1}")

    # Muestra una tabla con los resultados utilizando la librería tabulate
    st.write(tabulate(resultados, headers=["Iteraciones", "Xi", "f(xi)", "Error"], tablefmt="github",
                      floatfmt=(".10f", ".10f")))


def grafico_newton_fx(input_function_f, expr_with_numpy_f, limit):
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


def grafico_newton_df(input_function_df, expr_with_numpy_df, limit):
    x = np.linspace(-8, 8, 1000)
    y = eval(expr_with_numpy_df)  # Evaluar la expresión matemática
    fig, ax = plt.subplots(figsize=(8, 6))  # Ajustar el tamaño de la figura aquí
    if limit != 0:
        limn = limit * -1
        ax.set_ylim([limn, limit])
    ax.plot(x, y, color='red', label='Función')
    ax.axhline(0, color='black', linestyle='-', linewidth=1)
    ax.axvline(0, color='black', linestyle='-', linewidth=1)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(f"Gráfico de la Función: {input_function_df}")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)


def grafico_newton_fxdf(expr_with_numpy_f, expr_with_numpy_df, limit):
    x = np.linspace(-8, 8, 1000)
    y1 = eval(expr_with_numpy_f)  # Evaluar la expresión matemática para f(x)
    y2 = eval(expr_with_numpy_df)  # Evaluar la expresión matemática para g(x)
    fig, ax = plt.subplots(figsize=(8, 6))  # Ajustar el tamaño de la figura aquí
    if limit != 0:
        limn = limit * -1
        ax.set_ylim([limn, limit])
    ax.plot(x, y1, color='blue', label='Función f(x)')
    ax.plot(x, y2, color='red', label="Función f'(x)")
    ax.axhline(0, color='black', linestyle='-', linewidth=1)
    ax.axvline(0, color='black', linestyle='-', linewidth=1)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x) , f'(x)")
    ax.set_title(f"Gráfico de f(x) y f'(x)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
