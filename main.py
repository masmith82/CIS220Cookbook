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
        print("\nLogin successful. \nWelcome, " + userID + "!")
        global current_user
        current_user = get_user_id(userID)      # store current user_id (INT) for this session
        user_menu()


def create_new_user():
    #new_userID = int(input("Ingrese el id: "))     # we should let the databas assign the user ID
    new_first_name = input("Enter your first name: ")
    new_last_name = input("Enter your last name: ")
    new_email = input("Enter your email: ")
    new_username = input("Enter your username: ")
    new_password = input("Choose a password: ")
    create_user(new_first_name, new_last_name, new_email, new_username, new_password)

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
        
        if option_ingredients == 1:         # add ingredient to user stock
            show_user_ingredients(current_user)

        if option_ingredients == 2:         # add ingredient to user stock
            add_ingredient_to_stock(current_user)

        if option_ingredients == 3:         # add ingredient
            # Enter the ingredient name
            ing_add_name = input("Enter the ingredient name: ")
            # Enter the ingredient cost 
            ing_add_cost = float(input("Enter the cost per ingredient: "))
            
            # Enter if it is vegan or no
            while True:
                aux2 = input("The ingredient is low carb?(yes/no): ")
                if aux2 == "yes" or aux2 == "Yes" or aux2 == "YES" or aux2 == "y" or aux2 == "Y":
                    ing_add_veg = True
                    break
                elif aux2 == "no" or aux2 == "No" or aux2 == "NO" or aux2 == "n" or aux2 == "N":    
                    ing_add_veg = False
                    break
            
            # Enter if it is low carb
            while True:
                aux2 = input("The ingredient is low carb?(yes/no): ")
                if aux2 == "yes" or aux2 == "Yes" or aux2 == "YES" or aux2 == "y" or aux2 == "Y":
                    ing_add_low_carb = True
                    break
                elif aux2 == "no" or aux2 == "No" or aux2 == "NO" or aux2 == "n" or aux2 == "N":    
                    ing_add_low_carb = False
                    break

            # call the procedure insert_ingredient
            insert_ingredient(ing_add_name, ing_add_cost, ing_add_veg, ing_add_low_carb)

        elif option_ingredients == 4:           # modify ingredient submenu
            modify_ingredients_menu()

        elif option_ingredients == 5:           # delete ingredient
            # select what ingredient do you want to delete
            #enter the ingredient ID
            delete_ing_ID = int(input("Enter the ingredient ID: "))
            # enter the code to delete the ingredient here 
            delete_ingredient(delete_ing_ID)

        elif option_ingredients == 6:           # show full list of available ingredients
            # show the list of all the ingredients here 
            value = show_ingredients()

        elif option_ingredients == 7:           # back to user menu
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
            while True:
                vegan = input("The recipe is vegan?(yes/no): ")
                if vegan == "yes" or vegan == "Yes" or vegan == "YES" or vegan == "y" or vegan == "Y":
                    rec_add_veg = True
                    break
                elif vegan == "no" or vegan == "No" or vegan == "NO" or vegan == "n" or vegan == "N":    
                    rec_add_veg = False
                    break
        # Enter if it is low carb
            while True:
                low_carb = input("The recipe is low carb?(yes/no): ")
                if low_carb == "yes" or low_carb == "Yes" or low_carb == "YES" or low_carb == "y" or low_carb == "Y":
                    rec_add_carb = True
                    break
                elif vegan == "no" or low_carb == "No" or low_carb == "NO" or low_carb == "n" or low_carb == "N":    
                    rec_add_carb = False
                    break
        # call the procedure insert_ingredient
            result = insert_recipe(rec_add_name, rec_add_prep_time, rec_add_cook_time, rec_add_diff, rec_add_calories, rec_add_veg, rec_add_carb)
            
        elif option == 2:                   # go to modify recipe submenu
            modify_recipe_menu()

        elif option == 3:                   # show recipe list
            list_recipes()
            
        elif option == 4:                   # show recipe details
            recipe_id = validate_input(int(input("Enter the recipe ID to display: ")))
            list_recipe_detail(recipe_id)

        elif option == 5:                   # show filtered recipe
            recipe_filter_menu()

        elif option == 6:                   # delete recipe
            num_recipe_ID = int(input("Enter the recipe ID to delete: "))
            delete_recipe(num_recipe_ID)
        
        elif option == 7:                   # return to user menu
            break

