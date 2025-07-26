
"""
Ejercicio 1: Calculadora de Calificaciones
Descripción: Desarrolla un programa que solicite las calificaciones de varios estudiantes y luego realice los siguientes
 cálculos: la suma de todas las calificaciones, el promedio de las calificaciones, la calificación más alta y la
 calificación más baja. Finalmente, muestra estos resultados.
Instrucciones:
Pregunta al usuario cuántos estudiantes hay en la clase.
Utiliza un bucle for para solicitar las calificaciones de cada estudiante.
Almacena todas las calificaciones en una lista.
Calcula la suma de las calificaciones utilizando la función sum().
Calcula el promedio dividiendo la suma por el número de estudiantes.
Encuentra la calificación más alta con max() y la más baja con min().
Muestra todos los resultados al usuario.    """

"""
num_est=int(input(f"cuantos estudiantes hay en clase?: ".upper()))
lista=[]
suma=0
promedio=0
for tam_clase in range(num_est):
    nota=int(input(f"ingrese calificación: ".upper()))
    lista.append(nota)
    suma =sum(lista)
    promedio=suma/num_est
    max_nota=max(lista)
    min_nota=min(lista)
print(f"\nlista de calificaciones: ".upper(), lista)
# print(f"sumatoria de notas: ".upper(), suma)
print(f"promedio de notas:".upper(), round(promedio,2))     # round( ,2) define el numero de decimales a imprimir
print(f"calificación más alta:".upper(), max(lista))
print(f"calificación más baja:".upper(), min(lista))    """




