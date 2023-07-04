import pandas as pd
import numpy as np

import streamlit as st

import utils.functions as uf

st.title('HackerRank - Introducción')

st.write('Desafios introductorios de Python en HackerRank.')

# 1. Hello World
st.write('''
    #### **1. Hello World!** 

    Imprime un mensaje con Python.

''')

mensaje = st.text_input('Introduce tu mensaje')
st.write(mensaje)

st.divider()

# 2. If-Else
st.write('''
    #### **2. If-Else** 

    Trabajando con condicionales para determinar números pares e impares

    Dado un entero, *n*, realiza las siguientes acciones condicionales:

    - Si *n* es impar, imprime *"Weird"*
    - Si *n* es par y esta en el rango inclusivo de **2** y **5**, imprime *"Not Weird"*
    - Si *n* es par y esta en el rango inclusivo de **6** y **20**, imprime *"Weird"*
    - Si *n* es par y est mayor que **20**, imprime *"Not Weird"*


''')

numero = st.number_input('Introduce el número', 0)
numero = int(numero)

mensaje = uf.if_else(numero)

st.write(f'**Output**: {mensaje}')

st.divider()

# 3. Operadores aritmeticos
st.write('''
    #### **3. Operadores Aritméticos** 

    El código lee dos enteros *a* y *b*. Se deben imprimir 3 líneas donde:
    
    - La primera línea contiene la suma de los dos números.
    - La segunda línea contiene la resta de los dos números.
    - La tercera línea contiene la multiplicación de los dos números.

''')

col1, col2 = st.columns([0.5, 0.5])

numero_1 = col1.number_input('Introduce el número 1', 0)
numero_2 = col2.number_input('Introduce el número 2', 0)

st.write(f'**Resultado de la suma**: {numero_1 + numero_2}')
st.write(f'**Resultado de la resta**: {numero_1 - numero_2}')
st.write(f'**Resultado de la multiplicación**: {numero_1 * numero_2}')

st.divider()

# 4. División
st.write('''
    #### **4. División** 

    El código lee dos enteros *a* y *b*. Se deben imprimir 2 líneas donde:
    
    - La primera línea contiene la división de a sobre b redondeado.
    - La segunda línea contiene la división de b sobre a sin redondear.
''')

col1, col2 = st.columns([0.5, 0.5])

numero_1 = col1.number_input('Introduce el número *a*', 0)
numero_2 = col2.number_input('Introduce el número *b*', 0)

st.write(f'**Resultado de la división a/b**: {int(numero_1 / numero_2)}')
st.write(f'**Resultado de la división b/a**: {float(numero_2/ numero_1)}')

st.divider()

# 5. Ciclos
st.write('''
    #### **5. Ciclos** 

    El código lee dos enteros *a* y *b*. Se deben imprimir 2 líneas donde:
    
    - La primera línea contiene la división de a sobre b redondeado.
    - La segunda línea contiene la división de b sobre a sin redondear.
''')
