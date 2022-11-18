
import math
def regulafalsi():
    print("_________________________________")
    a = float(input("Valor de a: "))
    b = float(input("Valor de b: "))
    c = 0
    tol = float(input("Tolerancia: "))
    i = 1
    n0 = float(input("Iteraciones: "))

    print("_________________________________")

    fa = pow(a, 3) - (3 * pow(a, 2)) - (a) + 2
    fb = pow(b, 3) - (3 * pow(b, 2)) - (b) + 2
    pab = fa * fb

    if pab < 0:
        while i < n0:
            #x1=(XL*fXR - XR*fXL) / (fXR - fXL)
            x = ((a*fb)-(b*fa))/(fb-fa)
            fx = pow(x, 3) - (3 * pow(x, 2)) - (x) + 2


            pax = fa * fx

            if pax < 0:
                b = x
            else:
                a = x

            xn = ((a * fb) - (b * fa)) / (fb - fa)
            i = i + 1
            c = c + 1
            e = abs(xn - x) / xn
            print("x: " + str(xn) + " e: " + str(e) + " c: " + str(c))

            if e < tol:
                print("\nProcedure completed successfully\n")
                break







    else:
        print("No hay raíz")
    print("iteraciones: " + str(c))
    print("Raiz es igual a: " + str(xn))
    print("Error: " + str(e))


regulafalsi()
print("_________________________________")
seguir = input("Continuar? y/n: ")
while seguir == "y":
    regulafalsi()
    print("_________________________________")
    seguir = input("Continuar? y/n: ")
