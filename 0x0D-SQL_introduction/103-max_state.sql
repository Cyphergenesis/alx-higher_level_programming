--Displays the max temperature of each state, ordered by state name.
SELECT `state`, MAX(`value`) AS `mmax_temp`
FROM `temperatures`
GROUP BY `state`
ORDER BY `state`;