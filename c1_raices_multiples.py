import streamlit as st  # Importar Streamlit para crear aplicaciones web con Python
from tabulate import tabulate  # Importar Tabulate para formatear datos en una tabla
import matplotlib.pyplot as plt
import numpy as np


# Definir una función para resolver ecuaciones con raíces múltiples utilizando el método de Newton
def multiple_roots(f, df, df2, x0, tol, n):
    # Inicialización de variables
    xant = x0  # Valor anterior de x
    fant = f(xant)  # Valor de la función en xant
    iteration = 0  # Contador de iteraciones
    resultados = [[iteration, xant, f(xant),
                   ""]]  # Lista para almacenar los resultados de las iteraciones (para posterior tabulación)

    # Proceso iterativo utilizando el método de Newton
    while iteration <= n:
        # Fórmula de iteración del método de Newton
        xact = xant - fant * df(xant) / ((df(xant)) ** 2 - fant * df2(xant))

        # Calcular el valor de la función en el nuevo x (xact)
        fact = f(xact)

        # Calcular el error absoluto
        e_abs = abs(xact - xant)

        # Incrementar el contador de iteraciones
        iteration += 1

        # Actualizar las variables para la próxima iteración
        xant = xact
        fant = fact

        # Agregar los resultados de la iteración actual a la lista
        resultados.append([iteration, xant, f(xant), e_abs])

        # Verificar si el error absoluto está por debajo de la tolerancia especificada
        if e_abs < tol:
            # Mostrar la solución e información de iteración con una alerta de éxito
            st.success(f"¡Solución encontrada en x = {xact}!     Iteraciones: {iteration - 1}    Error = {e_abs}")
            break

    # Verificar si se alcanzó el número máximo de iteraciones sin encontrar una solución
    if iteration > n:
        # Mostrar un mensaje de advertencia con una alerta de advertencia
        st.warning(f"¡Solución no encontrada para la tolerancia = {tol}!")

    # Mostrar los resultados en formato tabular utilizando la biblioteca Tabulate
    st.write(tabulate(resultados, headers=["Iteraciones", "Xi", "f(x)", "Error"], tablefmt="github"))


def grafico_raices_multiples_fx(input_function_f, expr_with_numpy_f, limit):
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


def grafico_raices_multiples_df(input_function_df, expr_with_numpy_df, limit):
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


def grafico_raices_multiples_df2(input_function_df2, expr_with_numpy_df2, limit):
    x = np.linspace(-8, 8, 1000)
    y = eval(expr_with_numpy_df2)  # Evaluar la expresión matemática
    fig, ax = plt.subplots(figsize=(8, 6))  # Ajustar el tamaño de la figura aquí
    if limit != 0:
        limn = limit * -1
        ax.set_ylim([limn, limit])
    ax.plot(x, y, color='yellow', label='Función')
    ax.axhline(0, color='black', linestyle='-', linewidth=1)
    ax.axvline(0, color='black', linestyle='-', linewidth=1)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_title(f"Gráfico de la Función: {input_function_df2}")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)


def grafico_raices_multiples_all(expr_with_numpy_f, expr_with_numpy_df, expr_with_numpy_df2, limit):
    x = np.linspace(-8, 8, 1000)
    y1 = eval(expr_with_numpy_f)  # Evaluar la expresión matemática para f(x)
    y2 = eval(expr_with_numpy_df)  # Evaluar la expresión matemática para g(x)
    y3 = eval(expr_with_numpy_df2)
    fig, ax = plt.subplots(figsize=(8, 6))  # Ajustar el tamaño de la figura aquí
    if limit != 0:
        limn = limit * -1
        ax.set_ylim([limn, limit])
    ax.plot(x, y1, color='blue', label='Función f(x)')
    ax.plot(x, y2, color='red', label="Función f'(x)")
    ax.plot(x, y3, color='yellow', label="Función f''(x)")
    ax.axhline(0, color='black', linestyle='-', linewidth=1)
    ax.axvline(0, color='black', linestyle='-', linewidth=1)
    ax.set_xlabel("x")
    ax.set_ylabel("f(x) , f'(x)")
    ax.set_title(f"Gráfico de f(x) y f'(x)")
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)
