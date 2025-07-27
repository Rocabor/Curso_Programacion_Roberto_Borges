
"""PRIMERA ASIGNACION DEL MODULO 1 DE PROGRAMACION (CENTRO EDUCATIVO LOGROS)"""
"AUTOR: ROBERTO BORGES"

print("9. Usa print() para crear un diálogo en consola entre dos personajes. Cada línea debe estar comentada".upper(),end=" ")
print("explicando lo que está pasando.".upper())
# inicia una conversacion entre dos personas que se encuentran
persona_a="roberto"
persona_b="carlos"
# se definen dos variables con los nombres de dos personas en formato string (cadena texto)
print(f"{persona_a}:".upper(), f"hola {persona_b}, como estas?".capitalize())
# se utiliza el comando print() para mostrar en pantalla informacion contenida entre los parentesis
print(f"{persona_b}:".upper(), "estoy bien gracias, y que te parece el clima de hoy en maracaibo?".capitalize())
# la f antes de las comillas indica que es una cadena con formato, permitiendo insertar el valor de la variable dentro de la cadena.
print(f"{persona_a}:".upper(), "está agradable, aunque hay tiempo de lluvia!".capitalize())
# las {} imprime el nombre de una variable de una persona que inicia la conversacion en mayusculas utilizando el metodo upper()
print(f"{persona_b}:".upper(), "cierto! espero no llueva, así podré hacer mis diligencias hoy!".capitalize())
# la informacion entre "" indica que es una cadena de texto que se imprimirá en pantalla
print(f"{persona_a}:".upper(), "bueno, pienso lo mismo, ya que tengo clases de programación!".capitalize())
# la coma (,) se utiliza principalmente para separar elementos y para definir listas de múltiples elementos en una sola línea.
print(f"{persona_b}:".upper(), "ok me parece bien! que tengas un buen dia!".capitalize())
# el metodo capitalize() devuelve una copia de una cadena con el primer carácter convertido a mayúsculas y posteriores a minúsculas.
print(f"{persona_a}:".upper(), "ok gracias! igualmente...".capitalize())
# las ('''''') ("""") y (#) se utilizan para crear comentarios dentro del código