use cookbook;

DROP PROCEDURE IF EXISTS show_user_ingredients;
DROP PROCEDURE IF EXISTS add_ingredient_to_stock;
DROP PROCEDURE IF EXISTS create_ingredient;
DROP PROCEDURE IF EXISTS insert_ingredient;
DROP PROCEDURE IF EXISTS get_ingredient_name;
DROP PROCEDURE IF EXISTS get_cost_name;
DROP PROCEDURE IF EXISTS get_vegan_ingredients;
DROP PROCEDURE IF EXISTS get_carb_ingredients;
DROP PROCEDURE IF EXISTS set_ingredient_name;
DROP PROCEDURE IF EXISTS set_cost_ingredient;
DROP PROCEDURE IF EXISTS set_vegan_ingredient;
DROP PROCEDURE IF EXISTS set_carb_ingredient;
DROP PROCEDURE IF EXISTS delete_ingredient;



DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / insert ingredients
CREATE PROCEDURE show_user_ingredients (IN user_id INT)
BEGIN

-- query to return all ingredients owned by a given user
SELECT
    i.ingredient_name,
    ui.quantity
FROM
    user u
JOIN
    user_has_ingredients ui ON u.user_id = ui.user_id
JOIN
    ingredients i ON ui.ingredient_id = i.ingredient_id
WHERE u.user_id = user_id;

END $$
DELIMITER ;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / insert ingredients
CREATE PROCEDURE add_ingredient_to_stock (IN user_id INT, IN ingredient_id INT, IN quantity INT)
BEGIN
    
	-- insert the information in the table
INSERT INTO user_has_ingredients (user_id, ingredient_id, quantity)
  VALUES (user_id, ingredient_id, quantity)
  ON DUPLICATE KEY UPDATE
    quantity = quantity + VALUES(quantity);

END $$
DELIMITER ;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / insert ingredients
CREATE PROCEDURE insert_ingredient (IN i_name Varchar(100), IN cost float(10,2), IN veg TINYINT(1), IN carb TINYINT(1))
-- define the procedure body
BEGIN
  
	-- insert the information in the table
    INSERT INTO ingredients (ingredient_name, cost_per, vegan, low_carb)
VALUES
    (i_name,cost,veg,carb);
    
SELECT 'Ingredient add!!';
END $$
DELIMITER ;


-- get all the specific information from Ingredient

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return ingredient name for a specific ingredient
CREATE PROCEDURE get_ingredient_name (IN ingredientID int, OUT ingredient_name VARCHAR(100))
-- define the procedure body
BEGIN
    SELECT	
		ingredient_name
    FROM
		ingredients
	WHERE	 
		ingredient_id = ingredientID;
                                     
END $$
DELIMITER ;


DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return ingredient name for a specific ingredient
CREATE PROCEDURE get_cost_name (IN ingredientID int, OUT cost_per FLOAT(10,2))
-- define the procedure body
BEGIN
    SELECT	
		cost_per
    FROM
		ingredients
	WHERE	 
		ingredient_id = ingredientID;
                                   
END $$
DELIMITER ;



DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return ingredient vegan for a specific ingredient
CREATE PROCEDURE get_vegan_ingredients (IN ingredientID int, OUT vegan TINYINT(1))
-- define the procedure body
BEGIN
    SELECT	
		vegan
    FROM
		ingredients
	WHERE	 
		ingredient_id = ingredientID;
                                   
END $$
DELIMITER ;


DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return ingredient vegan for a specific ingredient
CREATE PROCEDURE get_carb_ingredients (IN ingredientID int, OUT low_carb TINYINT(1))
-- define the procedure body
BEGIN
    SELECT	
		low_carb
    FROM
		ingredients
	WHERE	 
		ingredient_id = ingredientID;
                                   
END $$
DELIMITER ;

-- --------------------------------------------
-- set all the specific information from Ingredient

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return ingredient name for a specific ingredient
CREATE PROCEDURE set_ingredient_name (IN ingredientID int, IN i_name VARCHAR(100))
-- define the procedure body
BEGIN
    -- update the Ingredients table and set a specific ingredient
    UPDATE	ingredients
    set ingredient_name = i_name
    WHERE ingredient_id = ingredientID;
    
    SELECT 'Ingredient name update correctly!!';
                                     
END $$
DELIMITER ;


DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return ingredient name for a specific ingredient
CREATE PROCEDURE set_cost_ingredient (IN ingredientID int, IN newcost FLOAT(10,2))
-- define the procedure body
BEGIN
    -- update the Ingredients table and set a specific ingredient
    UPDATE	ingredients
    set cost_per = newcost
    WHERE ingredient_id = ingredientID;
    
    SELECT 'Ingredient cost update correctly!!';
                                     
END $$
DELIMITER ;



DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return ingredient vegan for a specific ingredient
CREATE PROCEDURE set_vegan_ingredient (IN ingredientID int, IN veg TINYINT(1))
-- define the procedure body
BEGIN
     -- update the Ingredients table and set a specific ingredient
    UPDATE	ingredients
    set vegan = veg
    WHERE ingredient_id = ingredientID;
    
    SELECT 'Ingredient vegan update correctly!!';
                                   
END $$
DELIMITER ;


DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return ingredient vegan for a specific ingredient
CREATE PROCEDURE set_carb_ingredient (IN ingredientID int, IN carb TINYINT(1))
-- define the procedure body
BEGIN
     -- update the Ingredients table and set a specific ingredient
    UPDATE	ingredients
    set low_carb = carb
    WHERE ingredient_id = ingredientID;
    
    SELECT 'Ingredient carb update correctly!!';
                                   
END $$
DELIMITER ;

-- delete an especific ingredient

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / deleting an ingredient
CREATE PROCEDURE delete_ingredient (IN ingredientID int)
-- define the procedure body
BEGIN
     -- delete an ingredient
    DELETE FROM ingredients
    WHERE ingredient_id = ingredientID;
    
    SELECT 'Ingredient was delete correctly!!';
                                   
END $$
DELIMITER ;




