
"""PRIMERA ASIGNACION DEL MODULO 1 DE PROGRAMACION (CENTRO EDUCATIVO LOGROS)"""
"AUTOR: ROBERTO BORGES"

print("6. Usa variables numéricas para verificar si un número es mayor que otro usando operadores de comparación ".upper(),end="")
print("(>, <, ==) y muestra el resultado por consola.".upper())
a=1; b=10
print(f"variables: a={a} b={b}".title())
print(f"la condicion a == b: {a==b}".title())
print(f"la condicion a > b: {a>b}".title())
print(f"la condicion b > a: {a<b}".title())
if a==b:
    print(f"los valores son iguales: {a}".title())
else:
    if a > b:
        print(f"el mayor es: {a}".title())
    else:
        if a < b:
            print(f"el mayor es:{b}".title())