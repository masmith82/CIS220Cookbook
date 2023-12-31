import mysql.connector
import sys
from cookbook_menus import validate_input, validate_quantity

# Database connection parameters
HOSTNAME = "localhost"
USERNAME = "root"
DATABASE = "cookbook"

# global variable to hold the database connection
connection = None

########################
# DATABASE INTERACTION #
########################

# Connect to the database
# JORGE: I put this into it's own function and set up 'connection' as a global variable, so any function can use it
def connect() -> mysql.connector.connect:
    global connection
    passw = input("Enter sql password: ")
    try:
        connector = mysql.connector.connect(
            host = HOSTNAME, user = USERNAME, password = passw, database = DATABASE
        )
        connection = connector
        return connector
    except Exception as error:
        print(f"Error connecting to the database: {error}")
        sys.exit()

def disconnect():
    global connection
    try:
        connection.close()
        print("Connection closed successfully!")
    except Exception as error:
        print(f"Error closing the connection: {error}")
        sys.exit()

###################
# USER VALIDATION #
###################

# Called from login(). Check if the user exists in the database
def user_exists(username):
    cursor = connection.cursor()
    query = "SELECT COUNT(*) FROM user WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    return result[0] > 0        # Return true if the user exists

# Called from login(). Verify the password for the given username
def verify_password(username, password):
    cursor = connection.cursor()
    query = "SELECT passw FROM user WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    if str(result[0]) == password:
        return True
    else:
        return False
    
def get_user_id(username):
    cursor = connection.cursor()
    query = "SELECT user_id FROM user WHERE username = %s"
    cursor.execute(query, (username,))
    result = cursor.fetchone()
    return result[0]

########################
# INGREDIENT FUNCTIONS #
########################

# show all ingredients
def show_ingredients():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM ingredients")

    # Iterar sobre los resultados
    print("\nIngredient List")
    print("=" * 60)
    for row in cursor:
        print(f"id: {row[0]:<3} - {row[1]:<20} cost: ${row[2]:<10} vegan: {parse_bool(row[3]):<5} low carb: {parse_bool(row[4]):<5}")
    print("\n")

# show's ingredients in a user's stock
def show_user_ingredients(current_user):
    cursor = connection.cursor()
    cursor.callproc('show_user_ingredients', (current_user, ))
    for result in cursor.stored_results():
        print(f"\n{'Ingredient':<15} {'Quantity'}")
        print("=" * 30)
        for row in result.fetchall():
            print(f"{row[0]:<15} {row[1]}")
    print("\n")

# adds a quantity of ingredient to a user's stock
def add_ingredient_to_stock(current_user):
    cursor = connection.cursor()
    show_ingredients()
    ingredient_id = validate_input(input("Enter the ingredient ID to add: "))
    ingedient_quantity = validate_input(input("Enter the quantity to add: "))
    cursor.callproc('add_ingredient_to_stock', (current_user, ingredient_id, ingedient_quantity))
    connection.commit()
    print("\n")


# helper function to replace 1 and 0 with Y and N
def parse_bool(value):
    if value == 1:
        return "Y"
    else:
        return "N"

