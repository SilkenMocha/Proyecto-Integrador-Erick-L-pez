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
  
  cols = st.columns(3)
  currentCol = 0    
  k = 1
  for i in lista_x:
    cols[currentCol].metric('X' + str(k+1) , i)
    currentCol = (currentCol + 1) % len(cols)  


  

