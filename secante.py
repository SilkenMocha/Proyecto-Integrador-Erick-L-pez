import math
def secante():
    i=1
    print("_________________________________")
    n0 = float(input("Iteraciones: "))
    x0 = float(input("a: "))
    x1 = float(input("b: "))
    tol = float(input("Tolerancia: "))

    fx0 = pow(x0, 3)-(10*x0)-5
    fx1 = pow(x1, 3)-(10*x1)-5

    while i<n0:
        xn= x1 - ((fx1*(x1-x0)) / (fx1 - fx0))
        if abs(xn-x1)/xn < tol:
            print("Procedure completed successfully")
            break
        e = (xn-x1)/xn
        print(str(i) + "  xn: " + str(xn) + "   e: " + str(e))
        i=i+1
        x0 = x1
        x1=xn
        fx0=fx1
        fx1=pow(xn, 3)-(10*xn)-5
    e = (xn - x1) / xn
    print("iteraciones: " + str(i))
    print("Raiz es igual a: " + str(xn))
    print("Error: " + str(e))

secante()

print("_________________________________")
seguir = input("Continuar? y/n: ")
while seguir == "y":
    secante()
    print("_________________________________")
    seguir = input("Continuar? y/n: ")