def recipe_filter_menu():
    while True:
        show_recipe_filter_menu()
        option = int(input("Choose an option: "))
        
        if option == 1:                        # show recipes I can make with my ingredients
            filter_by_my_ingredients(current_user)
        elif option == 2:                       # show recipes within a calorie per serving limit
            calorie_limit = int(input("Enter the calorie limit: "))
            filter_by_calories(calorie_limit)
        elif option == 3:                       # show recipes within a total time limit
            time_limit = int(input("Enter the time limit: "))
            filter_by_time(time_limit)
        elif option == 4:                       # show vegan recipes
            basic_recipe_filter(1)
        elif option == 5:                       # show low-carb recipes
            basic_recipe_filter(2)
        elif option == 6:                       # show low-carb vegan recipes
            basic_recipe_filter(3)
        elif option == 7:
            break


# menu for modifying recipes
def modify_recipe_menu():
    while True:      
        show_modify_recipe_MENU()
        option = int(input("Choose an option: "))
        
        if option == 1:                   # add recipe step
            recipe_id = (validate_input(int(input("Enter the recipe ID: "))))
            add_recipe_step(recipe_id)

        if option == 2:                   # delete recipe step
            # enter recipe id
            num_recipe_ID = int(input("Enter the recipe ID: "))
            # enter step number
            get_recipe_steps(num_recipe_ID)
            num_step_number = int(input("Enter the step number: "))
            delete_recipe_step(num_recipe_ID, num_step_number)
        
        
        if option == 3:                        # modify recipe name
            mod_recipe_option = int(input("Enter the recipe id to modify: "))
            mod_recipe_name = input("Enter the new recipe name: ")
            set_recipe_name(mod_recipe_option,mod_recipe_name)

        elif option == 4:                        # modify recipe prep time              
            mod_recipe_option = int(input("Enter the recipe id to modify: "))
            mod_recipe_prep_time = int(input("Enter the new prep time: "))
            set_prepTime_recipes(mod_recipe_option,mod_recipe_prep_time)
        
        elif option == 5:                     # modify recipe cook time     
            mod_recipe_option = int(input("Enter the recipe id to modify: "))
            mod_recipe_cook_time = int(input("Enter the new cook time: "))
            set_cookTime_recipes(mod_recipe_option,mod_recipe_cook_time)

        elif option == 6:                          # modify recipe difficulty level
            mod_recipe_option = int(input("Enter the recipe id to modify: "))
            mod_recipe_diffLevel = validate_number(int(input("Enter the difficult level: ")))
            set_diffLevel_recipes(mod_recipe_option,mod_recipe_diffLevel)
            
        elif option == 7:                       # modify recipe calories per serving
            mod_recipe_option = int(input("Enter the recipe id to modify: "))
            mod_recipe_cal = int(input("Enter the new calories per serving: "))
            set_calories_per_serving_recipes(mod_recipe_option,mod_recipe_cal)

        elif option == 8:                       # modify recipe vegan
            mod_recipe_option = int(input("Enter the recipe id to modify: "))
            aux5 = input("Enter the if it is vegan(yes/no): ")
            if  aux5 == "yes" or aux5 == "YES" or aux5== "Yes":
                mod_recipe_vegan = True
            else:
                mod_recipe_vegan =False
            set_vegan_recipes(mod_recipe_option,mod_recipe_cal)

        elif option == 9:                     # modify recipe carb
            mod_recipe_option = int(input("Enter the recipe id to modify: "))
            aux6 = input("Enter the if it is low carb(yes/no): ")
            if  aux6 == "yes" or aux6 == "YES" or aux6 == "Yes":
                mod_recipe_carb = True
            else:
                mod_recipe_carb =False
            set_carb_recipes(mod_recipe_option,mod_recipe_carb)

        elif option == 10:
            break


#################
#   MAIN MENU   #
#################

# We define a variable to store the userID
usuarioID = None

# We define a variable to store the nickname
nickname = None
connect()

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
        disconnect()
        sys.exit()