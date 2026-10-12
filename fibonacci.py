
def Fibo(n):

    if n == 1:
        return 0

    if n == 2:
        return 1

    res = Fibo(n - 1) + Fibo(n - 2)
    return res

n = int(input("Ingresa el numero de termino: "))

if n < 1:
    print("Ingresa un numero entero mayor o igual a 1")
else:
    print("El termino", n, "de Fibonacci es:", Fibo(n))
