CREATE DATABASE IF NOT EXISTS cookbook;
USE cookbook;

DROP TABLE IF EXISTS recipe_steps;
DROP TABLE IF EXISTS user_has_ingredients;
DROP TABLE IF EXISTS ingredients;
DROP TABLE IF EXISTS recipes;
DROP TABLE IF EXISTS user;

-- create user table
CREATE TABLE user (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    email_address VARCHAR(100) UNIQUE,
    username VARCHAR(50) UNIQUE,
    passw VARCHAR(50)
);

-- insert dummy users
INSERT INTO user (user_id, first_name, last_name, email_address, username, passw)
VALUES
    (1, 'John', 'Doe', 'john.doe@email.com', 'jd', 'password'),
    (2, 'Jane', 'Smith', 'jane.smith@email.com', 'js_smith_1990', 'password'),
    (3, 'Bob', 'Johnson', 'bob.johnson@email.com', 'bob_j_1988', 'password'),
    (4, 'Alice', 'Williams', 'alice.williams@email.com', 'alice_w_1992', 'password'),
    (5, 'Charlie', 'Brown', 'charlie.brown@email.com', 'chuckie_b_1980', 'password'),
    (6, 'Eva', 'Jones', 'eva.jones@email.com', 'foreva_j_1987', 'password'),
    (7, 'Mike', 'Taylor', 'mike.taylor@email.com', 'mike_t_1983', 'password'),
    (8, 'Sara', 'Clark', 'sara.clark@email.com', 'sara_c_1995', 'password'),
    (9, 'David', 'Lee', 'david.lee@email.com', 'dlee_420', 'password'),
    (10, 'Anna', 'Martinez', 'anna.martinez@email.com', 'anna_m_1989', 'password');
    
-- Create Recipes table
CREATE TABLE recipes (
    recipe_id INT AUTO_INCREMENT PRIMARY KEY,
    recipe_name VARCHAR(100),
    prep_time INT,
    cook_time INT,
    difficulty_level TINYINT(5),
    calories_per_serving INT,
    vegan BOOLEAN,
    low_carb BOOLEAN
);

-- insert recipes
INSERT INTO recipes (recipe_id, recipe_name, prep_time, cook_time, difficulty_level, calories_per_serving, vegan, low_carb)
VALUES
    (1, 'Spaghetti Aglio e Olio', 10, 20, 2, 400, false, false),
    (2, 'Chicken Caesar Salad', 15, 0, 1, 350, false, true),
    (3, 'Vegetarian Stir Fry', 15, 15, 3, 300, true, true),
    (4, 'Grilled Cheese Sandwich', 5, 10, 1, 250, false, true),
    (5, 'Margherita Pizza', 20, 15, 4, 500, true, false),
    (6, 'Omelette', 10, 10, 2, 200, false, true),
    (7, 'Greek Salad', 10, 0, 1, 200, true, true),
    (8, 'Baked Salmon', 15, 20, 3, 350, false, true),
    (9, 'Pasta Primavera', 15, 20, 4, 300, true, false),
    (10, 'Tomato Basil Bruschetta', 10, 0, 2, 150, true, true);

-- Create Ingredients table
CREATE TABLE ingredients (
    ingredient_id INT AUTO_INCREMENT PRIMARY KEY,
    ingredient_name VARCHAR(100),
    cost_per DECIMAL(10, 2),
    vegan BOOLEAN,
    low_carb BOOLEAN
);

-- insert into ingredients table
INSERT INTO ingredients (ingredient_id, ingredient_name, cost_per, vegan, low_carb)
VALUES
    (1, 'Spaghetti', 0.99, false, false),
    (2, 'Olive Oil', 5.99, true, true),
    (3, 'Garlic', 2.49, true, true),
    (4, 'Chicken Breast', 7.99, false, true),
    (5, 'Romaine Lettuce', 2.99, true, true),
    (6, 'Parmesan Cheese', 4.49, false, true),
    (7, 'Bell Pepper', 1.99, true, true),
    (8, 'Salmon Fillet', 9.99, false, true),
    (9, 'Penne Pasta', 1.49, false, false),
    (10, 'Tomatoes', 3.99, true, true),
    (11, 'Eggs', 0.10, false, true);

-- create user ingredients table
CREATE TABLE user_has_ingredients (
    user_id INT,
    ingredient_id INT,
    quantity INT,
    PRIMARY KEY (user_id, ingredient_id),
    FOREIGN KEY (user_id) REFERENCES user(user_id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id)
);


