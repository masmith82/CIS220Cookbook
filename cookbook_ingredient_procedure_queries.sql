use cookbook;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / insert ingredients
CREATE PROCEDURE insert_ingredient (IN i_name Varchar(100), IN cost float(10,2), IN veg TINYINT(1), IN carb TINYINT(1))
-- define the procedure body
BEGIN
	-- declare the ingredient_Id 
	DECLARE ingredient_Id INT
    SET ingredient_Id = 1;
    
    -- search the user id in the user table
	SELECT ingredient_Id = MAX(ingredient_id)
	FROM Ingredients;
	SET ingredient_Id = ingredient_Id + 1;
    
	-- insert the information in the table
    INSERT INTO Ingredients (ingredient_id, ingredient_name, cost_per, vegan, low_carb)
VALUES
    (ingredient_Id,i_name,cost,veg,carb);
    
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
		Ingredients
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
		Ingredients
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
		Ingredients
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
		Ingredients
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
    UPDATE	Ingredients
    set ingredient_name = i_name;
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
    UPDATE	Ingredients
    set cost_per = newcost;
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
    UPDATE	Ingredients
    set vegan = veg;
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
    UPDATE	Ingredients
    set low_carb = carb;
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
    DELETE FROM Ingredients
    WHERE ingredient_id = ingredientID;
    
    SELECT 'Ingredient was delete correctly!!';
                                   
END $$
DELIMITER ;




