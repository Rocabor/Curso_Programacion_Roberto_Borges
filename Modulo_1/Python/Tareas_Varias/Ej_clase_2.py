
'''
# Ejercicio 1: Escribe un programa que solicite al usuario su nombre, edad y país de origen,
                # y luego imprima un mensaje personalizado usando esos datos.

nombre=input("ingrese su nombre:".upper())
edad=input("ingrese su edad:".upper())
pais=input("ingrese su pais de origen:".upper())
print(f"me llamo {nombre}, tengo {edad} y nací en {pais}".upper())  '''

'''
# Ejercicio 2: Escribe un programa que tome dos números del usuario, los sume y muestre el resultado.

numero_a=int(input("ingrese un numero:".upper()))
numero_b=int(input("ingrese otro numero:".upper()))
suma=numero_a+numero_b
print(f"la suma es: {suma}".upper())    '''

'''
# Ejercicio 3: Escribe un programa que tome dos números del usuario y verifique si el primer número es mayor,
                                # menor o igual al segundo número.
num_a,num_b=int(input("ingrese un numero: ".upper())),int(input("ingrese otro numero: ".upper()))
if num_a==num_b:
    print("los numeros son iguales".upper())
elif num_a>num_b:
    print(f"el numero {num_a} es mayor".upper())
else:
    print(f"el numero {num_b} es mayor".upper())    '''

'''
# Ejercicio 4: Escribe un programa que tome tres números del usuario y determine cuál es el mayor
                            # y cuál es el menor de los tres.
var_a= int(input("ingrese valor a: ".upper()))
var_b= int(input("ingrese valor b: ".upper()))
var_c= int(input("ingrese valor c: ".upper()))
mayor=max(var_a,var_b,var_c)
menor=min(var_a,var_b,var_c)
if var_a==var_b==var_c:
    print(f"todos los numeros son iguales".upper())
elif var_a==var_b or var_b==var_c or var_a==var_c:
   print(f"hay dos numeros iguales, y el mayor es: {mayor}".upper())
elif var_a>var_b and var_a>var_c:
    print(f"el numero mayor es: a".upper())
elif var_b>var_a and var_b>var_c:
    print(f"el numero mayor es: b".upper())
else:
    print(f"el numero mayor es: c".upper()) '''

'''
# Ejercicio 5: Escribe un programa que solicite al usuario dos números y verifique:
# Si ambos números son positivos usando el operador and.
num_a=int(input("ingrese un numero positivo o negativo: ".upper()))
num_b=int(input("ingrese un otro numero positivo o negativo: ".upper()))
if num_a>=0 and num_b>=0:
    print("los dos numeros son positivos".upper())
elif num_a <= 0 and num_b <= 0:
    print("los dos numeros son negativos".upper())
# Si el primer número no es negativo usando el operador not.
elif not num_a <= 0:
    print(f"el número positivo es: {num_a}".upper())
# Si al menos uno de los números es positivo usando el operador or.
# elif num_a>=0 or num_b<=0:
#     print(f"el número positivo es: {num_a}".upper())
else:
    print(f"el número positivo es: {num_b}".upper())    '''

'''
# Ejercicio 6: Escribe un programa que solicite al usuario una edad y verifique:
    # Si la persona tiene entre 18 y 65 años usando los operadores and y or.
        # Si la persona no es menor de edad usando el operador not.

edad=int(input("ingrese su edad: ".upper()))
if not edad<18 and edad<=65:
    print("usted está en el rango de los 18 a 65 años".upper())
elif edad<18 or edad>65:
    print("usted no está dentro del rango de edad".upper()) '''

'''
# Ejercicio 7: Escribe un programa que solicite una calificación numérica del usuario y determine el grado según 
# la siguiente escala:
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F
calificacion= int(input("ingrese calificacion: ".upper()))
if calificacion >= 90:
    print(f"grado de calificacion: A".upper())
elif calificacion>=80 and calificacion <=89:
    print(f"grado de calificacion: B".upper())
elif calificacion>=70 and calificacion <=79:
    print(f"grado de calificacion: C".upper())
elif calificacion>=60 and calificacion <=69:
    print(f"grado de calificacion: D".upper())
else:
    print(f"grado de calificacion: F".upper())  '''

'''
# Ejercicio 8: Escribe un programa que solicite un número del usuario y determine si es positivo, negativo o cero.
signo= int(input("ingrese número: ".upper()))
if signo>0:
    print(f"el número es positivo".upper())
elif signo <0:
     print(f"el número es negativo".upper())
else:
      print(f"el número es 0".upper())  '''


ciclo=int(input(f"elabore una lista de nómeros del 1 al 10 utilizando ciclo for o ciclo while"
                "\n\telija opción (1) para ciclo for o (2) para ciclo while: ".upper()))
# Ejercicio 1: ciclo for lista de numero del 1 al 10
if ciclo==1:
    for num_inic in range(10):
        print("ciclo for: ".upper(),num_inic+1)
elif ciclo==2:
# Ejercicio 2: ciclo while lista de numero del 1 al 10
    i=0
    while i<10:
        print("ciclo while: ".upper(), i+1)
        i+=1
else:
    print("no eligió ningula de las opciones".upper())