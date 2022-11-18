import streamlit as st
import numpy as numpy
import pandas as pd

st.title ("Métodos Numéricos")

col1, col2 = st.columns(2)
with col1:
    st.subheader("Tercer Evaluacion Parcial")
with col2:
    st.write("Erick López Saldviar — 348916")

seleccion = st.selectbox("Seleccione una opción: ", ["Método Biseccion", "Método Newton", "Método Secante", "Método Falsa Posicion", "Método Cramer"])

#if seleccion == "Método Biseccion": 