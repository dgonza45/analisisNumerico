# Importar bibliotecas necesarias
import numpy as np  # Operaciones numéricas eficientes
import streamlit as st  # Crear aplicaciones web interactivas
import sympy as sym  # Manipulación simbólica
import matplotlib.pyplot as plt  # Crear gráficos


# Definir una función para calcular el polinomio de Vandermonde
def vandermonde(x, y):
    # Convertir las listas de entrada en arreglos de numpy
    xi = np.array(x)
    b = np.array(y)
    n = len(x)  # Obtener la cantidad de puntos dados

    # Inicializar una matriz de Vandermonde llena de ceros
    vander = np.zeros(shape=(n, n), dtype=float)

    # Llenar la matriz de Vandermonde con las potencias de xi
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            # Calcular la potencia correspondiente
            potencia = (n - 1) - j
            vander[i, j] = xi[i] ** potencia

    # Resolver el sistema de ecuaciones lineales para obtener los coeficientes del polinomio
    coeficiente = np.linalg.solve(vander, b)

    # Crear un símbolo 'x' para construir el polinomio simbólicamente
    x = sym.Symbol('x')
    polinomio = 0

    # Construir el polinomio sumando términos de cada potencia
    for i in range(0, n, 1):
        # Calcular la potencia correspondiente
        potencia = (n - 1) - i
        # Multiplicar el coeficiente con la variable x elevada a la potencia correspondiente
        multiplicador = coeficiente[i] * (x ** potencia)
        # Acumular términos para formar el polinomio
        polinomio = polinomio + multiplicador

    # Convertir el polinomio simbólico en una función para evaluarlo numéricamente
    px = sym.lambdify(x, polinomio)

    # Generar puntos para graficar el polinomio
    a = np.min(xi)
    b2 = np.max(xi)
    xin = np.linspace(a, b2)
    yin = px(xin)

    # Mostrar la matriz de Vandermonde en la aplicación web de manera atractiva
    st.success("Matriz de Vandermonde:")
    st.table(vander)

    # Mostrar los coeficientes del polinomio de manera atractiva
    st.success("Coeficientes del Polinomio:")
    st.write(coeficiente)

    # Mostrar el polinomio de Vandermonde en la aplicación web de manera atractiva
    st.success("Polinomio de Vandermonde:")
    st.latex(polinomio)

    # Crear un gráfico de dispersión para los puntos dados
    plt.plot(xi, b, 'o', label='Puntos [x,y]')

    # Crear un gráfico de la función polinómica
    plt.plot(xin, yin, label='Polinomio p(x)')

    # Configurar etiquetas y leyenda del gráfico
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.title("Gráfico del Polinomio de Vandermonde")

    # Mostrar la cuadrícula en el gráfico
    plt.grid(True)

    # Mostrar el gráfico en la aplicación web
    st.pyplot()
