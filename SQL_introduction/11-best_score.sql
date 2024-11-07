-- This script selects from the second_table table the columns score name and arranges them in order of order and that meet the requirement that the score is less than or equal to 10 --

SELECT score, name FROM second_table ORDER BY score<=10 DESC;
