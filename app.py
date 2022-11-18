import streamlit as st
import numpy as numpy
import pandas as pd

st.title ("Métodos Numéricos")

col1, col2, col3 = st.columns(3)
with col1:
    st.subheader("Tercer Evaluacion Parcial")
with col2:
    st.subheader("Erick López Saldviar")
with col3:
    st.subheader("348916")
seleccion = st.selectbox("Seleccione una opción: ", ["Método Biseccion", "Método Newton", "Método Secante", "Método Falsa Posicion", "Método Cramer"])

#if seleccion == "Método Biseccion": 