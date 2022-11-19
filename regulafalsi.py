import math
import streamlit as st
import pandas as pd
import numpy as np

def regulafalsi():
    c = 0
    i = 1
    with st.form(key='calc_regulafalsi'):
        a = st.number_input('Valor de a: ', value= 3)
        b = st.number_input('Valor de b: ', value = 3.5)
        tol = st.number_input('Tolerancia: ', format="%.4f", step = 1e-4, value = 0.001 )
        n0 = st.number_input('Iteraciones: ', value = 100)
        calcular = st.form_submit_button('Calcular')

    fa = pow(a, 3) - (3 * pow(a, 2)) - (a) + 2
    fb = pow(b, 3) - (3 * pow(b, 2)) - (b) + 2
    pab = fa * fb

    lista_a = []
    lista_b = []
    lista_xn = []
    lista_fx = []
    
    lista_e = []
    lista_c = []

    if pab < 0:
        while i < n0:

            x = ((a*fb)-(b*fa))/(fb-fa)
            fx = pow(x, 3) - (3 * pow(x, 2)) - (x) + 2
            pax = fa * fx

            #lista_a = (a)
            #lista_b = (b)
            #lista_fx = (fx)

            if pax < 0:
                b = x
                fb = fx
            else:
                a = x
                fa = fx

            xn = ((a * fb) - (b * fa)) / (fb - fa)
            e = abs(xn - x) / xn            

            lista_a = (a)
            lista_b = (b)
            lista_fx = (fx)

            lista_xn.append(xn)
            lista_e.append(e)
            lista_c.append(i)
                        
            
            i = i + 1
            c = c + 1

            print("x: " + str(xn) + " e: " + str(e) + " c: " + str(c))

            if e < tol:
                print("\nProcedure completed successfully\n")
                break


    else:
        print("No hay raíz")

    d = {'a':lista_a, 'b':lista_b, 'Xn':lista_xn,'fx':lista_fx, 'e':lista_e }
    df = pd.DataFrame(data=d, index = lista_c )
    st.table(df)

    st.subheader("iteraciones: " + str(c))
    st.subheader("Raiz es igual a: " + str(xn))
    st.subheader("Error: " + str(e))
