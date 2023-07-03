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

# 2. Operadores aritmeticos
st.write('''
    #### **3. Operadores Aritméticos** 

    Trabajando con condicionales para determinar números pares e impares

    Dado un entero, *n*, realiza las siguientes acciones condicionales:

    - Si *n* es impar, imprime *"Weird"*
    - Si *n* es par y esta en el rango inclusivo de **2** y **5**, imprime *"Not Weird"*
    - Si *n* es par y esta en el rango inclusivo de **6** y **20**, imprime *"Weird"*
    - Si *n* es par y est mayor que **20**, imprime *"Not Weird"*
''')

col1, col2 = st.columns([0.5, 0.5])

numero_1 = col1.number_input('Introduce el número 1', 0)
numero_2 = col2.number_input('Introduce el número 2', 0)

st.write(f'**Output de suma**: {numero_1 + numero_2}')
st.write(f'**Output de resta**: {numero_1 - numero_2}')
st.write(f'**Output de multiplicación**: {numero_1 * numero_2}')

st.divider()