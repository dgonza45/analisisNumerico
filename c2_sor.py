import numpy as np
import pandas as pd
import streamlit as st


# Función que implementa el método SOR (Successive Over-Relaxation)
def sor_method(a, b, x0, tol, niter, w):
    # Inicialización de variables
    contador = 0  # Contador de iteraciones
    error = tol + 1  # Inicialización del error para garantizar que entre al bucle
    d = np.diag(np.diag(a))  # Matriz diagonal de 'a'
    l = -np.tril(a, -1)  # Parte triangular inferior de 'a' con diagonales excluidas
    u = -np.triu(a, 1)  # Parte triangular superior de 'a' con diagonales excluidas
    tabla = []  # Lista para almacenar los datos de cada iteración

    # Bucle iterativo del método SOR
    while error > tol and contador < niter:
        # Cálculo de la matriz T y el vector c en el método SOR
        t = np.linalg.inv(d - w * l) @ ((1 - w) * d + w * u)
        c = w * np.linalg.inv(d - w * l) @ b

        # Actualización de la solución
        x1 = t @ x0 + c

        # Cálculo del error y actualización de variables
        e = (np.linalg.norm(x1 - x0, ord=np.inf))
        error = e

        # Construcción de la tabla para el registro de iteraciones
        if contador == 0:
            tabla.append([contador] + list(x0) + [0])  # Primer registro con error cero
        else:
            tabla.append([contador] + list(x0) + [e_anterior])  # Registro con error de la iteración anterior

        # Actualización de variables para la próxima iteración
        x0 = x1
        contador += 1
        e_anterior = e

    # Verificación del resultado y generación de salida
    if error < tol:
        s = x0  # Solución aproximada
        eigenvalores = np.linalg.eigvals(t)  # Cálculo de los eigenvalores de 't'
        max_eig = np.max(np.abs(eigenvalores))  # Máximo valor absoluto de los eigenvalores

        # Visualización de la matriz T y sus eigenvalores
        st.write("Matriz T: ")
        st.write(t)
        st.write("")
        st.write(f"Eigenvalues: {max_eig}")
        st.write("")

        # Visualización de la solución aproximada y la tabla de iteraciones
        st.success(f"La aproximación de la solución con tolerancia {tol} es:")
        st.write(s)
    else:
        # En caso de no convergencia, mostrar un mensaje de error
        st.warning(f"Fracasó en {niter} iteraciones. La solución actual es:")
        st.write(s)

    # Agregar la última fila a la tabla de iteraciones y generar un DataFrame
    tabla.append([contador] + list(x0) + [e])
    df = pd.DataFrame(tabla, columns=['Iteración', 'x1', 'x2', 'x3', 'Error'])

    # Visualizar la tabla de iteraciones
    st.dataframe(df, width=1200, height=800)

    # Devolver el error final y la solución aproximada
    return e, s

