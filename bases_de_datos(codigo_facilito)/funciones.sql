DELIMITER //

CREATE FUNCTION obtener_paginas()
    RETURNS INT
    BEGIN 
        SET @paginas =(SELECT (ROUND(RAND () * 300) * 4));
        RETURNS @paginas;
    END//
    
DELIMITER ;
