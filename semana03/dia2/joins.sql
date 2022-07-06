-- Active: 1656548435828@@127.0.0.1@3306@cursos
-- INNER JOIN
SELECT nota.id,
alumno.nombre as alumno,
curso.nombre as curso,
nota.nota
from nota
INNER JOIN alumno
on nota.alumno_id = alumno.id
INNER JOIN curso on nota.curso_id = curso.id
ORDER BY alumno.nombre asc;

-- LEFT JOIN
SELECT a.id,a.nombre,avg(n.nota) as alumno
from alumno a
LEFT JOIN nota n on a.id = n.alumno_id
GROUP BY a.id,a.nombre
ORDER BY a.id asc;

-- RIGHT JOIN
select c.nombre as curso,avg(n.nota) as nota
from nota n
RIGHT JOIN curso c on n.curso_id = c.id
GROUP BY c.nombre;

-- Mostrar en una listado la relación de alumnos y sus notas por curso en cada columna
-- ejemplo
-- alumno | python | flask | mysql | promedio
-- peter  | 15     | 14    | 20    | 16.33
select a.nombre as alumno,
(select n.nota from nota n where n.alumno_id = a.id and n.curso_id=1) as HTML,
(select n.nota from nota n where n.alumno_id = a.id and n.curso_id=2) as JAVASCRIPT
from alumno a;

select a.nombre as alumno,
n1.nota as HTML,
n2.nota as JAVASCRIPT,
n3.nota as REACT,
n4.nota as PYTHON,
n5.nota as FLASK,
n6.nota as MYSQL,
avg(n.nota) as promedio
from alumno a
LEFT join nota n on n.alumno_id = a.id
LEFT join nota n1 on n1.alumno_id = a.id and n1.curso_id = 1
LEFT join nota n2 on n2.alumno_id = a.id and n2.curso_id = 2
LEFT join nota n3 on n3.alumno_id = a.id and n3.curso_id = 3
LEFT join nota n4 on n4.alumno_id = a.id and n4.curso_id = 4
LEFT join nota n5 on n5.alumno_id = a.id and n5.curso_id = 5
LEFT join nota n6 on n6.alumno_id = a.id and n6.curso_id = 6
GROUP BY a.nombre,n1.nota,n2.nota,n3.nota,n4.nota,n5.nota,n6.nota;

select * from alumno
where nota >
(select avg(nota) from alumno);