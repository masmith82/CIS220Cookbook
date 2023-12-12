'''
	This module contains a collection of functions that accomplish singular tasks
	associated with the Classic Models MYSql database.
 
	To use this module, import it and call the functions, paying careful attention
	to arguments and return types. READ THE DOCSTRINGS
'''

# use some MySQL modules provided by the MySQL Python Connector
import mysql, mysql.connector

def connection() -> mysql.connector.connect:
	'''
		Function connects to classic models database
		and returns a mysql connection object

		Parameters: None

		Returns: mysql connection object
	'''
	try:
		return mysql.connector.connect(
							user	 = 'root',
							password = 'root',
							database = 'classicmodels',
							host  	 = 'localhost'	
						)
	except mysql.connector.Error as err:
		print(f"There was a problem connecting: {err}")
		return None

def largest_pk(table_name: str, pk_name: str) -> int:
	'''
		Function returns most recently inserted primary from a table

		Parameters:
			table_name (str): The name of the table
			pk_name (str): The name of the primary key field

		Returns:
			int: The largest primary key
	'''
	con		= connection()
	cur		= con.cursor()
	sql		= f"SELECT * from {table_name} ORDER BY {pk_name} DESC LIMIT 1;"
	cur.execute(sql)
	info	= cur.fetchone()
	con.close()
	return info[0]

def	get_order_total(order_id: int) -> float:
	'''
		Function gets the total for an order

		Parameter:
			order_id (int): The Order Number for a particular order

		Returns:
			float: The total currency amount for an order
	'''
	con		= connection()
	cur		= con.cursor()
	sql		= f"SELECT SUM(quantityOrdered * priceEach) FROM orderdetails WHERE orderNumber = {order_id};"
	cur.execute(sql)
	info	= cur.fetchone()
	con.close()
	return info[0]