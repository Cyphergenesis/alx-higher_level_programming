-- List all cities in the databases hbtn_0d_usa.
-- Records are sorted in order of ascending cities.id.
SELECT c.`id`, c.`name`, s.`name`
   FROM `cities` AS c
	INNER JOIN `states` AS s
	ON c.`states_id` = s.`id`
   ORDER BY c.`id`;
