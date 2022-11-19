import streamlit as st
import numpy as numpy
import pandas as pd
#___________________________________
import biseccion as bs
import newton as nw
import secante as sc

st.title ("Métodos Numéricos")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Tercer Evaluacion Parcial")
with col2:
    st.subheader("Erick López - 348916")


seleccion = st.selectbox("Seleccione una opción: ", ["Método Biseccion", "Método Newton", "Método Secante", "Método Falsa Posicion", "Método Cramer"])

if seleccion == "Método Biseccion": 
    st.subheader("Método de Bisección")
    st.latex('''x^3 - 6x^2 + 11x -6.1''')
    bs.biseccion()

if seleccion == "Método Newton": 
    st.subheader("Método de Newton-Raphson")
    st.latex('''x^3 - 6x^2 + 11x -6.1''')
    st.latex('''\dfrac {\mathrm{d}}{\mathrm{d} x}= 3x^2-12x+11''')
    nw.newton()

if seleccion == "Método Secante": 
    st.subheader("Método de Secante")
    st.latex('''x^3 - 6x^2 + 11x -6.1''')
    sc.secante()