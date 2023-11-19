# Importación de bibliotecas necesarias
import numpy as np  # Importa la biblioteca NumPy para realizar operaciones numéricas eficientes
import streamlit as st  # Importa la biblioteca Streamlit para crear aplicaciones web interactivas
import sympy as sym  # Importa la biblioteca SymPy para realizar manipulación simbólica
import matplotlib.pyplot as plt  # Importa la biblioteca Matplotlib para crear gráficos
import pandas as pd  # Importa la biblioteca Pandas para manipulación de datos tabulares


# Función para calcular las diferencias divididas y generar la tabla
def diferencias_divididas(xi, y):
    n = len(xi)
    tabla = np.zeros(shape=(n, n + 1), dtype=float)  # Inicializa una matriz para la tabla de diferencias divididas

    # Llenar la primera columna de la tabla con los puntos x y
    for i in range(n):
        tabla[i, 0] = xi[i]
        tabla[i, 1] = y[i]

    coeficientes = [tabla[0, 1]]  # Lista para almacenar los coeficientes del polinomio

    x = sym.Symbol('x')
    polinomio = str(tabla[0, 1])  # Inicializar el polinomio con el primer coeficiente

    # Llenar la tabla y calcular coeficientes del polinomio
    for j in range(2, n + 1):
        for i in range(j - 1, n):
            tabla[i, j] = (tabla[i, j - 1] - tabla[i - 1, j - 1]) / (tabla[i, 0] - tabla[i - j + 1, 0])
            if i == j - 1:
                coeficientes.append(tabla[i, j])  # Agregar coeficiente a la lista
                if tabla[i, j] < 0:
                    polinomio += str(tabla[i, j])  # Construir el polinomio en formato de cadena
                else:
                    polinomio += "+" + str(tabla[i, j])
                for i in range(0, i):
                    polinomio += "*(x - " + str(tabla[i, 0]) + ")"

    polinomio_imprimir = polinomio.replace("- -", "+ ")  # Reemplazar "- -" por "+" en el polinomio

    expr = sym.sympify(polinomio)  # Convertir el polinomio de cadena a expresión simbólica
    func = sym.lambdify(x, expr)  # Convertir la expresión simbólica a función
    a = np.min(xi)
    b = np.max(xi)
    xin = np.linspace(a, b)
    yin = func(xin)

    # Crear una tabla con las diferencias divididas
    headers = ["X"] + ["Y"] + [f'{x + 1}A' for x in range(n - 1)]
    st.success("Tabla de Diferencias Divididas")
    df = pd.DataFrame(tabla, columns=headers)
    st.table(df)

    st.success("Coeficientes del Polinomio")
    st.write(coeficientes)

    st.success("Polinomio de Diferencias Divididas de Newton")
    st.write(polinomio_imprimir)

    # Graficar los puntos y el polinomio interpolante
    st.success("Gráfico de Diferencias Divididas de Newton")
    plt.plot(xi, y, 'o', label='Puntos de Entrada')
    plt.plot(xin, yin, label='Polinomio Interpolante')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title("Gráfico de Diferencias Divididas de Newton")
    plt.grid(True)
    st.pyplot()
