'''
	This demonstrates recording a multi-step transaction to a MySQL database.
	This transaction requires 3 tables to be updated. To maintain ACID compliance
	we only commit changes when the entire transction is complete. If any stage 
	fails, the entire transaction needs to fail.

	https://www.essentialsql.com/sql-acid-database-properties-explained/

	DB: 		Classic Models
	Server: 	MySQL
	Address: 	127.0.0.1
	Port: 		3306

	Various techniques are demonstrated. Connections are created and closed on an "as needed" basis
	and not left to persist.
	Also demonstrates passing MySQL Cursor objects as arguments to functions
'''
import mysql.connector	# module to allow us to talk to MySQL
import datetime			# module to get the current date and do date math

def get_connection() -> mysql.connector.connect:
	'''
		returns a connection to the classicmodels database
	'''
	try:
		return mysql.connector.connect(
				user	 = 'root',			# change this to work with other users
				password = 'root',			# change password
				database = 'classicmodels',	# database name
				host  	 = 'localhost'		# address of MySQL student. Default port 3306
			)
	except mysql.connector.Error as err:	# if you make it here, there was a problem
		print(f'There was a problem connecting to the database {err}')
		return None							# nothing to return because connection failed

def new_order_PK() -> int:
	'''
		Calculates a new order number from the orders table in classic models
		Use this to create the next order number in the sequence

		This is not necessary if your PK is auto increment
	'''
	con = get_connection()									# get the connection
	cur = con.cursor()										# get a cursor object
	cur.execute('SELECT MAX(orderNumber) FROM orders;')		# select the largest order number
	pk = cur.fetchone()[0]									# fetch the result from the 0th index 
	con.close()												# close connection
	return pk + 1											# return result

def update_stock_levels(cart: list, cur: mysql.connector.cursor) -> None:
	'''
		Decrements quantity in stock for each product in the shopping cart

		Parameters:
			cart (list): The shopping cart of (productcode, quantity) tuples
			cur (cursor): The MySQL cursor object representing the connection

		Returns: None
	'''
	# sql statement that handles the decrementation of the quantityInStock field
	sql = "UPDATE products SET quantityInStock = quantityInStock - %s WHERE productCode = %s"
	for product in cart:							# for each product in the cart
		product_code= product[0]					# alias the product code for readability
		quantity	= product[1]					# alias the quantity for readability
		cur.execute(sql, (quantity, product_code))	# execute the query. Don't commit. Not done

def process_order(cust_num: int, cart: list) -> bool:
	'''
		Processes a Classic Models order transaction

		Parameters:
			cust_num (int): The customer placing the order
			cart (list): The shopping cart of (productcode, quantity) tuples

		Returns:
			boolean representing the status of the transaction
	'''
	try:
		# STEP 1: Do any calculations that are required for the new record
		order_number	= new_order_PK()								# need to calculate the new order number
		current_date	= datetime.date.today()							# get the current date
		required_date	= current_date + datetime.timedelta(10)			# required date: arbitrary 10 days in the future
																		# This should be determined by the customer
		# STEP 2: Create the new Order record
		sql		= 'INSERT INTO orders VALUES(%s,%s,%s,%s,%s,%s,%s);'	# prepared SQl statement
		params	= (order_number, current_date, required_date, None,		# tuple of values to be substituted
					'In Process', 'Customer was rude', cust_num)
		con		= get_connection()										# get a connection to classic models
		cur		= con.cursor()											# get a cursor object
		cur.execute(sql, params)										# execute sql, don't commit until transaction is complete

		# STEP 3: Record each product on the order in the order details table
		sql	= "INSERT INTO orderdetails VALUES(%s, %s, %s, %s, %s);"	# prepared SQL statement
		line= 1															# counter for the line number field
		for product in cart:											# iterate through the shopping cart
			product_code= product[0]									# alias the product code for readability
			quantity	= product[1]									# alias the quantity for readability

			# SUB TASK: Get the price of the product in order to calculate the sale price
			# This could be implemented in a variety of ways, and probably should be a function
			# This code just marks everything up 10%
			cur.execute(f'SELECT buyPrice FROM products WHERE productCode = "{product_code}";')
			price = float(cur.fetchone()[0]) * 1.10						# add an arbitrary 10% markup to each product

			cur.execute(sql, (order_number, product_code,				# execute the SQL statement
						quantity, price, line))							# do not commit yet. Not done
			line += 1													# increment the line number

		# STEP 4: Update quantity in stock levels for each product in the cart
		update_stock_levels(cart, cur)									# pass the cart to function for updating stock levels

		# STEP 5: Commit the transaction
		con.commit()													# all tasks complete, commit the changes
		con.close()														# close the connection
		return True														# order was successful
		
	except mysql.connector.Error as err:								# there was a problem
		print(f'There was a problem with the transaction: {err}')		# print the error message
		con.rollback()													# rollback any in-process changes due to some error condition
		con.close()														# close the connection
		return False													# transaction was not successful


if __name__ == '__main__':
	# mock shopping cart, just for testing purposes
	items = [				# list of tuples
		('S10_4698', 2),	# tuple of product_code and quantity ordered
		('S12_4473', 4),	# tuple of product_code and quantity ordered
		('S10_1678', 3),	# tuple of product_code and quantity ordered
		('S12_3148', 2)		# tuple of product_code and quantity ordered
	]

	# existing customer number, just for testing purposes
	customer = 475	
	process_order(customer, items)