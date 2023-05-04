-- SQL Script that creates a stored procedure that computes and stores
-- the average weighted score for all students
DELIMITER //
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUsers;
CREATE PROCEDURE ComputeAverageWeightedScoreForUsers()
BEGIN
        UPDATE users AS U SET average_score = (
		SELECT SUM(P.weight * C.score) / SUM(P.weight)
        	FROM projects AS P JOIN corrections AS C ON P.id = C.project_id
        	WHERE C.user_id = U.id
	);
END//
DELIMITER ;

