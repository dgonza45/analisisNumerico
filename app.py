""" PI-Rates fue diseñada como proyecto final para la materia de Analisis Numerico - Universidad EAFIT 2023-2.

 Diseñado por: Daniel Gonzalez Bernal y Daniela Arango Gutierrez.

 Creditos especiales al profe por rotarnos los codigos de los metodos, a "peanut-eight.vercel.app" y
 a chatGTP por ayudarnos a comentar.
 """

# Todo este archivo contiene solo componentes del Front End (Toma de datos, alertas, botones, etc..).
#  Los metodos numericos estan en los archivos independientes.


# ======================================================================================================================
# ==========================================  FRONT CONFIG - STREAMLIT  ================================================
# ======================================================================================================================

import streamlit as st
import numpy as np  # Aunque algunos IDE digan que no se esta usando, SI SE ESTA USANDO !!!
import auxiliares
import c1_biseccion
import c1_punto_fijo
import c1_regla_falsa
import c1_newton
import c1_raices_multiples
import c1_secante
import c2_jacobi_gauss
import c2_sor
import c3_spline
import c3_vandermonde
import c3_newton


page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
background-color: #000000;
opacity: 1;
background-image:  radial-gradient(#ff00b8 2px, transparent 2px), radial-gradient(#ff00b8 2px, #000000 2px);
background-size: 80px 80px;
background-position: 0 0,40px 40px;
}}

