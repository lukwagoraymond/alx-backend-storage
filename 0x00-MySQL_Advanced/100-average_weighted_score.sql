-- SQL Script that creates a stored procedure that computes and store
-- the average weighted score for a student
DROP PROCEDURE IF EXISTS ComputeAverageWeightedScoreForUser;
DELIMITER //
CREATE PROCEDURE ComputeAverageWeightedScoreForUser(
    user_id INT
)
BEGIN
    DECLARE weight_avg_score FLOAT;
    SET weight_avg_score = (SELECT SUM(score * weight) / SUM(weight)
                        FROM users AS Us
                        JOIN corrections as Cor ON Us.id=Cor.user_id
                        JOIN projects AS Pr ON Cor.project_id=Pr.id
                        WHERE Us.id=user_id);
    UPDATE users SET average_score = weight_avg_score WHERE id=user_id;
END
//
DELIMITER ;

