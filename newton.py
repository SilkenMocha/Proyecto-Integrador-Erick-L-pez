import math
def newton():
    i=1
    print("_________________________________")
    n0 = float(input("Iteraciones: "))
    tol = float(input("Tolerancia: "))

    x0 = 1
    f0 = pow(x0, 3)+2*pow(x0, 2)+7*x0
    g0 = 3*pow(x0, 2)+4*x0+7

    while i < n0:
        xn = x0 - (f0/g0)

        if abs(xn-x0) <= tol:
            print("Procedure completed successfully")
            break
        e = (xn-x0)
        print(str(i) + "  xn: " + str(xn) + "   e: " + str(e))
        i = i+1

        x0 = xn
        f0 = pow(x0, 3)+2*pow(x0, 2)+7*x0
        g0 = 3*pow(x0, 2)+4*x0+7

    e = (xn-x0)
    print("iteraciones: " + str(i))
    print("Raiz es igual a: " + str(xn))
    print("Error: " + str(e))

newton()

print("_________________________________")
seguir = input("Continuar? y/n: ")
while seguir == "y":
    newton()
    print("_________________________________")
    seguir = input("Continuar? y/n: ")
