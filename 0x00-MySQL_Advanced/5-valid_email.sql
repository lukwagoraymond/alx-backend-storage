-- SQL Script that creates a trigger that resets the attribute
-- <valid_email> only when the <email> has been changed
delimiter //
CREATE TRIGGER valid_email_reset
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
	IF NEW.email != OLD.email THEN
		SET NEW.valid_email = 0;
	END IF;
END; //
delimiter ;

