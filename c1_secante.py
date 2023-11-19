import streamlit as st  # Importa la biblioteca Streamlit para construir aplicaciones web interactivas.
from tabulate import tabulate  # Importa la función 'tabulate' para formatear resultados en una tabla.
import matplotlib.pyplot as plt
import numpy as np


# Definición de la función que implementa el método de la secante.
def secante(f, p_0, p_1, tol, n):
    p_2 = 0
    # Verifica que p_0 y p_1 no sean iguales, ya que eso causaría una división por cero en el método de la secante.
    if p_0 == p_1:
        st.error("X0 no puede ser igual a X1")
        return None

    e_abs = abs(p_1 - p_0)
    i = 2  # Inicializa la variable de iteración en 2, ya que ya se han utilizado p_0 y p_1.

    # Inicializa una lista que almacenará los resultados de cada iteración.
    resultados = [[0, p_0, f(p_0), ""], [1, p_1, f(p_1), ""]]

    while i <= n:
        # Comprueba si la función en p_1 y p_0 son iguales para evitar la división por cero en el método de la secante.
        if f(p_1) == f(p_0):
            st.warning('Solución no encontrada (error en los valores iniciales)')
            break

        # Fórmula del método de la secante para calcular el próximo punto de aproximación.
        p_2 = p_1 - ((f(p_1) * (p_1 - p_0)) / (f(p_1) - f(p_0)))

        e_abs = abs(p_1 - p_2)  # Calcula la nueva diferencia absoluta entre p_1 y el nuevo punto p_2.

        # Almacena los resultados de la iteración actual en la lista 'resultados'.
        resultados.append([i, p_2, f(p_2), e_abs])

        if e_abs < tol:  # Condición de parada: verifica si la diferencia absoluta es menor que la tolerancia
            # especificada.
            st.success('Solución encontrada con éxito.')
            break

        p_0 = p_1  # Actualiza p_0 con el valor anterior de p_1.
        p_1 = p_2  # Actualiza p_1 con el nuevo valor calculado p_2.

        i += 1  # Incrementa la variable de iteración.

    # Verifica si se alcanzó el límite máximo de iteraciones sin cumplir la condición de parada.
    if i > n:
        st.warning("Solución no encontrada para la tolerancia de:", tol, "--- Iteraciones Usadas:", i - 1)

    # Muestra los resultados en una tabla utilizando la función 'tabulate'.
    st.write(tabulate(resultados, headers=["Iteraciones", "Xi", "f(xi)", "Error"], tablefmt="github",
                      floatfmt=(".10f", ".10f")))

    # Muestra la aproximación de la raíz encontrada si se cumplió la condición de parada antes de alcanzar el
    # límite de iteraciones.
    if i < n:
        st.success(f"Aproximación de la raíz encontrada en x = {p_2}")


def grafico_secante(input_function, expr_with_numpy, limit):
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
