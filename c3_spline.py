import numpy as np  # Importa NumPy para operaciones numéricas eficientes
import streamlit as st  # Importa Streamlit para crear aplicaciones web interactivas
import sympy as sym  # Importa SymPy para manipulación simbólica
import matplotlib.pyplot as plt  # Importa Matplotlib para gráficos


def spline(xi, fi, d):
    n = len(xi)
    x = sym.Symbol('x')

    # Implementación del trazador lineal
    if d == 1:
        tabla_px = []
        for i in range(1, n, 1):
            numerador = fi[i] - fi[i - 1]
            denominador = xi[i] - xi[i - 1]
            m = numerador / denominador
            px = fi[i - 1]
            px = px + m * (x - xi[i - 1])
            tabla_px.append(px)

        st.write("📈 Trazadores Lineales: ")
        for i in range(1, n, 1):
            px = tabla_px[i - 1]
            st.write(px)

        grafico_spline(n, tabla_px, xi, fi, 1)

    # Implementación del trazador cúbico
    elif d == 3:
        # Cálculo de las diferencias entre los puntos adyacentes
        h = np.zeros(n - 1, dtype=float)
        for j in range(0, n - 1, 1):
            h[j] = xi[j + 1] - xi[j]

        # Inicialización de matrices para resolver el sistema de ecuaciones
        A = np.zeros(shape=(n - 2, n - 2), dtype=float)
        B = np.zeros(n - 2, dtype=float)
        S = np.zeros(n, dtype=float)

        # Llenar matrices A y B
        A[0, 0] = 2 * (h[0] + h[1])
        A[0, 1] = h[1]
        B[0] = 6 * ((fi[2] - fi[1]) / h[1] - (fi[1] - fi[0]) / h[0])
        for i in range(1, n - 3, 1):
            A[i, i - 1] = h[i]
            A[i, i] = 2 * (h[i] + h[i + 1])
            A[i, i + 1] = h[i + 1]
            B[i] = 6 * ((fi[i + 2] - fi[i + 1]) / h[i + 1] - (fi[i + 1] - fi[i]) / h[i])
        A[n - 3, n - 4] = h[n - 3]
        A[n - 3, n - 3] = 2 * (h[n - 3] + h[n - 2])
        B[n - 3] = 6 * ((fi[n - 1] - fi[n - 2]) / h[n - 2] - (fi[n - 2] - fi[n - 3]) / h[n - 3])

        # Resolver el sistema de ecuaciones
        r = np.linalg.solve(A, B)

        # Calcular las segundas derivadas
        for j in range(1, n - 1, 1):
            S[j] = r[j - 1]
        S[0] = 0
        S[n - 1] = 0

        # Calcular coeficientes a, b, c, y d para cada tramo
        a = np.zeros(n - 1, dtype=float)
        b = np.zeros(n - 1, dtype=float)
        c = np.zeros(n - 1, dtype=float)
        d = np.zeros(n - 1, dtype=float)
        for j in range(0, n - 1, 1):
            a[j] = (S[j + 1] - S[j]) / (6 * h[j])
            b[j] = S[j] / 2
            c[j] = (fi[j + 1] - fi[j]) / h[j] - (2 * h[j] * S[j] + h[j] * S[j + 1]) / 6
            d[j] = fi[j]

        # Crear el polinomio trazador cúbico
        x = sym.Symbol('x')
        polinomio = []
        for j in range(0, n - 1, 1):
            ptramo = a[j] * (x - xi[j]) ** 3 + b[j] * (x - xi[j]) ** 2 + c[j] * (x - xi[j]) + d[j]
            ptramo = ptramo.expand()
            polinomio.append(ptramo)

        st.write("📈 Trazadores Cúbicos: ")
        for i in range(1, n, 1):
            px = polinomio[i - 1]
            st.write(px)

        grafico_spline(n, polinomio, xi, fi, 3)


def grafico_spline(n, arreglo, xi, fi, grado):
    x = sym.Symbol('x')
    xcoordenadas = np.array([])
    ycoordenadas = np.array([])
    for seccion in range(1, n, 1):
        # A y B para cada sección del trazador (si no se hace, quedan funciones completas e infinitas)
        a = xi[seccion - 1]
        b = xi[seccion]
        xseccion = np.linspace(a, b)  # Puntos equiespaciados entre a y b
        pxseccion = arreglo[seccion - 1]  # La función actual del trazador (en esa sección)
        pxt = sym.lambdify(x, pxseccion)  # Convertir a función
        yseccion = pxt(xseccion)  # Evaluación en Y
        xcoordenadas = np.concatenate((xcoordenadas, xseccion))  # Agregar puntos anteriores a los arreglos de
        # coordenadas
        ycoordenadas = np.concatenate((ycoordenadas, yseccion))

    # Graficar puntos y trazador
    plt.plot(xi, fi, 'ro', label='puntos')
    plt.plot(xcoordenadas, ycoordenadas, label='trazador')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    if grado == 1:
        plt.title("📈 Gráfico de Trazadores Lineales")
    elif grado == 2:
        plt.title("📈 Gráfico de Trazadores Cuadráticos")
    elif grado == 3:
        plt.title("📈 Gráfico de Trazadores Cúbicos")
    plt.grid(True)
    st.pyplot()
