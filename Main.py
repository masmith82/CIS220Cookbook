import sys
from cookbook_menus import *
from cookbook_functions import *

current_user = None         # store current user_id for this session

# login the user
def login():
    # We request the userID
    userID = input("Enter your userID: ")
    
    if not user_exists(userID):
        print("User does not exist.")
        return
    
    # We request the password
    passw = input("Enter your password: ")

    if not verify_password(userID, passw):
        print("Invalid password.")
        return

    # code to verify the user is here ----------------------------------------------

    # if user is valid we show the user menu
    if userID and passw:
        print("\nLogin successful. \nWelcome, " + userID + "!\n")
        global current_user
        current_user= get_user_id(userID)
        user_menu()


def create_new_user():
    #new_userID = int(input("Ingrese el id: "))     # we should let the databas assign the user ID
    new_first_name = input("Enter your first name: ")
    new_last_name = input("Enter your last name: ")
    new_email = input("Enter your email: ")
    new_username = input("Enter your username: ")
    new_password = input("Choose a password: ")
    value = create_user(new_first_name, new_last_name, new_email, new_username, new_password)

# user menu, displays after login
def user_menu():
    while True:
        show_user_menu()
        option = validate_input(input("\nEnter an option: "))     # get input
        
        if option == 1:
            ingredient_menu()               # go to ingredients menu          
        elif option == 2:
            recipe_menu()                   # go to recipe menu
        elif option == 3:
            break                           # exit to main menu

# menu to manage ingredients
def ingredient_menu():
    while True:
        show_ingredients_MENU()

        option_ingredients = validate_input(input("Enter an option: "))
        if option_ingredients == 1:         # add ingredient
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

        elif option_ingredients == 2:           # modify ingredient submenu
            modify_ingredients_menu()

        elif option_ingredients == 3:           # delete ingredient
            # select what ingredient do you want to delete
            #enter the ingredient ID
            delete_ing_ID = int(input("Enter the ingredient ID: "))
            # enter the code to delete the ingredient here 
            delete_ingredient(delete_ing_ID)

        elif option_ingredients == 4:           # show user's ingredients
            # show the list of all the ingredients here 
            value = show_ingredients()

        elif option_ingredients == 5:           # back to user menu
        # back to the before menu
            break

# submenu to modify ingredients
def modify_ingredients_menu():
    while True:
        show_modify_ingredients_MENU()
        option = validate_input(input("Enter an option: "))

        if option == 1:                         # modify ingredient name
        #enter the ingredient ID
            mod_ing_ID = int(input("Enter the ingredient ID: "))
            #Enter your new name
            mod_ing_name = input("Enter the new ingredient name: ")
            # set the ingredient name here
            set_ingredient_name(mod_ing_ID,mod_ing_name)
        
        elif option == 2:                       # modify ingredient cost
            #enter the ingredient ID
            mod_ing_ID = int(input("Enter the ingredient ID: "))
            #enter the new ingredient cost
            mod_ing_cost = int(input("Enter the new cost: "))
            # set the ingredient cost here
            set_cost_ingredient(mod_ing_ID,mod_ing_cost)    

        elif option == 3:                    # modify ingredient vegan
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

        elif option == 4:                    # modify ingredient carb
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
        
        elif option == 5:
            break

# menu to manage recipes
def recipe_menu():
    while True:
        show_recipe_MENU()
        option = validate_input(input("Enter an option: "))
        
        if option == 1:                                 # add recipe        
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
            
        elif option == 2:                   # go to modify recipe submenu
            modify_recipe_menu()

        elif option == 3:                   # add recipe step
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

        elif option == 4:                   # return to user menu
            # exit to the main menu
            break


def modify_recipe_menu():
    while True:
        show_modify_recipe_MENU()
        option = int(input("Choose an option: "))
        if option == 1:                        # modify recipe name
            mod_recipe_option = int(input("Enter the recipe id to modify: "))
            mod_recipe_name = input("Enter the new recipe name: ")
            set_recipe_name(mod_recipe_option,mod_recipe_name)

        elif option == 2:                        # modify recipe prep time              
            mod_recipe_option = int(input("Enter the recipe id to modify: "))
            mod_recipe_prep_time = int(input("Enter the new prep time: "))
            set_prepTime_recipes(mod_recipe_option,mod_recipe_prep_time)
        
        elif option == 3:                     # modify recipe cook time     
            mod_recipe_option = int(input("Enter the recipe id to modify: "))
            mod_recipe_cook_time = int(input("Enter the new cook time: "))
            set_cookTime_recipes(mod_recipe_option,mod_recipe_cook_time)

        elif option == 4:                          # modify recipe difficulty level
            mod_recipe_option = int(input("Enter the recipe id to modify: "))
            mod_recipe_diffLevel = validate_number(int(input("Enter the difficult level: ")))
            set_diffLevel_recipes(mod_recipe_option,mod_recipe_diffLevel)
            
        elif option == 5:                       # modify recipe calories per serving
            mod_recipe_option = int(input("Enter the recipe id to modify: "))
            mod_recipe_cal = int(input("Enter the new calories per serving: "))
            set_calories_per_serving_recipes(mod_recipe_option,mod_recipe_cal)

        elif option == 6:                       # modify recipe vegan
            mod_recipe_option = int(input("Enter the recipe id to modify: "))
            aux5 = input("Enter the if it is vegan(yes/no): ")
            if  aux5 == "yes" or aux5 == "YES" or aux5== "Yes":
                mod_recipe_vegan = True
            else:
                mod_recipe_vegan =False
            set_vegan_recipes(mod_recipe_option,mod_recipe_cal)

        elif option == 7:                     # modify recipe carb
            mod_recipe_option = int(input("Enter the recipe id to modify: "))
            aux6 = input("Enter the if it is low carb(yes/no): ")
            if  aux6 == "yes" or aux6 == "YES" or aux6 == "Yes":
                mod_recipe_carb = True
            else:
                mod_recipe_carb =False
            set_carb_recipes(mod_recipe_option,mod_recipe_carb)

        elif option == 8:                       # delete recipe
            mod_recipe_option = int(input("Enter the recipe id to delete: "))
            delete_recipe(mod_recipe_option)

        elif option == 9:
            break


#################
#   MAIN MENU   #
#################




# We define a variable to store the userID
usuarioID = None

# We define a variable to store the nickname
nickname = None

# main loop
while True:
    # We show the main menu
    show_principal_menu()

    # We get user input
    option = validate_input(input("Enter an option: "))

    # login
    if option == 1:
        login()
    
    # new user
    elif option == 2:
        create_new_user()

    # list users
    elif option == 3:
        print("Listing users...")
        show_user()

    elif option == 4:
        sys.exit()