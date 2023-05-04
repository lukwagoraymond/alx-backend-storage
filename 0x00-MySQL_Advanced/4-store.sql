-- SQL script that creates a trigger that decreases the quantity of
-- an item in table <items> after adding a new order in table <orders>
delimiter //
CREATE TRIGGER items_quantity_decrease
AFTER INSERT ON orders
FOR EACH ROW
BEGIN
	UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;

END;//
delimiter ;
