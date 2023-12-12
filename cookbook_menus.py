
####################
# MENU VALIDATION  #
####################

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

######################
# MENU TEXT DISPLAYS #
######################

# Define a function to display the main menu
def show_principal_menu():
  print("** PRINCIPAL MENU **")
  print("1) Log in")
  print("2) Create user")
  print("3) Show user list")
  print("4) Exit")

def show_user_menu():
# We define a function to display the user menu
    print("** MAIN USER MENU **")
    print("1) Ingredients")
    print("2) Recipes")
    print("3) Steps")
    print("4) Exit")

# We define a function to display the ingredients menu
def show_ingredients_MENU():
  print("** INGREDIENTS MENU **")
  print("1) Add ingredient")
  print("2) Modify ingredients")
  print("3) Delete ingredints")
  print("4) show ingredients list")
  print("5) Back")

# We define a function to display the recipe menu
def show_recipe_MENU():
  print("** RECIPE MENU **")
  print("1) Add recipe")
  print("2) Modify recipe")
  print("3) Delete recipe")
  print("4) show recipe list")
  print("5) Back")

# We define a function to display the modify ingredients menu
def show_modify_ingredients_MENU():
  print("** MODIFY INGREDIENTS MENU **")
  print("1) Modify the ingredient name")
  print("2) Modify the ingredient cost")
  print("3) Modify the ingredient vegan")
  print("4) Modify the ingredient carb")
  print("5) Back")

# We define a function to display the modify recipe menu
def show_modify_recipe_MENU():
  print("** MODIFY RECIPE MENU **")
  print("1) Modify the recipe name")
  print("2) Modify the recipe prep_time")
  print("3) Modify the recipe cook_time")
  print("4) Modify the recipe difficult level")
  print("5) Modify the recipe calories per serving")
  print("6) Modify the recipe vegan")
  print("7) Modify the recipe carb")
  print("8) Delete a recipe")
  print("9) Back")
  