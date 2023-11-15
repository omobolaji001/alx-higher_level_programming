-- lists all records of the table `second_table`:
-- 	Don't list rows without a name
--	Results should display the score and the name
--	Records should be listed by descending score.
SELECT `score`, `name` FROM `second_table` WHERE `name` <> "" ORDER BY `score` DESC;