-- insert user ingredients
INSERT INTO user_has_ingredients (user_id, ingredient_id, quantity)
VALUES
    (1, 1, 3),   -- Spaghetti
    (1, 2, 3),   -- Olive Oil
    (1, 3, 3),   -- Garlic

    (2, 4, 4),   -- Chicken Breast
    (2, 5, 2),   -- Romaine Lettuce
    (2, 6, 1),   -- Parmesan Cheese

    (3, 7, 3),   -- Bell Pepper
    (3, 8, 2),   -- Salmon Fillet
    (3, 9, 5),   -- Penne Pasta

    (4, 2, 1),   -- Olive Oil
    (4, 4, 3),   -- Chicken Breast
    (4, 5, 4),   -- Romaine Lettuce

    (5, 10, 5),  -- Tomatoes
    (5, 3, 2),   -- Garlic
    (5, 6, 1),   -- Parmesan Cheese

    (6, 8, 2),   -- Salmon Fillet
    (6, 1, 3),   -- Spaghetti
    (6, 7, 4),   -- Bell Pepper

    (7, 9, 2),   -- Penne Pasta
    (7, 2, 1),   -- Olive Oil
    (7, 4, 3),   -- Chicken Breast

    (8, 5, 3),   -- Romaine Lettuce
    (8, 3, 2),   -- Garlic
    (8, 7, 1),   -- Bell Pepper

    (9, 1, 4),   -- Spaghetti
    (9, 4, 2),   -- Chicken Breast
    (9, 8, 3),   -- Salmon Fillet

    (10, 10, 5), -- Tomatoes
    (10, 6, 2),  -- Parmesan Cheese
    (10, 2, 1);  -- Olive Oil

-- create recipe steps table
CREATE TABLE recipe_steps (
    recipe_id INT,
    step_number INT DEFAULT 1,
    ingredient_id INT,
    quantity INT,
    instructions TEXT,
    PRIMARY KEY (recipe_id, step_number),  -- Composite primary key
    FOREIGN KEY (recipe_id) REFERENCES recipes(recipe_id),
    FOREIGN KEY (ingredient_id) REFERENCES ingredients(ingredient_id)
);

DELIMITER $$

CREATE TRIGGER xxx BEFORE INSERT ON recipe_steps
FOR EACH ROW BEGIN
    SET NEW.step_number = (
       SELECT IFNULL(MAX(step_number), 0) + 1
       FROM recipe_steps
       WHERE recipe_id = NEW.recipe_id
    );
END $$

DELIMITER ;

-- insert recipe steps
INSERT INTO recipe_steps (recipe_id, ingredient_id, quantity, instructions)
VALUES
-- Recipe 1: Spaghetti Aglio e Olio
    (1, 1, 1, 'Boil water and cook spaghetti according to package instructions.'),
    (1, 2, 3, 'In a pan, sauté minced garlic in olive oil until golden.'),
    (1, 3, 2, 'Add cooked spaghetti to the pan and toss. Serve with grated Parmesan.'),

-- Recipe 2: Chicken Caesar Salad
    (2, 5, 1, 'Wash and chop Romaine lettuce.'),
    (2, 6, 1, 'Grate Parmesan cheese.'),
    (2, 4, 2, 'Grill chicken breast and slice into strips.'),
    (2, 6, 25, 'Toss lettuce, chicken, and Parmesan. Add Caesar dressing.'),

-- Recipe 3: Vegetarian Stir Fry
    (3, 7, 2, 'Slice bell pepper into strips.'),
    (3, 8, 1, 'Season salmon fillet and bake in the oven.'),
    (3, 9, 1, 'Cook penne pasta according to package instructions.'),
    (3, 7, 1, 'Sauté bell pepper. Toss with cooked pasta and top with baked salmon.'),

-- Recipe 4: Grilled Cheese Sandwich
    (4, 4, 2, 'Butter one side of each bread slice.'),
    (4, 6, 1, 'Place Parmesan cheese between bread slices.'),
    (4, 4, 2, 'Grill the sandwich until the bread is golden and the cheese is melted.'),

-- Recipe 5: Margherita Pizza
    (5, 10, 3, 'Slice tomatoes into thin rounds.'),
    (5, 6, 2, 'Slice fresh mozzarella.'),
    (5, 2, 2, 'Roll out pizza dough. Add tomato slices and mozzarella. Bake until crust is golden.'),

-- Recipe 6: Omelette

    (6, 11, 2, 'Season salmon fillet and bake in the oven.'),
    (6, 11, 2, 'Whisk eggs and pour into a hot, greased pan.'),
    (6, 11, 2, 'Flake baked salmon into the omelette. Fold and serve.'),

-- Recipe 7: Greek Salad

    (7, 5, 1, 'Wash and chop Romaine lettuce.'),
    (7, 6, 1, 'Grate Parmesan cheese.'),
    (7, 10, 3, 'Slice tomatoes and olives. Toss with lettuce, cheese, and Greek dressing.'),

-- Recipe 8: Baked Salmon

    (8, 8, 1, 'Season salmon fillet and bake in the oven until cooked through.'),

-- Recipe 9: Pasta Primavera

    (9, 9, 1, 'Cook penne pasta according to package instructions.'),
    (9, 7, 2, 'Slice bell pepper into strips and sauté with garlic.'),
    (9, 10, 2, 'Dice tomatoes. Toss cooked pasta with vegetables.'),

-- Recipe 10: Tomato Basil Bruschetta

    (10, 10, 3, 'Dice tomatoes and basil. Mix with olive oil and garlic.'),
    (10, 6, 1, 'Grate Parmesan cheese.'),
    (10, 4, 2, 'Slice baguette, toast, and top with tomato mixture and Parmesan.');

SOURCE cookbook_user_procedure_queries.sql
SOURCE cookbook_recipes_procedure_queries.sql
SOURCE cookbook_ingredient_procedure_queries.sql