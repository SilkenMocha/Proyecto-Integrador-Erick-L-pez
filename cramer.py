import numpy as np
import streamlit as st
import pandas as pd
import numpy as np

A = np.array([ [1,1], [1,5]])
b = np.array([1,10])


def cramer(A,b):
  n = len(b)
  D = np.linalg.det(A)
  x = np.zeros(n)

  for k in range(n):
    Ak = A.copy()
    Ak[:,k] = b
    Dk = np.linalg.det(Ak)
    x[k] = Dk/D
    print ("x", k+1, "= ", x[k])

