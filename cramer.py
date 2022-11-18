impoort numpy as np

A = np.array([ [1,1,1], [2,3,-2],[3,-2,1]])
b = np.array([4,4,-1])


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

cramer(A,b)