# Define the function to insert a new ingredient
def insert_ingredient(name, cost, vegan, carb):
    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO Ingredients (ingredient_name, cost_per, vegan, low_carb)
            VALUES (%s, %s, %s, %s)
        """

        if not name or not name.strip():
            raise ValueError("Invalid name")

        # Execute the query with user-provided data
        cursor.execute(query, (name, cost, vegan, carb))

        # Commit the changes
        connection.commit()
        print("\nIngredient created successfully!\n")
    
    except Exception as error:
        print(f"Error inserting ingredient: {error}")
        return None

#####################################
# INGREDIENT MODIFICATION FUNCTIONS #
#####################################

# Define the function to set_ingredient_name 
def set_ingredient_name( ingredient_id, i_name):
    try:
        cursor = connection.cursor()
        # Execute the stored procedure
        cursor.callproc("set_ingredient_name", (ingredient_id, i_name))

        # Commit the changes and close the connection
        connection.commit()

    except Exception as error:
        print(f"Error setting the ingredient name: {error}")

# Define the function to set ingredient cost  
def set_cost_ingredient( ingredient_id, cost):

    try:
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_cost_ingredient", (ingredient_id, cost))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()

        # Return the result
        #return result[0]
    except Exception as error:
        print(f"Error setting the ingredient cost: {error}")


# Define the function to set vegan ingredient  
def set_vegan_ingredient( ingredient_id, vegan):

    try:
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_vegan_ingredient", (ingredient_id, vegan))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()

        # Return the result
        return result[0]
    except Exception as error:
        print(f"Error setting the vegan ingredient: {error}")

# Define the function to set carb ingredient  
def set_carb_ingredient( ingredient_id, carb):

    try:
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_carb_ingredient", (ingredient_id, carb))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()

        # Return the result
        return result[0]
    except Exception as error:
        print(f"Error setting the carb ingredient: {error}")

# Define the function to set carb ingredient  
def delete_ingredient( ingredient_id):
    try:
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("delete_ingredient", (ingredient_id,))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()

    except Exception as error:
        print(f"Error deleting ingredient: {error}")

####################
# RECIPE FUNCTIONS #
####################

def list_recipes():
        cursor = connection.cursor()

        query = """
            SELECT recipe_id, recipe_name FROM recipes
        """
        
        cursor.execute(query)
        for row in cursor:
            print(f"{row[0]:<3} - {row[1]:<20}")

def list_recipe_detail(recipe_id):
    cursor = connection.cursor()

    query = """
        SELECT recipe_name, difficulty_level, prep_time, cook_time, calories_per_serving, vegan, low_carb
        FROM recipes
        WHERE recipe_id = %s      
    """     
    cursor.execute(query, (recipe_id,))
    if cursor.rowcount == 0:
        print("No recipe steps found")
        return None
    for row in cursor:
        print(f"\n{row[0]:<3}")
        print(f"Difficulty: {'★ ' * int(row[1])}")
        print(f"Prep Time: {row[2]} minutes | Cook Time: {row[3]} minutes")
        print(f"Calories per serving: {row[4]}")
        print(f"Vegan: {parse_bool(row[5])} | Low Carb: {parse_bool(row[6])}")
        print("\n")
        get_recipe_steps(recipe_id)


# Define the function to insert a new ingredient
def insert_recipe(name, p_time, c_time, diff_level, cal, vegan, carb):
    try:
        # Connect to the database
        cursor = connection.cursor()

        query = """
            INSERT INTO recipes (recipe_name, prep_time, cook_time, difficulty_level, calories_per_serving, vegan, low_carb)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """

        if not name or not name.strip():
            raise ValueError("Invalid first name")
        # ... (Perform similar validation for other inputs)

        # Execute the query with user-provided data
        cursor.execute(query, (name, p_time, c_time, diff_level, cal, vegan, carb))
        connection.commit()
        print("\nRecipe created successfully!\n")

    except Exception as error:
        print(f"Error inserting recipe: {error}")
        return None


# delete a recipe
def delete_recipe(id):
    try:
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("delete_recipe", (id))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()

    except Exception as error:
        print(f"Error delete a recipe: {error}")
        return None


#########################
# RECIPE STEP FUNCTIONS #
##########################

def get_recipe_steps(recipe_id):
    cursor = connection.cursor()
    query = """
        SELECT step_number, i.ingredient_name, quantity, instructions
        FROM recipe_steps rs
        INNER JOIN ingredients i ON rs.ingredient_id = i.ingredient_id
        WHERE recipe_id = %s
    """
    cursor.execute(query, (recipe_id,))
    step = 1
    for row in cursor:
        if row[1] == None:          # if no ingredient is found, set the name to None
            row[1] = "None"
        print(f"Step {step}:\n=======\nIngredients used: {row[1]} x {row[2]}\nInstructions: {row[3]}")
        step += 1                    # increment the step number, this is because step_number in the database my not be sequential due to how AUTO_INCREMENT works

  
def add_recipe_step(recipe_id):
    cursor = connection.cursor()
    list_recipe_detail(recipe_id)
    ingredient_quantity = 0         # initialize the ingredient quantity to 0                   
    ingredient_id = validate_input(input("Enter the ingredient ID to add: "))
    if ingredient_id != None:       # if the ingredient id is valid, ask for the quantity
        ingredient_quantity = validate_quantity(input("Enter the quantity to add: "))
    instructions = input("Enter the instructions: ")

    query = """
        INSERT INTO recipe_steps (recipe_id, ingredient_id, quantity, instructions)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (recipe_id, ingredient_id, ingredient_quantity, instructions))
    connection.commit()
    print("\n")

