import streamlit as st
import numpy as numpy
import pandas as pd
#___________________________________
#import biseccion

st.title ("Métodos Numéricos")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Tercer Evaluacion Parcial")
with col2:
    st.subheader("Erick López - 348916")


seleccion = st.selectbox("Seleccione una opción: ", ["Método Biseccion", "Método Newton", "Método Secante", "Método Falsa Posicion", "Método Cramer"])

#st.latex('''x^3 - 6x^2 + 11x -6.1''')
#if seleccion == "Método Biseccion": 
