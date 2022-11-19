import math
import streamlit as st
import pandas as pd
import numpy as np

def newton():
    i=1
    #print("_________________________________")
    #n0 = float(input("Iteraciones: "))
    #tol = float(input("Tolerancia: "))
    with st.form(key='calc_biseccion'):
        tol = st.number_input('Tolerancia: ', format="%.4f", step = 1e-4, value = 0.001)
        n0 = st.number_input('Iteraciones', value = 100)
        calcular = st.form_submit_button('Calcular')

    x0 = 1
    f0 = pow(x0, 3) - (6 * pow(x0, 2)) + (11 * x0) - 6.1
    g0 = 3*pow(x0, 2) - 12*x0 + 11

    lista_xn = []
    lista_e = []
    lista_c = []    

    while i < n0:
        xn = x0 - (f0/g0)

        if abs(xn-x0) <= tol:
            st.write("Procedure completed successfully")
            break
        e = (xn-x0)
        i = i+1
        
        #print(str(i) + "  xn: " + str(xn) + "   e: " + str(e))

        lista_xn.append(xn)
        lista_e.append(e)
        lista_c.append(i)

        x0 = xn
        f0 = pow(x0, 3) - (6 * pow(x0, 2)) + (11 * x0) - 6.1
        g0 = 3*pow(x0, 2) - 12*x0 + 11

    d = {'Xn':lista_xn, 'e':lista_e }
    df = pd.DataFrame(data=d, index = lista_c )
    st.table(df)    
    
    e = (xn-x0)
    st.subheader("iteraciones: " + str(i))
    st.subheader("Raiz es igual a: " + str(xn))
    st.subheader("Error: " + str(e))