def delete_recipe_step(recipe_id, step_number):
    try:
        cursor = connection.cursor()
        step_number = validate_input(input("Enter the step number to delete: "))
        query = """
            DELETE FROM recipe_steps
            WHERE recipe_id = %s AND step_number = %s
        """
        cursor.execute(query, (recipe_id, step_number))
        connection.commit()
        print("\n")
        
    except Exception as error:
        print(f"Error deleting recipe step: {error}")
  
###########################
# RECIPE FILTER FUNCTIONS #
###########################

# simple filters for vegan and low carb options
def basic_recipe_filter(type):
    title = ""
    if type == 1:
        title = "\nVegan Recipes"
        query = """
            SELECT recipe_id, recipe_name FROM recipes
            WHERE vegan = 1
        """
    if type == 2:
        title = "\nLow-Carb Recipes"
        query = """
            SELECT recipe_id, recipe_name FROM recipes
            WHERE low_carb = 1
        """
    if type == 3:
        title = "\nLow-Carb Vegan Recipes"
        query = """
            SELECT recipe_id, recipe_name FROM recipes
            WHERE low_carb = 1 AND vegan = 1
        """

    cursor = connection.cursor()
    cursor.execute(query)
    print(title)
    print("=" * 30)
    for row in cursor:
        print(f"{row[0]:<3} - {row[1]:<20}")
        
def filter_by_calories(calories):
    query = """
        SELECT recipe_id, recipe_name FROM recipes
        WHERE calories_per_serving <= %s
    """
    cursor = connection.cursor()
    cursor.execute(query, (calories,))
    print("\nRecipes with less than " + str(calories) + " calories per serving:")
    print("=" * 60)
    results = cursor.fetchall()
    for row in results:
        query = """
            SELECT calories_per_serving FROM recipes
            WHERE recipe_id = %s
        """
        cursor.execute(query, (row[0],))
        for subrow in cursor:
            print(f"{row[0]:<3} - {row[1]:<30} | Calories: {subrow[0]}")
        
# filter by total prep + cook time
def filter_by_time(time):
    query = """
        SELECT recipe_id, recipe_name FROM recipes
        WHERE prep_time + cook_time <= %s
    """
    cursor = connection.cursor()
    cursor.execute(query, (time,))
    print("\nRecipes that can be made in under " + str(time) + " minutes total:")
    print("=" * 60)
    results = cursor.fetchall()
    for row in results:       
        query = """
            SELECT prep_time, cook_time, SUM(prep_time + cook_time) FROM recipes
            WHERE recipe_id = %s
        """
        cursor.execute(query, (row[0],))
        for subrow in cursor:
            print(f"{row[0]:<3} - {row[1]:<30} | Prep Time: {subrow[0]} | Cook Time: {subrow[1]} | Total Time: {subrow[2]}")

