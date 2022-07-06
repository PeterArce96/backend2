-- Active: 1656548435828@@127.0.0.1@3306@cursos

-- CANTIDAD DE DATOS
SELECT count(*) FROM alumno;
-- PROMEDIO DE NOTAS
SELECT sum(nota) / COUNT(*) from alumno;
-- PROMEDIO DE NOTAS CON COMANDO AVG,además de la MENOR y MAYOR nota
SELECT AVG(nota),MIN(nota),MAX(nota) from alumno;
-- TRAER el PRIMER Y ÚLTIMO país ordenados alfabéticamente
SELECT MIN(pais),MAX(pais) from alumno;
SELECT MAX(id) from alumno;
-- Traer la CANTIDAD de alumnos de PERÚ
SELECT COUNT(*) from alumno WHERE pais = 'Perú';
-- Traer la CANTIDAD de alumnos por PAIS, con el comando GROUP BY, y ORDER BY para traerlos descendentemente.
SELECT pais,COUNT(*) as cantidad from alumno GROUP BY pais
ORDER BY count(*)DESC;

-- Traer nota promedio, nota mínima y máxima por PAIS ordenando por promedio más alto por Pais
SELECT pais, AVG(nota) as promedio,MIN(nota) as menor_nota,MAX(nota) as mayor_nota from alumno
-- Solo va tomar los alumnos con nota Mayor a 10
WHERE nota > 10
GROUP BY pais
-- HAVING --> teniendo tal sentencia, en este caso los PAISES que tienen PROMEDIO menor a 15
HAVING AVG(nota) < 15
ORDER BY promedio DESC;

-- TOMA el promedio de nota de los alumnos aprobados (nota mayores a 10).
SELECT pais,avg(nota) as promedio
FROM alumno
WHERE nota > 10
GROUP BY pais
ORDER BY promedio DESC;