[data-testid="stSidebar"] > div:first-child {{
background-color: #be21b0;
opacity: 1;
background-image:  radial-gradient(#000000 1.5px, transparent 1.5px), radial-gradient(#000000 1.5px, #be21b0 1.5px);
background-size: 60px 60px;
background-position: 0 0,30px 30px;
}}

[data-testid="stHeader"] {{
background: rgba(0,0,0,0);
}}

[data-testid="stToolbar"] {{
right: 2rem;
}}
</style>
"""

st.set_page_config(page_title="🏴‍☠️PI-Rates 🏴‍☠️")
st.markdown(page_bg_img, unsafe_allow_html=True)

# ======================================================================================================================
# ================================================  SIDEBAR CONFIG  ====================================================
# ======================================================================================================================

st.sidebar.header("🔍 METODOS")
st.set_option('deprecation.showPyplotGlobalUse', False)

options_cap1 = ['Bisección', 'Punto Fijo', 'Regla Falsa', 'Newton', 'Raices Multiples', 'Secante']
options_cap2 = ['Jacobi', 'Gauss', 'Sor']
options_cap3 = ['Vandermonde', 'Newton', 'Spline']
BonusPoints = ['Taylor Series', 'Stone']
options_spline = ['Lineal', 'Cubico']

with st.sidebar:
    st.text("Capitulo 1")
    metodo_seleccionado_capitulo1 = st.selectbox('Seleccione el metodo que desea utilizar',
                                                 [""] + options_cap1)
    st.text("Capitulo 2")
    metodo_seleccionado_capitulo2 = st.selectbox('Seleccione el metodo que desea utilizar',
                                                 [""] + options_cap2)
    st.text("Capitulo 3")
    metodo_seleccionado_capitulo3 = st.selectbox('Seleccione el metodo que desea utilizar',
                                                 [""] + options_cap3)
    st.text("BONUS")
    metodo_seleccionado_capitulo4 = st.selectbox('Bonus desbloqueado', [""] + BonusPoints)

if (metodo_seleccionado_capitulo1 == '' and metodo_seleccionado_capitulo2 == '' and metodo_seleccionado_capitulo3 == ''
        and metodo_seleccionado_capitulo4 == ''):
    st.write("<h1 style='text-align: center;'>🏴‍☠️ PI-Rates 🏴‍☠️</h1>", unsafe_allow_html=True)
    st.write(
        "<p style='font-size:18px'>¡Bienvenido a PI-Rates! En esta página podrás explorar los métodos numéricos más "
        "fascinantes de los 7 océanos.</p>", unsafe_allow_html=True)
    st.image("pirate.jpg", caption='', use_column_width=True)

# ======================================================================================================================
#                                                    METODOS CAPITULO 1
# ======================================================================================================================

# ======================================================================================================================
# ====================================================  BISECCION  =====================================================
# ======================================================================================================================

# TESTED =  "log(sin(x)^2 + 1)-(1/2)"  "(f,0,1,10**-7,100)"
if metodo_seleccionado_capitulo1 == 'Bisección':
    st.write("<h1 style='text-align: center;'>💀 BISECCION️ 💀️</h1>", unsafe_allow_html=True)
    input_function = st.text_input('Ingrese la función F')
    function_name = st.latex(input_function)
    interval_a = st.number_input('Ingrese el punto A del intervalo', value=0.0, step=0.1)
    interval_b = st.number_input('Ingrese el punto B del intervalo', value=0.0, step=0.1)
    tolerance = st.text_input('Tolerancia', value=1e-7)
    valor = float(tolerance)
    max_iterations = st.number_input('Ingrese el numero maximo de iteraciones', value=100, min_value=1, step=1)
    limit = st.number_input('Ingrese el rango para el valor maximo del eje Y en las graficas '
                            '(Dejar en 0 para modo automatico)', min_value=0, step=10)
    expr_with_numpy = auxiliares.reemplazar_funciones_matematicas(input_function)
    if expr_with_numpy:
        func = eval(f"lambda x: {expr_with_numpy}")  # Convertir string a función
    col1, col2 = st.columns(2)
    if col1.button('Resolver'):
        c1_biseccion.bisection(func, interval_a, interval_b, valor, max_iterations)
    if col2.button('Graficar'):
        c1_biseccion.grafico_biseccion(input_function, expr_with_numpy, limit)
    st.info('Recuerde que A debe ser menor que B.')
    st.info('Asegúrese que la funcion sea continua en el intervalo.')

# ======================================================================================================================
# ===================================================  PUNTO FIJO  =====================================================
# ======================================================================================================================

# TESTED =  "log(sin(x)^2 + 1)-(1/2)-x"  "log(sin(x)^2 + 1)-(1/2)"  "(f, g, -0.5, 10**-7, 100)"
elif metodo_seleccionado_capitulo1 == 'Punto Fijo':
    st.write("<h1 style='text-align: center;'>💀 PUNTO FIJO 💀️</h1>", unsafe_allow_html=True)
    input_function_f = st.text_input('Ingrese la función F')
    function_name_f = st.latex(input_function_f)
    input_function_g = st.text_input('Ingrese la función G')
    function_name_g = st.latex(input_function_g)
    initial_value = st.number_input('Ingrese el valor inicial X0', step=0.1, format="%.2f")
    tolerance = st.text_input('Tolerancia', value=1e-7)
    valor = float(tolerance)
    max_iterations = st.number_input('Ingrese el numero maximo de iteraciones', value=100, min_value=1, step=1)
    limit = st.number_input('Ingrese el rango para el valor maximo del eje Y en las graficas '
                            '(Dejar en 0 para modo automatico)', min_value=0, step=10)
    expr_with_numpy_f = auxiliares.reemplazar_funciones_matematicas(input_function_f)
    expr_with_numpy_g = auxiliares.reemplazar_funciones_matematicas(input_function_g)
    col1, col2, col3, col4 = st.columns(4)
    if expr_with_numpy_f:
        func_f = eval(f"lambda x: {expr_with_numpy_f}")  # Convertir string a función
    if expr_with_numpy_g:
        func_g = eval(f"lambda x: {expr_with_numpy_g}")  # Convertir string a función
    if col1.button("Resolver"):
        c1_punto_fijo.fixed_point(func_f, func_g, initial_value, valor, max_iterations)
    if col2.button('Graficar F(x)'):
        c1_punto_fijo.grafico_punto_fijo_fx(input_function_f, expr_with_numpy_f, limit)
    if col3.button('Graficar G(x)'):
        c1_punto_fijo.grafico_punto_fijo_gx(input_function_g, expr_with_numpy_g, limit)
    if col4.button('Graficar F(x) & G(x)'):
        c1_punto_fijo.grafico_punto_fijo_fxgx(expr_with_numpy_f, expr_with_numpy_g, limit)
    st.info('Asegurese que F(x) sea continua en el intervalo.')
    st.info('Asegurese que G(x) sea uniforme y continua en el intervalo.')

# ======================================================================================================================
# ==================================================  REGLA FALSA  =====================================================
# ======================================================================================================================

# TESTED =  "log(sin(x)^2 + 1)-(1/2)"  "(f,0,1,10**-7,100)"
elif metodo_seleccionado_capitulo1 == 'Regla Falsa':
    st.write("<h1 style='text-align: center;'>💀 REGLA FALSA 💀️</h1>", unsafe_allow_html=True)
    input_function = st.text_input('Ingrese la función F')
    function_name = st.latex(input_function)
    interval_a = st.number_input('Ingrese el punto A del intervalo', value=0.0, step=0.1)
    interval_b = st.number_input('Ingrese el punto B del intervalo', value=0.0, step=0.1)
    tolerance = st.text_input('Tolerancia', value=1e-7)
    valor = float(tolerance)
    max_iterations = st.number_input('Ingrese el numero maximo de iteraciones', value=100, min_value=1, step=1)
    limit = st.number_input('Ingrese el rango para el valor maximo del eje Y en las graficas '
                            '(Dejar en 0 para modo automatico)', min_value=0, step=10)
    expr_with_numpy = auxiliares.reemplazar_funciones_matematicas(input_function)
    if expr_with_numpy:
        func = eval(f"lambda x: {expr_with_numpy}")  # Convertir string a función
    col1, col2 = st.columns(2)
    if col1.button('Resolver'):
        c1_regla_falsa.false_position(func, interval_a, interval_b, valor, max_iterations)
    if col2.button('Graficar'):
        c1_regla_falsa.grafico_regla_falsa(input_function, expr_with_numpy, limit)

# ======================================================================================================================
# ==================================================  NEWTON  ==========================================================
# ======================================================================================================================

# TESTED =  "log(sin(x)^2 + 1)-(1/2)"  "2*(1/(sin(x)^2 + 1))*(sin(x)*cos(x))"  "(f,df,0.5,10**-7,100)"
elif metodo_seleccionado_capitulo1 == 'Newton':
    st.write("<h1 style='text-align: center;'>💀 NEWTON 💀️</h1>", unsafe_allow_html=True)
    input_function_f = st.text_input('Ingrese la función F')
    function_name_f = st.latex(input_function_f)
    input_function_df = st.text_input('Ingrese la función dF')
    function_name_df = st.latex(input_function_df)
    initial_value = st.number_input('Ingrese el valor inicial X0', step=0.1, format="%.2f")
    tolerance = st.text_input('Tolerancia', value=1e-7)
    valor = float(tolerance)
    max_iterations = st.number_input('Ingrese el numero maximo de iteraciones', value=100, min_value=1, step=1)
    limit = st.number_input('Ingrese el rango para el valor maximo del eje Y en las graficas '
                            '(Dejar en 0 para modo automatico)', min_value=0, step=10)
    expr_with_numpy_f = auxiliares.reemplazar_funciones_matematicas(input_function_f)
    expr_with_numpy_df = auxiliares.reemplazar_funciones_matematicas(input_function_df)
    if expr_with_numpy_f:
        func_f = eval(f"lambda x: {expr_with_numpy_f}")
    if expr_with_numpy_df:
        func_df = eval(f"lambda x: {expr_with_numpy_df}")
    col1, col2, col3, col4 = st.columns(4)
    if col1.button('Resolver'):
        c1_newton.newton(func_f, func_df, initial_value, valor, max_iterations)
    if col2.button('Graficar F(x)'):
        c1_newton.grafico_newton_fx(input_function_f, expr_with_numpy_f, limit)
    if col3.button("Graficar F'(x)"):
        c1_newton.grafico_newton_df(input_function_df, expr_with_numpy_df, limit)
    if col4.button("Graficar F(x) & F'(x)"):
        c1_newton.grafico_newton_fxdf(expr_with_numpy_f, expr_with_numpy_df, limit)
    st.info('Asegurese de que F(x) sea continua y que su derivada no sea igual a cero en ninguno de '
            'los puntos del intervalo analizado.')

# ======================================================================================================================
# ===============================================  RAICES MULTIPLES  ===================================================
# ======================================================================================================================

# TESTED =  "exp(x)-x-1"  "exp(x)-1"  "exp(x)"  "(f,df,d2f,1,10**-7,100)"
elif metodo_seleccionado_capitulo1 == 'Raices Multiples':
    st.write("<h1 style='text-align: center;'>💀 RAICES MULTIPLES 💀️</h1>", unsafe_allow_html=True)
    input_function_f = st.text_input('Ingrese la función F')
    function_name_f = st.latex(input_function_f)
    input_function_df = st.text_input('Ingrese la función dF')
    function_name_df = st.latex(input_function_df)
    input_function_df2 = st.text_input('Ingrese la función dF2')
    function_name_df2 = st.latex(input_function_df2)
    initial_value = st.number_input('Ingrese el valor inicial X0', step=0.1)
    tolerance = st.text_input('Tolerancia', value=1e-7)
    valor = float(tolerance)
    max_iterations = st.number_input('Ingrese el numero maximo de iteraciones', value=100, min_value=1, step=1)
    limit = st.number_input('Ingrese el rango para el valor maximo del eje Y en las graficas '
                            '(Dejar en 0 para modo automatico)', min_value=0, step=10)
    expr_with_numpy_f = auxiliares.reemplazar_funciones_matematicas(input_function_f)
    expr_with_numpy_df = auxiliares.reemplazar_funciones_matematicas(input_function_df)
    expr_with_numpy_df2 = auxiliares.reemplazar_funciones_matematicas(input_function_df2)
    if expr_with_numpy_f:
        func_f = eval(f"lambda x: {expr_with_numpy_f}")
    if expr_with_numpy_df:
        func_df = eval(f"lambda x: {expr_with_numpy_df}")
    if expr_with_numpy_df2:
        func_df2 = eval(f"lambda x: {expr_with_numpy_df2}")
    col1, col2, col3, col4, col5 = st.columns(5)
    if col1.button('Resolver'):
        c1_raices_multiples.multiple_roots(func_f, func_df, func_df2, initial_value, valor, max_iterations)
    if col2.button('Graficar F(x)'):
        c1_raices_multiples.grafico_raices_multiples_fx(input_function_f, expr_with_numpy_f, limit)
    if col3.button("Graficar F'(x)"):
        c1_raices_multiples.grafico_raices_multiples_df(input_function_df, expr_with_numpy_df, limit)
    if col4.button("Graficar F''(x)"):
        c1_raices_multiples.grafico_raices_multiples_df2(input_function_df2, expr_with_numpy_df2, limit)
    if col5.button("Graficar F(x), F'(x) & F''(x)"):
        (c1_raices_multiples.grafico_raices_multiples_all
         (expr_with_numpy_f, expr_with_numpy_df, expr_with_numpy_df2, limit))
    st.info('Asegurese de que F(x) sea continua.')
    st.info('Confirme que las derivadas ingresadas sean las correctas.')

# ======================================================================================================================
# ==================================================  SECANTE  =========================================================
# ======================================================================================================================

# TESTED =  "log(sin(x)^2 + 1)-(1/2)"  "(f,0.5,1,10**-7,100)"
elif metodo_seleccionado_capitulo1 == 'Secante':
    st.write("<h1 style='text-align: center;'>💀 SECANTE 💀️</h1>", unsafe_allow_html=True)
    input_function = st.text_input('Ingrese la función F')
    function_name = st.latex(input_function)
    interval_a = st.number_input('Ingrese el valor inicial X0', step=0.1)
    interval_b = st.number_input('Ingrese el valor inicial X1', step=0.1)
    tolerance = st.text_input('Tolerancia', value=1e-7)
    valor = float(tolerance)
    max_iterations = st.number_input('Ingrese el numero maximo de iteraciones', value=100, min_value=1, step=1)
    limit = st.number_input('Ingrese el rango para el valor maximo del eje Y en las graficas '
                            '(Dejar en 0 para modo automatico)', min_value=0, step=10)
    expr_with_numpy = auxiliares.reemplazar_funciones_matematicas(input_function)
    if expr_with_numpy:
        func = eval(f"lambda x: {expr_with_numpy}")  # Convertir string a función
    col1, col2 = st.columns(2)
    if col1.button('Resolver'):
        c1_secante.secante(func, interval_a, interval_b, valor, max_iterations)
    if col2.button('Graficar'):
        c1_secante.grafico_secante(input_function, expr_with_numpy, limit)
    st.info('Asegurese de que F(x) sea continua.')

# ======================================================================================================================
#                                                    METODOS CAPITULO 2
# ======================================================================================================================

# ======================================================================================================================
# ==================================================  JACOBI  ==========================================================
# ======================================================================================================================

# TESTED =  "A = [[11, 5, 4], [5, 25, 4], [5, 4, 10]]"  "B = [10, 10, 10]"  "X0 = [1, 1, 1]"
#  "Tol = 1e-7"  "Niter = 100"
if metodo_seleccionado_capitulo2 == 'Jacobi':
    st.write("<h1 style='text-align: center;'>💀 JACOBI 💀️</h1>", unsafe_allow_html=True)
    st.subheader('Matriz A')
    A_matrix_entry = auxiliares.create_matrix_entry()
    st.write("Matriz A creada:")
    st.write(A_matrix_entry)
    st.subheader('Matriz B')
    row_b = auxiliares.create_row_entry_b()
    st.write('Matriz B creada:')
    st.write(row_b)
    st.subheader('Matriz X0')
    row_x0 = auxiliares.create_row_entry_x0()
    st.write('Matriz X0 creada:')
    st.write(row_x0)
    Niter = st.number_input('Ingrese el numero maximo de iteraciones', min_value=1, value=100, step=1)
    tolerance = st.text_input('Tolerancia', value=1e-7)
    tol = float(tolerance)
    if st.button("Resolver"):
        c2_jacobi_gauss.jacobiseidel(A_matrix_entry, row_b, row_x0, tol, Niter, 0)
    st.info('Recuerde que para garantizar la convergencia, la matriz debe ser diagonalmente dominante. '
            'Esto significa que el valor absoluto del elemento diagonal de cada fila debe ser mayor que la suma '
            'de los valores absolutos de los demás elementos de esa fila.')


# ======================================================================================================================
# ==================================================  GAUSS  =========================================================
# ======================================================================================================================

# TESTED =  "A = [[11, 5, 4], [5, 25, 4], [5, 4, 10]]"  "B = [10, 10, 10]"  "X0 = [1, 1, 1]"
#  "Tol = 1e-7"  "Niter = 100"
elif metodo_seleccionado_capitulo2 == 'Gauss':
    st.write("<h1 style='text-align: center;'>💀 GAUSS 💀️</h1>", unsafe_allow_html=True)
    st.subheader('Matriz A')
    A_matrix_entry = auxiliares.create_matrix_entry()
    st.write("Matriz A creada:")
    st.write(A_matrix_entry)
    st.subheader('Matriz B')
    row_b = auxiliares.create_row_entry_b()
    st.write('Matriz B creada:')
    st.write(row_b)
    st.subheader('Matriz X0')
    row_x0 = auxiliares.create_row_entry_x0()
    st.write('Matriz X0 creada:')
    st.write(row_x0)
    Niter = st.number_input('Ingrese el numero maximo de iteraciones', min_value=1, value=100, step=1)
    tolerance = st.text_input('Tolerancia', value=1e-7)
    tol = float(tolerance)
    if st.button("Resolver"):
        c2_jacobi_gauss.jacobiseidel(A_matrix_entry, row_b, row_x0, tol, Niter, 1)
    st.info('Recuerde que para garantizar la convergencia, la matriz debe ser diagonalmente dominante. '
            'Esto significa que el valor absoluto del elemento diagonal de cada fila debe ser mayor que la suma '
            'de los valores absolutos de los demás elementos de esa fila.')

# ======================================================================================================================
# ====================================================  SOR  ===========================================================
# ======================================================================================================================

# TESTED =  "A = [[11, 5, 4], [5, 25, 4], [5, 4, 10]]"  "B = [10, 10, 10]"  "X0 = [1, 1, 1]"
#  "Tol = 1e-7"  "Niter = 100"  "w = 0.4"
elif metodo_seleccionado_capitulo2 == 'Sor':
    st.write("<h1 style='text-align: center;'>💀 SOR 💀️</h1>", unsafe_allow_html=True)
    st.subheader('Matriz A')
    A_matrix_entry = auxiliares.create_matrix_entry()
    st.write("Matriz A creada:")
    st.write(A_matrix_entry)
    st.subheader('Matriz B')
    row_b = auxiliares.create_row_entry_b()
    st.write('Matriz B creada:')
    st.write(row_b)
    st.subheader('Matriz X0')
    row_x0 = auxiliares.create_row_entry_x0()
    st.write('Matriz X0 creada:')
    st.write(row_x0)
    Niter = st.number_input('Ingrese el numero maximo de iteraciones', min_value=1, value=100, step=1)
    tolerance = st.text_input('Tolerancia', value=1e-7)
    W = st.number_input('Parámetro de relajación W', min_value=0.0, max_value=2.0, value=0.4, step=0.1)
    valor = float(tolerance)
    if st.button("Resolver"):
        c2_sor.sor_method(A_matrix_entry, row_b, row_x0, valor, Niter, W)
    st.info('Recuerde que el parámetro W, conocido como el factor de relajación, es crucial en el método SOR.'
            'Debe estar en el rango (0, 2) para garantizar la convergencia del método. '
            'Valores cercanos a 1 suelen ser buenos para la convergencia.')

# ======================================================================================================================
#                                               METODOS CAPITULO 3
# ======================================================================================================================

# ======================================================================================================================
# ================================================  VANDERMONDE  =======================================================
# ======================================================================================================================

# TESTED =  "x = [-1, 0, 3, 4]"  "y = [15.5, 3, 8, 1]"
if metodo_seleccionado_capitulo3 == 'Vandermonde':
    st.write("<h1 style='text-align: center;'>💀 VANDERMONDE 💀️</h1>", unsafe_allow_html=True)
    x_list, y_list = auxiliares.create_data_lists_xy()
    st.write("Valores de X:")
    x = x_list
    st.text(x)
    st.write("Valores de Y:")
    y = y_list
    st.text(y)
    if st.button("Resolver"):
        c3_vandermonde.vandermonde(x, y)

# ======================================================================================================================
# =====================================================  NEWTON  =======================================================
# ======================================================================================================================

# TESTED =  "x = [-1, 0, 3, 4]"  "y = [15.5, 3, 8, 1]"
elif metodo_seleccionado_capitulo3 == 'Newton':
    st.write("<h1 style='text-align: center;'>💀 NEWTON 💀️</h1>", unsafe_allow_html=True)
    x_list, y_list = auxiliares.create_data_lists_xy()
    st.write("Valores de X:")
    x = x_list
    st.text(x)
    st.write("Valores de Y:")
    y = y_list
    st.text(y)
    if st.button("Resolver"):
        c3_newton.diferencias_divididas(x, y)

# ======================================================================================================================
# =====================================================  SPLINE  =======================================================
# ======================================================================================================================

# TESTED =  "x = [0, 2, 4]"  "y = [3, 5, 1]"
elif metodo_seleccionado_capitulo3 == 'Spline':
    spline = st.selectbox('¿Seleccione el Spline a utilizar?', [""] + options_spline)
    if spline == 'Lineal':
        x_list, y_list = auxiliares.create_data_lists_xy()
        st.write("Valores de X:")
        x = x_list
        st.text(x)
        st.write("Valores de Y:")
        y = y_list
        st.text(y)
        if st.button("Resolver"):
            c3_spline.spline(x, y, 1)
# TESTED =  "x = [-2.0, -1.0, 1.0, 3.0]   "y = [3.0, 1.0, 2.0, -1.0]"
    elif spline == 'Cubico':
        x_list, y_list = auxiliares.create_data_lists_xy()
        st.write("Valores de X:")
        x = x_list
        st.text(x)
        st.write("Valores de Y:")
        y = y_list
        st.text(y)
        if st.button("Resolver"):
            c3_spline.spline(x, y, 3)

# ======================================================================================================================
#                                                    METODOS CAPITULO 4
# ======================================================================================================================

# ======================================================================================================================
# =====================================================  MEMES  ========================================================
# ======================================================================================================================
if metodo_seleccionado_capitulo4 == 'Taylor Series':
    st.write('Grafica de Taylor realizada con Series de Taylor')
    st.image("Taylor.jpg", caption='', use_column_width=False)
elif metodo_seleccionado_capitulo4 == 'Stone':
    st.image("Stone.jpg", caption='', use_column_width=False)