def filter_by_my_ingredients(current_user):
    cursor = connection.cursor()
    query = """
        SELECT DISTINCT R.recipe_id, R.recipe_name, R.prep_time, R.cook_time, R.difficulty_level, R.calories_per_serving, R.vegan, R.low_carb
        FROM recipes R
        JOIN
            (SELECT RS.recipe_id, I.ingredient_id, SUM(RS.quantity) AS total_required
                FROM recipe_steps RS
                JOIN ingredients I ON RS.ingredient_id = I.ingredient_id
                GROUP BY RS.recipe_id, I.ingredient_id)
        AS RecipeTotal ON R.recipe_id = RecipeTotal.recipe_id
        JOIN recipe_steps RS ON R.recipe_id = RS.recipe_id
        JOIN ingredients I ON RS.ingredient_id = I.ingredient_id
        JOIN user_has_ingredients UI ON I.ingredient_id = UI.ingredient_id
        WHERE
            UI.user_id = %s
        GROUP BY
            R.recipe_ID
        HAVING
            COUNT(*) = COUNT(CASE WHEN UI.quantity >= RecipeTotal.total_required THEN 1 END);
        """
    cursor.execute(query, (current_user,))
    print("\nRecipes I can make with my ingredients:")
    print("=" * 60)
    results = cursor.fetchall()
    for row in results:
        query = """
            SELECT DISTINCT i.ingredient_name, rs.quantity FROM ingredients i
            JOIN recipe_steps rs ON i.ingredient_id = rs.ingredient_id
            WHERE rs.recipe_id = %s
        """
        cursor.execute(query, (row[0],))
        print(f"\nRecipe ID: {row[0]:<2} - {row[1]:<30}")
        print(f"Ingrdients needed:")
        for subrow in cursor:
            print(f"{'':<3} - {subrow[0]:<30} x {subrow[1]}")
        
#################################
# RECIPE MODIFICATION FUNCTIONS #
#################################

# set the recipe name
def set_recipe_name(id, name):
    try:
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_recipe_name", (id, name))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()

    except Exception as error:
        print(f"Error seting recipe name: {error}")
        return None

# set the prep time
def set_prepTime_recipes(id, p_time):
    try:
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_prepTime_recipes", (id, p_time))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes
        connection.commit()

    except Exception as error:
        print(f"Error seting prep time in recipe: {error}")
        return None


# set the cook time
def set_cookTime_recipes(id, c_time):
    try:
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_cookTime_recipes", (id, c_time))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()


    except Exception as error:
        print(f"Error seting cook time in recipe: {error}")
        return None

# set the difficult level
def set_diffLevel_recipes(id, level):
    try:
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_diffLevel_recipes", (id, level))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()

    except Exception as error:
        print(f"Error seting diff level in recipe: {error}")
        return None

# set the calories per serving
def set_calories_per_serving_recipes(id, cal):
    try:
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_calories_per_serving_recipes", (id, cal))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()

    except Exception as error:
        print(f"Error seting calories in recipe: {error}")
        return None

# set the vegan
def set_vegan_recipes(id, veg):
    try:
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_vegan_recipesset_vegan_recipes", (id, veg))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()

        return result[0]
    except Exception as error:
        print(f"Error seting vegan in recipe: {error}")
        return None

# set the carb
def set_carb_recipes(id, carb):
    try:
        # Connect to the database
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_carb_recipes", (id, carb))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()
 
    except Exception as error:
        print(f"Error seting carb in recipe: {error}")
        return None


##################
# USER FUNCTIONS #
##################   

# Define the function to insert a new user
def create_user(first_name, last_name, email_address, username, passw = "password"):
    try:
        print("Creating")

        cursor = connection.cursor()

        query = """
            INSERT INTO User (first_name, last_name, email_address, username, passw)
            VALUES (%s, %s, %s, %s, %s)
        """
        # Validate user input before inserting
        if not first_name or not first_name.strip():
            raise ValueError("Invalid name")
        # ... (Perform similar validation for other inputs)

        # Execute the query with user-provided data
        cursor.execute(query, (first_name, last_name, email_address, username, passw))
        # Commit the changes and close the connection
        connection.commit()
        print("User created successfully!")

    except Exception as error:
        print(f"Error creating a new user: {error}")
        return None

def show_user():
    cursor = connection.cursor()

    # Ejecutar la consulta
    cursor.execute("SELECT * FROM user")

    # Iterar sobre los resultados
    for row in cursor:
        # Imprimir los datos del usuario
        print(f"ID: {row[0]}")
        print(f"First Name: {row[1]}")
        print(f"last Name: {row[2]}")
        print(f"Email: {row[3]}")
        print(f"Username: {row[4]}\n")