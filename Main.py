import mysql.connector
import sys

# Database connection parameters
HOSTNAME = "localhost"
USERNAME = "root"
PASSWORD = None
DATABASE = "cookbook"

# Define a function to display the main menu
def show_principal_menu():
  print("** PRINCIPAL MENU **")
  print("1) Log in")
  print("2) Create user")
  print("3) Show user list")
  print("4) Exit")

# Define a function to validate user input
def validate_input(option):
  while not option.isdigit():
    print("The entry must be a number.")
    option = input("Enter an option: ")
  return int(option)

def validate_number(entrada):
  while not entrada.isdigit() or int(entrada) < 1 or int(entrada) > 5:
    print("La entrada debe ser un número entre 1 y 5.")
    entrada = input("Ingrese un número: ")
  return int(entrada)

# We define a function to display the user menu
def show_user_MENU():
  print("** MENU **")
  print("1) Ingredients")
  print("2) Recipes")
  print("3) Steps")
  print("4) Exit")

# We define a function to display the ingredients menu
def show_ingredients_MENU():
  print("** MENU **")
  print("1) Add ingredient")
  print("2) Modify ingredients")
  print("3) Delete ingredints")
  print("4) show ingredients list")
  print("5) Back")

# We define a function to display the recipe menu
def show_recipe_MENU():
  print("** MENU **")
  print("1) Add recipe")
  print("2) Modify recipe")
  print("3) Delete recipe")
  print("4) show recipe list")
  print("5) Back")

# We define a function to display the modify ingredients menu
def show_modify_ingredients_MENU():
  print("** MODIFY MENU **")
  print("1) Modify the ingredient name")
  print("2) Modify the ingredient cost")
  print("3) Modify the ingredient vegan")
  print("4) Modify the ingredient carb")
  print("5) Back")

# We define a function to display the modify recipe menu
def show_modify_recipe_MENU():
  print("** MODIFY MENU **")
  print("1) Modify the recipe name")
  print("2) Modify the recipe prep_time")
  print("3) Modify the recipe cook_time")
  print("4) Modify the recipe difficult level")
  print("5) Modify the recipe calories per serving")
  print("6) Modify the recipe vegan")
  print("7) Modify the recipe carb")
  print("8) Delete a recipe")
  print("9) Back")


# Define the function to insert a new ingredient
def insert_ingredient(id,name, cost, vegan, carb):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
        cursor = connection.cursor()

        query = """
            INSERT INTO Ingredients (id,name, cost, vegan, carb)
            VALUES (%s, %s, %s, %s, %s)
        """

        # Validate user input before inserting
        if not isinstance(id, int) or id <= 0:
            raise ValueError("Invalid user ID")
        if not name or not name.strip():
            raise ValueError("Invalid name")

        # Execute the query with user-provided data
        cursor.execute(query, (id,name, cost, vegan, carb))

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        # Return the result
        return result[0]
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
        connection.close()

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
        connection.close()

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
        connection.close()

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
        connection.close()

        # Return the result
        return result[0]
    except Exception as error:
        print(f"Error setting the carb ingredient: {error}")

# Define the function to set carb ingredient  
def delete_ingredient( ingredientID):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("delete_ingredient", (ingredientID))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        # Return the result
        return result[0]
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
        connection.close()

        # Return the result
        return result[0]
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

    cursor.execute("SELECT * FROM Ingredients")

    # Iterar sobre los resultados
    for row in cursor:
        # Imprimir los datos del usuario
        print(f"id: {row[0]}")
        print(f"name: {row[1]}")
        print(f"cost: {row[2]}")
        print(f"vegan: {row[3]}")
        print(f"carb: {row[4]}\n")

    # close the conection
    connection.close()

