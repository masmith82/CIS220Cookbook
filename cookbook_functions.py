import mysql.connector
import sys

# Database connection parameters
HOSTNAME = "localhost"
USERNAME = "root"
PASSWORD = "MJw!0TeN!0"
DATABASE = "cookbook"

# global variable to hold the database connection
connection = None

########################
# DATABASE INTERACTION #
########################

# Connect to the database
# JORGE: Put this into it's own function and set up 'connection' as a global variable, so any function can use it
def connect() -> mysql.connector.connect:
    global connection

    try:
        connection = mysql.connector.connect(
            host = HOSTNAME, user = USERNAME, password = PASSWORD, database = DATABASE
        )
        return connection
    except Exception as error:
        print(f"Error connecting to the database: {error}")
        sys.exit()

connection = connect()

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

###################################
# DATABASE MANIPULATION FUNCTIONS #
###################################

# Define the function to insert a new ingredient
def insert_ingredient(id, name, cost, vegan, carb):
    try:
        cursor = connection.cursor()

        query = """
            INSERT INTO Ingredients (ingredient_id, name, cost, vegan, carb)
            VALUES (%s, %s, %s, %s, %s)
        """

        # Validate user input before inserting
        if not isinstance(id, int) or id <= 0:
            raise ValueError("Invalid user ID")
        if not name or not name.strip():
            raise ValueError("Invalid name")

        # Execute the query with user-provided data
        cursor.execute(query, (id,name, cost, vegan, carb))

        # Commit the changes
        connection.commit()
    
    except Exception as error:
        print(f"Error inserting ingredient: {error}")
        return None


# Define the function to set_ingredient_name 
def set_ingredient_name( ingredientID, i_name):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_ingredient_name", (ingredientID, i_name))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()

        # Return the result
        #return result[0]
    except Exception as error:
        print(f"Error setting the ingredient name: {error}")

# Define the function to set ingredient cost  
def set_cost_ingredient( ingredientID, cost):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_cost_ingredient", (ingredientID, cost))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()

        # Return the result
        #return result[0]
    except Exception as error:
        print(f"Error setting the ingredient cost: {error}")


# Define the function to set vegan ingredient  
def set_vegan_ingredient( ingredientID, vegan):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_vegan_ingredient", (ingredientID, vegan))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()

        # Return the result
        return result[0]
    except Exception as error:
        print(f"Error setting the vegan ingredient: {error}")

# Define the function to set carb ingredient  
def set_carb_ingredient( ingredientID, carb):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_carb_ingredient", (ingredientID, carb))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()

        # Return the result
        return result[0]
    except Exception as error:
        print(f"Error setting the carb ingredient: {error}")

# Define the function to set carb ingredient  
def delete_ingredient( ingredientID):

    try:
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("delete_ingredient", (ingredientID))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()

    except Exception as error:
        print(f"Error deleting ingredient: {error}")


# Define the function to insert recipe steps
def insert_recipe_step(recipe_id, step_number, ingredient_id, quantity, instructions):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
        cursor = connection.cursor()

        query = """
            INSERT INTO Recipe_Steps (recipe_id, step_number, ingredient_id, quantity, instructions)
            VALUES (%s, %s, %s, %s, %s)
        """

        # Validate user input before inserting
        if not isinstance(recipe_id, int) or recipe_id <= 0:
            raise ValueError("Invalid user ID")
        if not ingredient_id or not ingredient_id.strip():
            raise ValueError("Invalid first name")
        # ... (Perform similar validation for other inputs)

        # Execute the query with user-provided data
        cursor.execute(query, (recipe_id, step_number, ingredient_id, quantity, instructions))

        # Commit the changes and close the connection
        connection.commit()

    except Exception as error:
        print(f"Error inserting recipe step: {error}")
        return None

# Define the function to show the ingredients
def show_ingredients():
    # made the conection with the DB
    connection = mysql.connector.connect(
        host = HOSTNAME, user = USERNAME, password = PASSWORD, database = DATABASE
    )
    cursor = connection.cursor()

    # call the ingredients from the cookbook

    cursor.execute("SELECT * FROM ingredients")

    # Iterar sobre los resultados
    for row in cursor:
        # Imprimir los datos del usuario
        print(f"id: {row[0]}")
        print(f"name: {row[1]}")
        print(f"cost: {row[2]}")
        print(f"vegan: {row[3]}")
        print(f"carb: {row[4]}\n")


# Define the function to insert a new ingredient
def insert_recipe(id, name, p_time, c_time, diff_level, cal, vegan, carb):

    try:
        # Connect to the database
        cursor = connection.cursor()

        query = """
            INSERT INTO Recipe (recipe_id, recipe_name, p_time, c_time, diff_level, cal, vegan, carb)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        # Validate user input before inserting
        if not isinstance(id, int) or id <= 0:
            raise ValueError("Invalid user ID")
        if not name or not name.strip():
            raise ValueError("Invalid first name")
        # ... (Perform similar validation for other inputs)

        # Execute the query with user-provided data
        cursor.execute(query, (id, name, p_time, c_time, diff_level, cal, vegan, carb))
        connection.commit()

    except Exception as error:
        print(f"Error inserting recipe: {error}")
        return None
    
# set the recipe name
def set_recipe_name(id, name):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
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
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
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

# Define the function to insert a new ingredient
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