-- Active: 1656548435828@@127.0.0.1@3306@db_codigo
-- TRIGGERS
DELIMITER $$

CREATE TRIGGER tg_correo_alumno
BEFORE INSERT
ON tbl_alumno FOR EACH ROW
BEGIN
    set NEW.alumno_email = CONCAT(lower(REPLACE(NEW.alumno_nombre,' ','.')),'@codigo.edu.pe');
END
$$

DELIMITER ;

insert into tbl_alumno(alumno_nombre) values('Gino Carranza');

select * from tbl_alumno;