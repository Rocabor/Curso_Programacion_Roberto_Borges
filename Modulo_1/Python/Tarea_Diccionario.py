

# *📘 Ejercicios de Diccionarios (dict)*

# 1. Crear un diccionario de estudiante

diccionario={ "nombre" : "Ana", "edad" : 20, "carrera" : "Ingeniería"}
print(f"diccionario=",diccionario)
print(f"Imprime valor carrera:", diccionario["carrera"],"\n")

# 2. Contar frecuencia de letras
# Dada una palabra
# Crea un diccionario que cuente cuántas veces aparece cada letra
# Resultado esperado: {'b': 1, 'a': 3, 'n': 2}

palabra = "banana"
contar_letra={}
# print(contar_palabras)
for letra in palabra:
    if letra not in contar_letra:
        contar_letra[letra]=1
    else:
        contar_letra[letra]+=1
print(f"Contar frecuencia de letras: {palabra}=",contar_letra,"\n")

# 3. Actualizar valores
# Dado el diccionario
# precios = {"manzana": 0.5, "banana": 0.3}

precios = {"manzana": 0.5, "banana": 0.3}
print(precios)
print("Cambia el precio de la banana a 0.4")
precios["banana"]=0.4
print(precios,"\n")

# 4. Iterar sobre claves y valores
# Dado el diccionario
capitales = {"Francia": "París", "Italia": "Roma", "España": "Madrid"}
# Imprime cada país y su capital en formato: "La capital de [país] es [capital]"
for clave , valor in capitales.items():
    print(f"La capital de: {valor} es {clave}")


# 🧠 Ejercicio combinado: Alumnos y sus materias
# Tienes un diccionario que representa a varios alumnos y las materias que están cursando. Cada materia está representada
# como un conjunto.

alumnos = {"Luis": {"Matemáticas", "Historia", "Biología"}, "Ana": {"Matemáticas", "Física", "Química"},
           "Carlos": {"Historia", "Arte", "Biología"}}

# print(f"\n",alumnos)
# 1. Mostrar todas las materias únicas que cursan los alumnos (sin repetir).
union_luis_ana_carlos = alumnos["Luis"].union(alumnos["Ana"],alumnos["Carlos"])
print("\nLas materias unicas son:", sorted(union_luis_ana_carlos))

# 2. Encontrar las materias comunes entre Luis y Ana.
print("\nLa materia comun entre Luis y Ana es:", set.intersection(alumnos["Luis"] ,alumnos["Ana"]))


# 3. Agregar una nueva materia a Carlos: "Física".
alumnos["Carlos"].add("Fisica")
print(f"\n",alumnos)


# 4. Eliminar la materia "Arte" de Carlos, si existe.
alumnos["Carlos"].discard("Arte")
print(f"\n",alumnos)


# 5. Imprimir el nombre de cada alumno y cuántas materias cursa.
for clave in alumnos.keys():
    print(f"Nombre: {clave}---Materias que cursa:",len(alumnos[clave]))


