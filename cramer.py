import numpy as np
import streamlit as st
import pandas as pd
import numpy as np

def cramer(A,b):
  n = len(b)
  D = np.linalg.det(A)
  x = np.zeros(n)

  lista_x = []
  for k in range(n):
    Ak = A.copy()
    Ak[:,k] = b
    Dk = np.linalg.det(Ak)
    x[k] = Dk/D

    lista_x.append(x[k])
    st.subheader("x" + str(k+1) + "= "+ str(x[k]))
    st.metric("X" + str(k+1) , x[k])
  
  #st.write(lista_x)

  

