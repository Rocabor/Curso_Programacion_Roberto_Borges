

ciclo=int(input(f"elabore una lista de nómeros del 1 al 10 utilizando ciclo for o ciclo while"
                "\n\telija opción (1) para ciclo for o (2) para ciclo while: ".upper()))
# Ejercicio 1: ciclo for lista de numero del 1 al 10
if ciclo==1:
    for num_inic in range(10):
        print("ciclo for: ".upper(),num_inic+1)
elif ciclo==2:
# Ejercicio 2: ciclo while lista de numero del 1 al 10
    iter=1
    while iter<11:
        print("ciclo while: ".upper(), iter)
        iter+=1
else:
    print("no eligió ningula de las opciones".upper())