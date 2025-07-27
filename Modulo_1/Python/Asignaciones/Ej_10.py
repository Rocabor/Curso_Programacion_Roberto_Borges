
"""PRIMERA ASIGNACION DEL MODULO 1 DE PROGRAMACION (CENTRO EDUCATIVO LOGROS)"""
"AUTOR: ROBERTO BORGES"

print("10. Realiza un cálculo de la fórmula: (a + b) * c / d con valores fijos en variables.".upper(),end=" ")
print("Imprime el resultado con un mensaje explicativo.".upper())

a=1 ; b=4 ; c=5 ; d=2
resultado= (a+b)*c/d
print(f"variables: a={a} b={b} c={c} y d={d}".title())
print("formula: (a+b)*c/d".title())
print(f"primero se evalua el parentesis (1+4)={a+b}".capitalize())
print(f"segundo se evalua la multiplicación (5)*5={(a+b)*c}".capitalize())
print(f"finalmente se divide y el resultado es (25)/2= {(a+b)*c/d}".capitalize())