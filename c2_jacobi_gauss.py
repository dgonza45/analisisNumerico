import numpy as np
import pandas as pd
import streamlit as st


def jacobiseidel(a, b, x0, tol, niter, method):
    # Inicialización de variables
    contador = 0  # Contador de iteraciones
    error = tol + 1  # Inicialización del error
    d = np.diag(np.diag(a))  # Extrae la matriz diagonal de A
    l = -np.tril(a, -1)  # Extrae la parte triangular inferior de A (sin diagonal)
    u = -np.triu(a, 1)  # Extrae la parte triangular superior de A (sin diagonal)
    tabla = []  # Lista para almacenar información de cada iteración

    # Bucle principal del método iterativo
    while error > tol and contador < niter:
        if method == 0:
            # Método de Jacobi: Calcula la siguiente iteración utilizando la fórmula de Jacobi
            t = np.linalg.inv(d) @ (l + u)
            c = np.linalg.inv(d) @ b
            x1 = t @ x0 + c
        if method == 1:
            # Método de Gauss-Seidel: Calcula la siguiente iteración utilizando la fórmula de Gauss-Seidel
            t = np.linalg.inv(d - l) @ u
            c = np.linalg.inv(d - l) @ b
            x1 = t @ x0 + c

        # Cálculo del error relativo
        e = (np.linalg.norm(x1 - x0, ord=np.inf)) / (
            np.linalg.norm(x1, ord=np.inf))  # Calcula el error relativo
        error = e

        # Registro de la información para la tabla
        if contador == 0:
            # La primera iteración no tiene error anterior
            tabla.append([contador] + list(x0) + [0])
        else:
            tabla.append([contador] + list(x0) + [e_anterior])  # Guarda información de la iteración actual

        # Actualización de variables para la siguiente iteración
        x0 = x1
        contador += 1
        e_anterior = e

    # Verificación del criterio de convergencia
    if error < tol:
        # Si el error es menor que la tolerancia, se considera que el método ha convergido
        s = x0
        eigenvalores = np.linalg.eigvals(t)
        max_eig = np.max(np.abs(eigenvalores))
        st.success("¡Convergencia Exitosa! 🎉")
        st.write("Matriz t: ")
        st.write(t)
        st.write("")
        st.write(f"Eigenvalues: {max_eig}")
        st.write("")
        st.write(f"La aproximación de la solución del sistema con una tolerancia = {tol} es: ")
        st.write(s)
    else:
        # Si no converge después de Niter iteraciones, se muestra un mensaje de error
        s = x0
        st.error(f"Fracasó en {niter} iteraciones 😟", icon="⚠️")

    # Registro final de la última iteración en la tabla
    tabla.append([contador] + list(x0) + [e])
    df = pd.DataFrame(tabla, columns=['Iteración', 'x1', 'x2', 'x3', 'Error'])
    st.dataframe(df, width=1200, height=800)

    # Devolución del error y la solución aproximada
    return e, s

