use cookbook;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / create a new recipe
CREATE PROCEDURE create_recipe (IN rec_name Varchar(100), IN p_time INT, IN c_time INT, IN diff_level TINYINT(5), IN calories INT, IN veg TINYINT(1), IN carb TINYINT(1))
-- define the procedure body
BEGIN
	-- declare the ingredient_Id 
	DECLARE ID INT
    SET ID = 1;
    
    -- search the user id in the user table
	SELECT ID = MAX(recipe_ID)
	FROM recipes;
	SET ID = ID + 1;
    
	-- insert the information in the table
    INSERT INTO Recipes (recipe_ID, recipe_name, prep_time, cook_time, difficulty_level, calories_per_serving, vegan, low_carb)
VALUES
    (ID, rec_name, p_time, c_time, diff_level, calories, veg, carb);
    
SELECT 'Recipe created!!';
END $$
DELIMITER ;


-- get all the specific information from recipes

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return recipe name for a specific recipe
CREATE PROCEDURE get_recipe_name (IN recipeID int, OUT recipe_name VARCHAR(100))
-- define the procedure body
BEGIN
    SELECT	
		recipe_name
    FROM
		Recipes
	WHERE	 
		recipe_ID = recipeID;
                                     
END $$
DELIMITER ;


DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return preparation time for a specific recipe
CREATE PROCEDURE get_prepTime_recipes (IN recipeID int, OUT prep_time INT)
-- define the procedure body
BEGIN
    SELECT	
		prep_time
    FROM
		Recipes
	WHERE	 
		recipe_ID = recipeID;
                                     
END $$
DELIMITER ;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return cook time for a specific recipe
CREATE PROCEDURE get_cookTime_recipes (IN recipeID int, OUT cook_time INT)
-- define the procedure body
BEGIN
    SELECT	
		cook_time
    FROM
		Recipes
	WHERE	 
		recipe_ID = recipeID;
                                     
END $$
DELIMITER ;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return complexity for a specific recipe
CREATE PROCEDURE get_difficulty_level_recipes (IN recipeID int, OUT difficulty_level TINYINT(5))
-- define the procedure body
BEGIN
    SELECT	
		difficulty_level
    FROM
		Recipes
	WHERE	 
		recipe_ID = recipeID;
                                     
END $$
DELIMITER ;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return calories for a specific recipe
CREATE PROCEDURE get_calories_recipes (IN recipeID int, OUT calories_per_serving INT)
-- define the procedure body
BEGIN
    SELECT	
		calories_per_serving
    FROM
		Recipes
	WHERE	 
		recipe_ID = recipeID;
                                     
END $$
DELIMITER ;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return vegan for a specific recipe
CREATE PROCEDURE get_vegan_recipes (IN recipeID int, OUT vegan TINYINT(1))
-- define the procedure body
BEGIN
    SELECT	
		vegan
    FROM
		Recipes
	WHERE	 
		recipe_ID = recipeID;
                                     
END $$
DELIMITER ;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / return carb for a specific recipe
CREATE PROCEDURE get_carb_recipes (IN recipeID int, OUT low_carb TINYINT(1))
-- define the procedure body
BEGIN
    SELECT	
		low_carb
    FROM
		Recipes
	WHERE	 
		recipe_ID = recipeID;
                                     
END $$
DELIMITER ;

-- ----------------------------------------------------------
-- set all the specific information from recipes

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / change recipe name for a specific recipe
CREATE PROCEDURE set_recipe_name (IN recipeID int, IN newname VARCHAR(100))
-- define the procedure body
BEGIN
    -- update the Ingredients table and set a specific ingredient
    UPDATE	Recipes
    set recipe_name = newname;
    WHERE recipe_ID = recipeID;
    
    SELECT 'Recipe name update correctly!!';
                                     
END $$
DELIMITER ;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / change preparation time for a specific recipe
CREATE PROCEDURE set_prepTime_recipes (IN recipeID int, IN pTime INT)
-- define the procedure body
BEGIN
    -- update the Ingredients table and set a specific ingredient
    UPDATE	Recipes
    set prep_time = pTime;
    WHERE recipe_ID = recipeID;
    
    SELECT 'Prep time update correctly!!';
                                     
END $$
DELIMITER ;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / change cook time for a specific recipe
CREATE PROCEDURE set_cookTime_recipes (IN recipeID int, IN cTime INT)
-- define the procedure body
BEGIN
    -- update the Ingredients table and set a specific ingredient
    UPDATE	Recipes
    set prep_time = cTime;
    WHERE recipe_ID = recipeID;
    
    SELECT 'Cook time update correctly!!';
                                     
END $$
DELIMITER ;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / change difficult level for a specific recipe
CREATE PROCEDURE set_diffLevel_recipes (IN recipeID int, IN dlevel TINYINT(5))
-- define the procedure body
BEGIN
    -- update the Ingredients table and set a specific ingredient
    UPDATE	Recipes
    set difficulty_level = dlevel;
    WHERE recipe_ID = recipeID;
    
    SELECT 'Difficult level update correctly!!';
                                     
END $$
DELIMITER ;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / change difficult level for a specific recipe
CREATE PROCEDURE set_calories_per_serving_recipes (IN recipeID int, IN cal INT)
-- define the procedure body
BEGIN
    -- update the Ingredients table and set a specific ingredient
    UPDATE	Recipes
    set calories_per_serving = cal;
    WHERE recipe_ID = recipeID;
    
    SELECT 'Serving Calories update correctly!!';
                                     
END $$
DELIMITER ;

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / change difficult level for a specific recipe
CREATE PROCEDURE set_vegan_recipes (IN recipeID int, IN veg TINYINT(1))
-- define the procedure body
BEGIN
    -- update the Ingredients table and set a specific ingredient
    UPDATE	Recipes
    set vegan = veg;
    WHERE recipe_ID = recipeID;
    
    SELECT 'Vegan update correctly!!';
                                     
END $$
DELIMITER ;


DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / change difficult level for a specific recipe
CREATE PROCEDURE set_carb_recipes (IN recipeID int, IN carb TINYINT(1))
-- define the procedure body
BEGIN
    -- update the Ingredients table and set a specific ingredient
    UPDATE	Recipes
    set low_carb = carb;
    WHERE recipe_ID = recipeID;
    
    SELECT 'Low carb update correctly!!';
                                     
END $$
DELIMITER ;


-- delete an especific recipe

DELIMITER $$ -- temporary delimiter to take place of ;
USE cookbook$$ 
-- Input parameters and output parameters / deleting a recipe
CREATE PROCEDURE delete_recipe (IN recipeID int)
-- define the procedure body
BEGIN
     -- delete a recipe
    DELETE FROM Recipes
    WHERE recipe_ID = recipeID;
    
    SELECT 'Recipe was delete correctly!!';
                                   
END $$
DELIMITER ;
