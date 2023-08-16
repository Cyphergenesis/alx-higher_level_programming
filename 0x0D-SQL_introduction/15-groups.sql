--List the number of records with the same score in the table second_table.
--Records are ordered by descending ccount.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER B Y `number` DESC;
