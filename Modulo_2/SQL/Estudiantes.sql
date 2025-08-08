
-- Para crear una tabla en SQL, se utiliza la sentencia CREATE TABLE. 
-- La estructura básica es: CREATE TABLE nombre_tabla (nombre_columna tipo_de_dato, ...);.

CREATE TABLE Estudiantes (
  	id INT PRIMARY KEY,
	Cedula varchar(100),
    Nombre VARCHAR(100),
    Apellido VARCHAR(100)  
);

-- Para insertar valores en una tabla SQL, se utiliza la sentencia INSERT INTO. 
-- La sintaxis básica es: 
-- INSERT INTO nombre_tabla (columna1, columna2, ...) VALUES (valor1, valor2, ...);. 

INSERT INTO Estudiantes (id, cedula, nombre, apellido) VALUES
(1,'16.1863.54', 'roberto', 'borges'),
(2,'29.767.741', 'jinmy', 'chacin'),
(3,'30.604.870', 'maria', 'urdaneta'),
(4,'30.820.000', 'daniel', 'sandoval'),
(5,'31.279.773', 'daviannys', 'villalobos'),
(6,'31.913.070', 'humberto', 'alvarez'),
(7,'32.056.687', 'german', 'suarez'),
(8,'32.636.138', 'juan', 'polania'),
(9,'32.698.769', 'jose', 'velasquez'),
(10,'33.319.114', 'gabriel', 'suarez'),
(11,'33.607.751', 'robert', 'boscan'),
(12,'33.893.333', 'carlos', 'moreno'),
(13,'33.966.984', 'jinm', 'chacin'),
(14,'34.544.638', 'juan', 'arrieta');

--  Actualizar Datos (Update).Para actualizar una tabla en SQL, se utiliza la sentencia UPDATE.
-- UPDATE nombre_tabla
-- SET columna1 = valor1, columna2 = valor2, ...
-- WHERE condición;
UPDATE Estudiantes
SET cedula = '16.186.354'
WHERE id = 1;