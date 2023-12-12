-- Write a procedure to total an order, with the OrderID passed as an argument

DELIMITER $$ -- temporary delimiter to take place of ;

USE classicmodels$$ -- which database the procedure is for
DROP PROCEDURE IF EXISTS order_total;

-- Input parameters and output parameters
CREATE PROCEDURE order_total (IN orderID INT, OUT total DECIMAL(8,2), OUT tax DECIMAL(8,2))
-- define the procedure body
BEGIN
	-- write as many queries as you need
    SELECT	SUM(quantityOrdered * priceEach) AS "Order Total"
    INTO	total
    FROM	orderdetails
    WHERE	orderNumber = orderID; -- allows the orderID to be specified
								   -- when we call the procedure
	
	SET tax = calculate_tax(total);

END $$
DELIMITER ;