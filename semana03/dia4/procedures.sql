
-- CREAR UN PROCEDURE o procedimiento.
-- Cambiar el limitador de ";" a "$$" para que se ejecute todo el procedure, hasta el END
DELIMITER $$
CREATE PROCEDURE listar_alumnos()
BEGIN
    SELECT * FROM tbl_alumno;
END
$$

DELIMITER ;

-- INVOCAR UN PROCEDIMIENTO ALMACENADO
CALL listar_alumnos();

-- TRABAJO CON BUCLES Y CONDICIONALES
-- IN --> variable de entrada
-- OUT --> variable de salida
DELIMITER $$
CREATE PROCEDURE ejemplo_bucle(IN tope INT,OUT suma INT UNSIGNED)
BEGIN
    DECLARE contador INT;
    SET contador = 1;
    SET suma = 0;

    bucle: LOOP
        IF contador > tope THEN
            LEAVE bucle;
        END IF;

        SET suma = suma + contador;
        SET contador = contador + 1;
    END LOOP;
END
$$

DELIMITER ;

CALL ejemplo_bucle(10,@resultado);
SELECT @resultado;