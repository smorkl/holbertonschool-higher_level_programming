-- sndndi --

DELIMITER $$
CREATE PROCEDURE mi_procedimiento()
BEGIN
  DECLARE done INT DEFAULT FALSE;
  DECLARE cur CURSOR FOR SELECT DISTINCT score FROM second_table;
  DECLARE CONTINUE HANDLER FOR NOT FOUND SET done = TRUE;

  OPEN cur;

  read_loop: LOOP
    FETCH cur INTO @score;
    IF done THEN
      LEAVE read_loop;
    END IF;

    INSERT INTO mi_tabla (valor) VALUES (@score);
  END LOOP;

  CLOSE cur;
END $$
DELIMITER ;