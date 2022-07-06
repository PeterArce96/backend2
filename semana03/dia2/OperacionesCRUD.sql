-- Active: 1656548435828@@127.0.0.1@3306@cursos
-- Operaciones CRUD(CREATE,READ,UPDATE,DELETE)

-- READ --> SELECT
SELECT * FROM alumno;
SELECT nombre,pais from alumno;
SELECT distinct pais from alumno;
-- FILTRO CON WHERE
SELECT * FROM alumno WHERE pais = 'Perú';
SELECT * FROM alumno WHERE id = 7;

-- CREATE --> INSERT
INSERT INTO alumno(nombre, email, pais) VALUES('Luis Garcia','luis@gmail.com','Chile');

ALTER TABLE alumno ADD COLUMN nota INT NOT NULL DEFAULT 0;

INSERT INTO alumno(nombre,email,pais,nota) VALUES('Jose Rodriguez','joserod@hotmail.com','Bolivia',15);

INSERT INTO alumno(nombre) values('Carlos Perez'),('Fabiola Rivera'),('Olga Huaman');

-- UPDATE -->UPDATE
UPDATE alumno SET nota = 20;
UPDATE alumno SET nota = 11 WHERE id = 1;
UPDATE alumno 
SET email = CONCAT(lower(REPLACE(nombre,' ','_')),'@codigo.edu.pe')
-- SELECT nombre,email,CONCAT(lower(REPLACE(nombre,' ','_')),'@codigo.edu.pe') 
-- FROM alumno 
WHERE email IS NULL;

-- DELETE --> DELETE
-- Sumamente peligroso, te puede borrar todo sin un WHERE
DELETE FROM alumno where id=5;
-- Si borras un registro de la tabla, queda un espacio en blanco para el ID, si vuelves a insertar, este se suma al último, es decir no en el espacio en blanco.
-- Si quieres ponerlo justo en el espacio donde has eliminado el registro tienes que agregarle el "id" en el VALUES a insertar
-- Lo malo de esto es que no se puede volver a ejecutar ya que el "id" es único
insert into alumno(id,nombre,email) VALUES(5,'Oscar Morales','orcar@gmail.com');
-- El comando TRUNCATE elimina toda la tabla, sin dejar rastro.
TRUNCATE table alumno;
