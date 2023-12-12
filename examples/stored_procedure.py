'''
	This small program ilustrates how to call a MySQL Stored Procedure
	from Python. Stored procedures allow us the ability to define an API
	(application programmers interface) for our database by defining the
	main behaviors as MySQL objects insetad of programmers having to define
	them in the language of their choice. Then you can simply call procedures
	from any type of app/language that you need.
	
	1) Define the procedure using an SQL CREATE PROCEDURE statement
	2) Execut the CREATE PROCEDURE statement to "store" the procedure in the DB
	2) Call the procedure using a programming language of choice
'''

# import statement to include mysql connector objects
import mysql
from mysql.connector import connect, Error, cursor

try:
	# call the connect function to establish a connection
	# this function will return a connection object
	connection = connect(
							user	 = 'root',
							password = 'root',
							database = 'classicmodels',
							host	 = 'localhost'	# 127.0.0.1:3306
						)
	cur = connection.cursor()			# get a cursor
 
	# need orderID and a variable for total and tax
	orderID	= 10106						# for WHERE clause	
	total	= 0							# variable to hold the total
	tax		= 0							# variable to hold the tax
	args 	= (orderID, total, tax)		# tuple containing procedure arguments
 
	# use the callproc function from the cursor object
	# pass the procedure name as a string and a tuple of expected arguments
	# check the procedure documentation!
	# unlike executing direct queries which populate the cursor with a table of results,
	# procedures return values in classic "function" behavior
	# store the return in a variable and then unpack
	result	= cur.callproc('order_total', args)	# returns a tuple
 
	# unpack the results from the tuple
	total	= float(result[1])					# alias results for readability
	tax		= float(result[2])
	
	print()
	print(f'{"Order Number:":<15}{orderID}')
	print(f'{"Sub Total:":<15}${total}')
	print(f'{"Tax:":<15}${tax}')
	print("=" * 24)
	print(f'{"Total:":<15}${total + tax}')
 
except mysql.connector.Error as err:
	print(err)
