
"""PRIMERA ASIGNACION DEL MODULO 1 DE PROGRAMACION (CENTRO EDUCATIVO LOGROS)"""
"AUTOR: ROBERTO BORGES"

print("3. Crea un programa que use una variable booleana (True o False) y aplique los operadores lógicos and, or,".upper(),end= "")
print("y not con otras variables booleanas.".upper())
a=False ; b=False ; c=True; d=False
print(f"a={a}  b={b}  c={c}  d={d}".title())
print(f"terminos a - c y b - d son iguales:".capitalize(),(a==c) and (b==d))         #condicion and se cumple siempre y cuando ambos terminos sean True o False
print(f"terminos a - c o b - d son iguales:".capitalize(),(a==c) or (b==d))          #condicion or se cumple siempre que haya un termino True
print(f"terminos a - b y c - d son diferentes:".capitalize(),not(a==b) and (c!=d))   #condicion not niega el termino
print(f"terminos a - c o b - d son diferentes:".capitalize(),(a!=c) or not(b==d))