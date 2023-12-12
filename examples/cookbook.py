

import db
import mysql, mysql.connector
from mysql.connector import connect, Error, errorcode, cursor

def connection() -> mysql.connector.connect:
	try:
		return mysql.connector.connect(
							user	 = 'root',
							password = 'MJw!0TeN!0',
							database = 'cookbook',
							host  	 = 'localhost'	
						)
	except mysql.connector.Error as err:
		print(f"There was a problem connecting: {err}")
		return None

def option1():
    print("You selected option 1")

def option2():
    user_login()

def option3():
    print("You selected option 3")

def option4():
    print("You selected option 4")

def start_menu():
    print("Menu:")
    print("1. Register New User")
    print("2. Log In")
    print("0. Exit")

def new_user_reg():
    print("Menu:")
    print("1. Register New User")
    print("2. Log In")
    print("0. Exit")

def user_login():
    username = input("Enter username: ")
    user = cur.callproc('search_user', (username,))
    if user == -1:
        print("Username not found. Please try again.")
        user_login()
  
    pword = input("Enter password: ")
    cur.callproc('check_password', pword)
    while pword != 1:
        print("Incorrect password. Please try again.")
        pword = input("Enter password: ")

 
def user_menu():
    pass

# MAIN

conn = connection()
cur = conn.cursor() 

def main():
    while True:
        start_menu()
        choice = input("Enter the number of your choice (0 to exit): ")

        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            option3()
        elif choice == '4':
            option4()
        elif choice == '0':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid number.")

if __name__ == "__main__":
    main()







#sql = "SELECT customerName, phone FROM customers;"	# define an sql statement
#cur.execute(sql)									# execute the statement


for result in cur:									# loop through the results. Each row is returned as a tuple
	print(f'{result[0]:<40}{result[1]}')


	sql = 	("INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, state, country)"
			 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);") # the '%s' characters are place holders

	# define a tuple, list or dictionary to contain the placeholder values	
	# each field in this tuple will be inserted into it's positional place holder 's%'
	# the order of this data must match the column list above
	params = ("1234", "Mountain Ops", "Whitener", "Ken", "1234567", "123 North St", "Dryden", "NY", "US")

	cur.execute(sql, params)	# execute the query by passing in the SQL statement and it's associated data
	connection.commit()			# commit transaction. The insert statement will not be 'official' until committed


# def largest_pk(table_name: str, pk_name: str) -> int:
# 	'''
# 		Function returns most recently inserted primary from a table

# 		Parameters:
# 			table_name (str): The name of the table
# 			pk_name (str): The name of the primary key field

# 		Returns:
# 			int: The largest primary key
# 	'''
# 	con		= connection()
# 	cur		= con.cursor()
# 	sql		= f"SELECT * from {table_name} ORDER BY {pk_name} DESC LIMIT 1;"
# 	cur.execute(sql)
# 	info	= cur.fetchone()
# 	con.close()
# 	return info[0]

# def	get_order_total(order_id: int) -> float:
# 	'''
# 		Function gets the total for an order

# 		Parameter:
# 			order_id (int): The Order Number for a particular order

# 		Returns:
# 			float: The total currency amount for an order
# 	'''
# 	con		= connection()
# 	cur		= con.cursor()
# 	sql		= f"SELECT SUM(quantityOrdered * priceEach) FROM orderdetails WHERE orderNumber = {order_id};"
# 	cur.execute(sql)
# 	info	= cur.fetchone()
# 	con.close()
# 	return info[0]