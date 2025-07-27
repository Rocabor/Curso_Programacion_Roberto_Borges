
"""PRIMERA ASIGNACION DEL MODULO 1 DE PROGRAMACION (CENTRO EDUCATIVO LOGROS)"""
"AUTOR: ROBERTO BORGES"

print("8. Crea un programa que use operadores lógicos para decidir si puedes salir hoy: por ejemplo,".upper(),end=" ")
print("salir si no llueve y tienes tiempo libre.".upper())
llueve=False ; tiempo_libre=True
salida=llueve==False and tiempo_libre==True
print(f"esta lloviendo?: {llueve}\ntengo tiempo libre?: {tiempo_libre}".title())
print(f"entonces podre salir hoy?: {salida}".title())

if llueve==False and tiempo_libre==True:
    print("puedo salir hoy".title())         #se ejecuta si tengo tiempo libre (verdadero) y no llueve (falso)
else:                          # (en el caso and ambas condiciones tienen que ser verdaderas, por eso se niega el falso)
    print("no podre salir hoy".title())      #se ejecuta cuando no se da la condicion inicial