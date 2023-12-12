import db

largest_cust_pk = db.largest_pk("customers", "customerNumber")

print(f"Largest customer PK is {largest_cust_pk}")

orders = [10174, 10374, 10141, 10247, 10363, 10183]

for order in orders:
	print(f"The total for order number {order} is: ${ db.get_order_total(order) }")