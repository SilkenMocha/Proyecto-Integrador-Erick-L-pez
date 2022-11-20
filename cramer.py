import numpy as np
import streamlit as st
import pandas as pd
import numpy as np

def cramer(A,b):
  n = len(b)
  D = np.linalg.det(A)
  x = np.zeros(n)
  A
  b

  for k in range(n):
    Ak = A.copy()
    Ak[:,k] = b
    Dk = np.linalg.det(Ak)
    x[k] = Dk/D
    k=k+1

    st.write ("x", str(k), "= ", x[k])
    
    #st.metric("X"+str(k), x[k])

  #cols = st.columns(3)
  #currentCol = 0    
  #for i in x[k]:
    #cols[currentCol].metric('x', i)
    #currentCol = (currentCol + 1) % len(cols)
  

