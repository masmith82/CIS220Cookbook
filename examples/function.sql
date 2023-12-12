USE classicmodels;
DROP FUNCTION IF EXISTS calculate_tax;
DELIMITER $$
CREATE FUNCTION calculate_tax(order_total DECIMAL(8,2)) RETURNS DECIMAL(8,2)
NO SQL -- this function will not use any SQL
BEGIN
	-- the tax rate is 6%
    RETURN order_total * .06;
END$$
DELIMITER ;