# Define the function to insert a new ingredient
def insert_recipe(id, name, p_time, c_time, diff_level, cal, vegan, carb):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
        cursor = connection.cursor()

        query = """
            INSERT INTO Recipe (id, name, p_time, c_time, diff_level, cal, vegan, carb)
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

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        # Return the result
        return result[0]
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
        connection.close()

        # Return the result
        return result[0]
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

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        # Return the result
        return result[0]
    except Exception as error:
        print(f"Error seting prep time in recipe: {error}")
        return None


# set the cook time
def set_cookTime_recipes(id, c_time):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_cookTime_recipes", (id, c_time))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        # Return the result
        return result[0]
    except Exception as error:
        print(f"Error seting cook time in recipe: {error}")
        return None

# set the difficult level
def set_diffLevel_recipes(id, level):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_diffLevel_recipes", (id, level))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        # Return the result
        return result[0]
    except Exception as error:
        print(f"Error seting diff level in recipe: {error}")
        return None

# set the calories per serving
def set_calories_per_serving_recipes(id, cal):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_calories_per_serving_recipes", (id, cal))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        # Return the result
        return result[0]
    except Exception as error:
        print(f"Error seting calories in recipe: {error}")
        return None

# set the vegan
def set_vegan_recipes(id, veg):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_vegan_recipesset_vegan_recipes", (id, veg))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        # Return the result
        return result[0]
    except Exception as error:
        print(f"Error seting vegan in recipe: {error}")
        return None

# set the carb
def set_carb_recipes(id, carb):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("set_carb_recipes", (id, carb))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        # Return the result
        return result[0]
    except Exception as error:
        print(f"Error seting carb in recipe: {error}")
        return None

# delete a recipe
def delete_recipe(id):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
        cursor = connection.cursor()

        # Execute the stored procedure
        cursor.callproc("delete_recipe", (id))

        # Fetch the result
        result = cursor.fetchone()

        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        # Return the result
        return result[0]
    except Exception as error:
        print(f"Error delete a recipe: {error}")
        return None

# Define the function to insert a new ingredient
def createuser(user_id, first_name, last_name, email_address, username):

    try:
        # Connect to the database
        connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
        )
        cursor = connection.cursor()

        query = """
            INSERT INTO User (user_ID, first_name, last_name, email_address, username)
            VALUES (%s, %s, %s, %s, %s)
        """
        # Validate user input before inserting
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("Invalid user ID")
        if not first_name or not first_name.strip():
            raise ValueError("Invalid first name")
        # ... (Perform similar validation for other inputs)

        # Execute the query with user-provided data
        cursor.execute(query, (user_id, first_name, last_name, email_address, username))
        # Commit the changes and close the connection
        connection.commit()
        connection.close()

        # Return the result
        return result[0]
    except Exception as error:
        #print(f"Error creating a new user: {error}")
        return None

def show_user():

    # Conectar con la base de datos
    connection = mysql.connector.connect(
            host=HOSTNAME, user=USERNAME, password=PASSWORD, database= DATABASE
    )
    cursor = connection.cursor()

    # Ejecutar la consulta
    cursor.execute("SELECT * FROM User")

    # Iterar sobre los resultados
    for row in cursor:
        # Imprimir los datos del usuario
        print(f"ID: {row[0]}")
        print(f"First Name: {row[1]}")
        print(f"last Name: {row[2]}")
        print(f"Email: {row[3]}")
        print(f"Username: {row[4]}\n")

    # Cerrar la conexión
    connection.close()







# We define a variable to store the userID
usuarioID = None

# We define a variable to store the nickname
nickname = None


#################
#   MAIN LOOP   #
#################

# main loop
while True:
  # We show the main menu
  show_principal_menu()

  # We get user input
  option = validate_input(input("Enter an option: "))

  # If the user selects option 1
  if option == 1:
    # We request the userID
    userID = input("Enter your userID: ")
    # We request the nickname
    nickname = input("Enter your nickname: ")


# code to verify the user is here ----------------------------------------------



    # If the userID and nickname are valid
    if userID and nickname:
      # We enter the user menu
      while True:
        # We show the user menu
        show_user_MENU()

        # We get user input
        option_user = validate_input(input("Enter an option: "))

        # If the user selects option 1
        if option_user == 1:
            # show the Ingredients MENU
            show_ingredients_MENU()
            # We get user input
            option_ingredients = validate_input(input("Enter an option: "))
            if option_ingredients == 1:
                # Enter the ingredient cost 
                ing_add_id = int(input("Enter the ingredient id: "))
                # Enter the ingredient name
                ing_add_name = input("Enter the ingredient name: ")
                # Enter the ingredient cost 
                ing_add_cost = float(input("Enter the cost per ingredient: "))
                # Enter if it is vegan or no
                aux1 = input("The ingredient is vegan?(yes/no): ")
                if aux1 == "yes" or aux1 == "Yes" or aux1 == "YES":
                    ing_add_veg = True
                else:    
                    ing_add_veg = False
                # Enter if it is low carb
                aux2 = input("The ingredient is low carb?(yes/no): ")
                if aux2 == "yes" or aux2 == "Yes" or aux2 == "YES":
                    ing_add_low_carb = True
                else:    
                    ing_add_low_carb = False
                # call the procedure insert_ingredient
                value = insert_ingredient(ing_add_id, ing_add_name, ing_add_cost, ing_add_veg, ing_add_veg)
                


            elif option_ingredients == 2:
                # show the menu to medify the ingredients
                show_modify_ingredients_MENU()
                # We get user input
                option_modify_ingredients = validate_input(input("Enter an option: "))
                if option_modify_ingredients == 1:
                   #enter the ingredient ID
                   mod_ing_ID = int(input("Enter the ingredient ID: "))
                   #Enter your new name
                   mod_ing_name = input("Enter the new ingredient name: ")
                   # set the ingredient name here
                   set_ingredient_name(mod_ing_ID,mod_ing_name)
                
                elif option_modify_ingredients == 2:
                    #enter the ingredient ID
                    mod_ing_ID = int(input("Enter the ingredient ID: "))
                    #enter the new ingredient cost
                    mod_ing_cost = int(input("Enter the new cost: "))
                    # set the ingredient cost here
                    set_cost_ingredient(mod_ing_ID,mod_ing_cost)    

                elif option_modify_ingredients == 3:
                    #enter the ingredient ID
                    mod_ing_ID = int(input("Enter the ingredient ID: "))
                    #enter the new ingredient cost
                    aux3 = input("Enter if the ingredient is vegan (yes/no): ")
                    if aux3 == "yes" or aux3 == "Yes" or aux3 == "YES":
                        mod_ing_veg = True
                    else:    
                        mod_ing_veg = False
                    # set the ingredient vegan here
                    set_vegan_ingredient(mod_ing_ID,mod_ing_veg)    

                elif option_modify_ingredients == 4:
                    #enter the ingredient ID
                    mod_ing_ID = int(input("Enter the ingredient ID: "))
                    #enter the new ingredient cost
                    aux4 = input("Enter if the ingredient is vegan (yes/no): ")
                    if aux4 == "yes" or aux4 == "Yes" or aux4 == "YES":
                        mod_ing_carb = True
                    else:    
                        mod_ing_carb = False
                    # set the ingredient carb here
                    set_carb_ingredient(mod_ing_ID,mod_ing_carb)    

                elif option_ingredients == 5:
                    # back to the before menu
                    break

            elif option_ingredients == 3:
                # select what ingredient do you want to delete
                #enter the ingredient ID
                delete_ing_ID = int(input("Enter the ingredient ID: "))
                # enter the code to delete the ingredient here 
                delete_ingredient(delete_ing_ID)

            elif option_ingredients == 4:
                # show the list of all the ingredients here 
                value = show_ingredients()

            elif option_ingredients == 5:
               # back to the before menu
               break

        # if select the number 2 show the recipe nemu
        elif option_user == 2:
            # Mshow the recipe menu
            show_recipe_MENU()
            # We get user input
            option_recipe = validate_input(input("Enter an option: "))
            if option_recipe == 1:
                # Enter the recipe ID 
                rec_add_ID = int(input("Enter the recipe ID: "))
                # Enter the recipe name
                rec_add_name = input("Enter the recipe name: ")
                # Enter the recipe prep_time 
                rec_add_prep_time = int(input("Enter the prep time: "))
                # Enter the recipe prep_time 
                rec_add_cook_time = int(input("Enter the cook time: "))
                # enter the difficulty level
                rec_add_diff = validate_number(int(input("Enter the difficult level: ")))
                # Enter the recipe calories per serving 
                rec_add_calories = int(input("Enter the calories per serving: "))
                # Enter if it is vegan or no
                aux1 = input("The ingredient is vegan?(yes/no): ")
                if aux1 == "yes" or aux1 == "Yes" or aux1 == "YES":
                    rec_add_veg = True
                else:    
                    rec_add_veg = False
                # Enter if it is low carb
                aux2 = input("The ingredient is low carb?(yes/no): ")
                if aux2 == "yes" or aux2 == "Yes" or aux2 == "YES":
                    rec_add_low_carb = True
                else:    
                    rec_add_low_carb = False
                # call the procedure insert_ingredient
                result = insert_recipe(rec_add_ID, rec_add_name, rec_add_prep_time, rec_add_cook_time, rec_add_veg, rec_add_veg)
                


            elif option_recipe == 2:
                # show the menu to medify the ingredients
                show_modify_recipe_MENU()
                option_modify_recipe = int(input("Choose an option: "))
                if option_modify_recipe == 1:
                    # Enter the recipe id to modify
                    mod_recipe_option = int(input("Enter the recipe id to modify: "))
                    #modify the recipe name
                    mod_recipe_name = input("Enter the new recipe name: ")
                    set_recipe_name(mod_recipe_option,mod_recipe_name)

                elif option_modify_recipe == 2:
                    # Enter the recipe id to modify
                    mod_recipe_option = int(input("Enter the recipe id to modify: "))
                    #modify the prep time
                    mod_recipe_prep_time = int(input("Enter the new prep time: "))
                    set_prepTime_recipes(mod_recipe_option,mod_recipe_prep_time)
                
                elif option_modify_recipe == 3:
                    # Enter the recipe id to modify
                    mod_recipe_option = int(input("Enter the recipe id to modify: "))
                    #modify the cook time
                    mod_recipe_cook_time = int(input("Enter the new cook time: "))
                    set_cookTime_recipes(mod_recipe_option,mod_recipe_cook_time)

                elif option_modify_recipe == 4:
                    # Enter the recipe id to modify
                    mod_recipe_option = int(input("Enter the recipe id to modify: "))
                    #modify the difficult level
                    mod_recipe_diffLevel = validate_number(int(input("Enter the difficult level: ")))
                    set_diffLevel_recipes(mod_recipe_option,mod_recipe_diffLevel)
                    
                elif option_modify_recipe == 5:
                    # Enter the recipe id to modify
                    mod_recipe_option = int(input("Enter the recipe id to modify: "))
                    #modify the calories
                    mod_recipe_cal = int(input("Enter the new calories per serving: "))
                    set_calories_per_serving_recipes(mod_recipe_option,mod_recipe_cal)

                elif option_modify_recipe == 6:
                    # Enter the recipe id to modify
                    mod_recipe_option = int(input("Enter the recipe id to modify: "))
                    #modify the vegan
                    aux5 = input("Enter the if it is vegan(yes/no): ")
                    if  aux5 == "yes" or aux5 == "YES" or aux5== "Yes":
                        mod_recipe_vegan = True
                    else:
                        mod_recipe_vegan =False
                    set_vegan_recipes(mod_recipe_option,mod_recipe_cal)

                elif option_modify_recipe == 7:
                    # Enter the recipe id to modify
                    mod_recipe_option = int(input("Enter the recipe id to modify: "))
                    #modify the low carb
                    aux6 = input("Enter the if it is low carb(yes/no): ")
                    if  aux6 == "yes" or aux6 == "YES" or aux6 == "Yes":
                        mod_recipe_carb = True
                    else:
                        mod_recipe_carb =False
                    set_carb_recipes(mod_recipe_option,mod_recipe_carb)

                elif option_modify_recipe == 8:
                    # Enter the recipe id to delete
                    mod_recipe_option = int(input("Enter the recipe id to delete: "))
                    delete_recipe(mod_recipe_option)

                elif option_user == 9:
                    # exit to the before menu
                    break

        # if the user select the option #3
        elif option_user == 3:
            # enter recipe id
            num_recipe_ID = int(input("Enter the recipe ID: "))
            # enter step number
            num_step_number = int(input("Enter the step number: "))
            # enter ingredient id
            num_ingredient_ID = int(input("Enter the ingredient ID: "))
            # enter step number
            num_quantity = int(input("Enter the quantity: "))
            #enter the instructions
            num_instruc = input("Enter here the instructions: ")
            #insert the information in the table recipe steps
            value = insert_recipe_step(num_recipe_ID, num_step_number, num_ingredient_ID, num_quantity, num_instruc )


        # if the user select the option #3
        elif option_user == 4:
            # exit to the main menu
            break

  # if the user select the option #2
  elif option == 2:
    # create a new user
    new_userID = int(input("Ingrese el id: "))
    new_first_name = input("Enter your first name: ")
    new_last_name = input("Enter your last name: ")
    new_email = input("Enter your email: ")
    new_username = input("Enter your username: ")
    value = createuser(new_userID, new_first_name, new_last_name, new_email, new_username)
    
    # if the user select the option #3
  elif option == 3:
    show_user()
    

  # if the user select the option #3
  elif option == 4:
    # exit of the program
    sys.exit()

