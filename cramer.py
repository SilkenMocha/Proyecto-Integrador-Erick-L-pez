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

    lista_x.append(round(x[k], 5))
    st.subheader("x" + str(k+1) + "= "+ str(x[k]))
    st.metric("X" + str(k+1) , x[k])
  
  cols = st.columns(3)
  currentCol = 0    
  for i in lista_x:
    cols[currentCol].metric('x', i)
    currentCol = (currentCol + 1) % len(cols)  
  
  #st.write(lista_x)

  

