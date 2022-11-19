import math
import streamlit as st
import pandas as pd
import numpy as np

def secante():
    i=1
    with st.form(key='calc_secante'):
        x0 = st.number_input('Valor de a: ', value= 3)
        x1 = st.number_input('Valor de b: ', value = 3.5)
        tol = st.number_input('Tolerancia: ', format="%.4f", step = 1e-4, value = 0.001 )
        n0 = st.number_input('Iteraciones: ', value = 100)
        calcular = st.form_submit_button('Calcular')    

    fx0 = pow(x0, 3) - (6 * pow(x0, 2)) + (11*x0) - 6.1
    fx1 = pow(x1, 3) - (6 * pow(x1, 2)) + (11*x1) - 6.1

    lista_xn = []
    lista_e = []
    lista_c = []    

    while i<n0:
        xn= x1 - ((fx1*(x1-x0)) / (fx1 - fx0))
        if abs(xn-x1)/xn < tol:
            print("Procedure completed successfully")
            break
        e = (xn-x1)/xn
        
        lista_xn.append(xn)
        lista_e.append(e)
        lista_c.append(i)        
        
        i=i+1
        x0 = x1
        x1 = xn
        fx0 = fx1
        fx1 = pow(x0, 3) - (6 * pow(xn, 2)) + (11*xn) - 6.1
    
    d = {'Xn':lista_xn, 'e':lista_e }
    df = pd.DataFrame(data=d, index = lista_c )
    st.table(df)    

    e = (xn - x1) / xn
    st.write("iteraciones: " + str(i))
    st.write("Raiz es igual a: " + str(xn))
    st.write("Error: " + str(e))

