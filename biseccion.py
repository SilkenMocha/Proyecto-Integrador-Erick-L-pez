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
                #lista = ['x, e, c']
            lista = []
            lista.append(xn, e, c)
                #list1 = [xn, e, c]
                #list_e = ["e", e]
                #list_c = ["c", c]
                #for el in list1:
                    #cols[currentCol].metric()
                    #currentCol = (currentCol + 1) % len(cols)

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

    st.write(lista)


#biseccion()
#print("_________________________________")
#seguir = input("Continuar? y/n: ")
#while seguir == "y":
    #biseccion()
    #print("_________________________________")
    #seguir = input("Continuar? y/n: ")
