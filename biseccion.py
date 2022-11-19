import math
import streamlit as st
import pandas as pd
import numpy as np


def biseccion():
    #print("_________________________________")
    #a = float(input("Valor de a: "))
    #b = float(input("Valor de b: "))
    c = 0
    #tol = float(input("Tolerancia: "))
    i = 1
    #n0 = float(input("Iteraciones: "))
    #print("_________________________________")

    with st.form(key='calc_biseccion'):
        a = st.number_input('Valor de a: ', value= -2)
        b = st.number_input('Valor de b: ', value = 4)
        tol = st.number_input('Tolerancia: ', value = 0.001)
        n0 = st.number_input('Iteraciones: ', value = 100)
        calcular = st.form_submit_button('Calcular')
    

    fa = pow(a, 3) - (6 * pow(a, 2)) + (11*a) - 6.1
    fb = pow(b, 3) - (6 * pow(b, 2)) + (11*b) - 6.1
    pab = fa * fb
    
    lista_xn = []
    lista_e = []
    lista_c = []
    
    if pab < 0:
        while i < n0:

            x = (a + b) / 2
            fx = pow(x, 3) - (6 * pow(x, 2)) + (11 * x) - 6.1
            pax = fa * fx
            
            if pax < 0:
                b = x
            else:
                a = x
                xn = (a + b) / 2
                c = c + 1
                e = abs(xn - x) / xn
                x = xn
                i = i + 1
                #print("x: " + str(xn) + " e: " + str(e) + " c: " + str(c))

            lista_xn.append(xn)
            lista_e.append(e)
            lista_c.append(c)

            st.write("x: " + str(xn) + " e: " + str(e) + " c: " + str(c))

            if e < tol:
                #print("\nProcedure completed successfully\n")
                
                st.write("\nProcedure completed successfully\n")
                break



    else:
        #print("No hay raíz")
        st.write ("No hay raiz")
    
    #print("iteraciones: " + str(c))
    #print("Raiz es igual a: " + str(xn))
    #print("Error: " + str(e))

    st.write("iteraciones: " + str(c))
    st.write("Raiz es igual a: " + str(xn))
    st.write("Error: " + str(e))
    st.write(lista_xn, lista_e, lista_c)

    #cols = st.columns(3)
    #currentCol = 0    
    #for i in lista_xn:
        #cols[currentCol].metric('xn'+, i)
        #currentCol = (currentCol + 1) % len(cols)
    
    col1, col2 = st.columns(2)
    c = 1
    with col1:
        for i in lista_xn:
            c = c+1
            st.metric('xn ' + str(c), i)

    with col2:
        for i in lista_e:
            st.metric('e', i)

    d = {'Xn':lista_xn, 'e':lista_e }
    df = pd.DataFrame(data=d, index = lista_c )
    st.table(df)

            



#biseccion()
#print("_________________________________")
#seguir = input("Continuar? y/n: ")
#while seguir == "y":
    #biseccion()
    #print("_________________________________")
    #seguir = input("Continuar? y/n: ")
