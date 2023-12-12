'''
	This program illustrates basic connectivity to mysql using Python

	assumptions: 
		Python is installed
		mysql is installed and running
		mysql connector for python is installed

	1) if you don't have Python installed, install Python: https://www.python.org/
	2) install mysql-connector-python using the terminal and 'pip' Python's package manager
		command: pip install mysql-connector-python
		Documentation: mysql-connector-python: https://dev.mysql.com/doc/connector-python/en/
		Note: If you are using Linux it is possible that PIP was not installed with Python: pip: https://pypi.org/project/pip/
	3) Once Python and the MySQL connector are installed you can begin communicating with MySQL. 
		Refer to the links above for documentation and examples

	Database: Classic Models
'''
# import statement to include mysql connector objects
from mysql.connector import connect, Error, errorcode, cursor

try:
	# call the connect function to establish a connection
	# this function will return a connection object
	connection = connect(
							user	 = 'root',
							password = 'root',
							database = 'classicmodels',
							host  	 = 'localhost'	
						)
	'''
	A database cursor can be thought of as a pointer to a specific row within a query result.  
	The pointer can be moved from one row to the next.  
	Depending on the type of cursor, you may be even able to move it to the previous row

	Cursors can be defined with two main scrolling capabilities, FORWARD_ONLY or SCROLL.

		FORWARD_ONLY: The cursor starts on the first row and end on the last. The cursor can only move to the next row in the result.
		SCROLL: the cursor can use operations, such as FIRST, LAST, PRIOR, NEXT, RELATIVE, ABSOLUTE to navigate the results.
	'''
	# ask the connection object (from above) to give you a cursor
	# you then use the cursor to execute SQL statements
	cur = connection.cursor() 

	sql = "SELECT customerName, phone FROM customers;"	# define an sql statement
	cur.execute(sql)									# execute the statement
														# the results will be "held" in the cursor object

	for result in cur:									# loop through the results. Each row is returned as a tuple
		print(f'{result[0]:<40}{result[1]}')			# print the results

	# demonstrate how to insert data into MySQL
	sql = 	("INSERT INTO customers (customerNumber, customerName, contactLastName, contactFirstName, phone, addressLine1, city, state, country)"
			 "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s);") # the '%s' characters are place holders

	# define a tuple, list or dictionary to contain the placeholder values	
	# each field in this tuple will be inserted into it's positional place holder 's%'
	# the order of this data must match the column list above
	params = ("1234", "Mountain Ops", "Whitener", "Ken", "1234567", "123 North St", "Dryden", "NY", "US")

	cur.execute(sql, params)	# execute the query by passing in the SQL statement and it's associated data
	connection.commit()			# commit transaction. The insert statement will not be 'official' until committed

	# let's select the newly inserted data using "largest PK logic"
	sql = "SELECT customerName, customerNumber from customers ORDER BY customerNumber DESC LIMIT 1;"
	cur.execute(sql)					# execute the SQL. The results will be held in the cursor object
	info = cur.fetchone()				# should only be one result. Use the 'fetchone' function
										# results are returned as Python tuples
	print(f"{info[0]}'s ID: {info[1]}")	# you can index the individual fields

	sql 	= f"DELETE FROM customers WHERE customerNumber = {info[1]};"# use an F String to format a paramter query
	cur.execute(sql)			# execute prepared statement and the parameters
	connection.commit()			# commit the changes

except mysql.connector.Error as err:							# catch connection errors
	print(f"There was a problem connecting: {err}")
finally:														# close the DB connection whether and exception was thrown or not
	if connection.is_connected():								# are we still connected?
		# clean up your mess!
		cur.close()				# close the cursor
		connection.close()		# close the connections
		print("Connection has been closed")