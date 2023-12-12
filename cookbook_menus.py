
####################
# MENU VALIDATION  #
####################

def validate_input(option):
  if type(option) == int:
    return option
  while not option.isdigit():
    print("The entry must be a number.")
    option = input("Enter an option: ")
  return int(option)

def validate_quantity(option):
  if type(option) == "":
    print("No quantity entered, quantity set to 0.")
    return 0
  if type(option) == int:
    return option
  while not option.isdigit():
    print("The entry must be a number.")
    option = input("Enter an option: ")
  return int(option)

def validate_number(entrada):
  while int(entrada) < 1 or int(entrada) > 5:
    print("La entrada debe ser un número entre 1 y 5.")
    entrada = input("Ingrese un número: ")
  return int(entrada)

######################
# MENU TEXT DISPLAYS #
######################

# Define a function to display the main menu
def show_principal_menu():
  print("\n** PRINCIPAL MENU **")
  print("1) Log in")
  print("2) Create user")
  print("3) Show user list")
  print("4) Exit\n")

def show_user_menu():
# We define a function to display the user menu
    print("\n** MAIN USER MENU **")
    print("1) Ingredients")
    print("2) Recipes")
    print("3) Exit\n")

# We define a function to display the ingredients menu
def show_ingredients_MENU():
  print("\n** INGREDIENTS MENU **")
  print("1) Show your ingredient stock")
  print("2) Add ingredient to your stock")
  print("3) Create new custom ingredient")
  print("4) Modify ingredients")
  print("5) Delete ingredints")
  print("6) Show ingredients list")
  print("7) Back\n")

# We define a function to display the recipe menu
def show_recipe_MENU():
  print("\n** RECIPE MENU **")
  print("1) Add recipe")
  print("2) Modify recipe")
  print("3) Show recipe list")
  print("4) Show recipe detail")
  print("5) Apply filters")
  print("6) Delete recipe")
  print("7) Back\n")

# We define a function to display the modify ingredients menu
def show_modify_ingredients_MENU():
  print("\n** MODIFY INGREDIENTS MENU **")
  print("1) Modify the ingredient name")
  print("2) Modify the ingredient cost")
  print("3) Set vegan status")
  print("4) Set low-carb status")
  print("5) Back\n")

def show_recipe_filter_menu():
  print("\n** RECIPE FILTER MENU **")
  print("1) Show recipes I can make with my ingredients")
  print("2) Show recipes within a calorie per serving limit")
  print("3) Show recipes within a prep time limit")
  print("4) Show vegan recipes")
  print("5) Show low-carb recipes")
  print("6) Show low-carb vegan recipes")
  print("7) Back\n")

# We define a function to display the modify recipe menu
def show_modify_recipe_MENU():
  print("\n** MODIFY RECIPE MENU **")
  print("1) Add a recipe step")
  print("2) Delete a recipe step")
  print("3) Modify the recipe name")
  print("4) Modify the recipe prep_time")
  print("5) Modify the recipe cook_time")
  print("6) Modify the recipe difficult level")
  print("7) Modify the recipe calories per serving")
  print("8) Modify the recipe vegan")
  print("9) Modify the recipe carb")
  print("10) Back\n")
  