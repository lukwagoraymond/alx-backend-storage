-- A SQL Script that ranks bands from different country origins,
-- ordered by the number of (non-unique) fans
-- Final table should have two columns: origin & nb_fans
SELECT `origin`, SUM(`fans`) AS `nb_fans` FROM `metal_bands`
GROUP BY `origin`
ORDER BY `nb_fans` DESC;

