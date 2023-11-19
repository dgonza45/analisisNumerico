import streamlit as st
import numpy as np
import re

rows = 0

def reemplazar_funciones_matematicas(expr):
    # Expresión regular para buscar nombres de funciones matemáticas y operadores matemáticos
    pattern = r'\b(sin|cos|tan|sqrt|exp|log|log10)|(\*\*|\^|\+|\-|\*|\/)'

    # Función para reemplazar cada nombre de función y operador matemático
    def replace(match):
        # Si es una función matemática, devuelve su versión con prefijo 'numpy.'
        if match.group(1):
            return f'np.{match.group(1)}'
        # Si es el carácter '^', devuelve el operador '**'
        elif match.group(2) == '^':
            return '**'
        # De lo contrario, devuelve el operador o carácter original
        else:
            return match.group(2)

    # Reemplaza los nombres de funciones y operadores en la expresión por sus equivalentes
    return re.sub(pattern, replace, expr)


# Crear la interfaz de usuario con Streamlit
def create_matrix_entry():
    global rows
    rows = st.number_input("Ingrese el tamaño de la matriz", min_value=1, value=1, step=1)
    columns = rows

    # Crear una matriz vacía
    matrix = np.zeros((rows, columns))

    # Rellenar la matriz con los valores introducidos por el usuario
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = st.number_input(f"Valor en posición ({i}, {j})", key=f"{i}-{j}")

    # Guardar la matriz en una variable
    return matrix


def create_row_entry_x0():
    x0 = np.zeros(rows)
    for i in range(rows):
        x0[i] = st.number_input(f"Valor en posición {i}", key=f"{i}")

    return x0


def create_row_entry_b():
    x0 = np.zeros(rows)
    for i in range(rows):
        x0[i] = st.number_input(f"Valor en posición {i}", key=f'{14 + i}')

    return x0


def create_data_lists_xy():
    num_values = st.number_input("Numero de valores", min_value=1, value=1, step=1)

    x_values = []
    y_values = []

    for i in range(num_values):
        x = st.number_input(f"Valor de X {i + 1}", key=f"x_{i}")
        y = st.number_input(f"Valor de Y {i + 1}", key=f"y_{i}")

        x_values.append(x)
        y_values.append(y)

    return x_values, y_values
