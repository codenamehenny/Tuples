#3. Mastering Tuple Packing and Unpacking in Python
#Task 1: Customer Order Processing Refine your skills in tuple unpacking by managing customer orders.
#Problem Statement: You are given a list of tuples, each representing a customer's order. 
# Each tuple contains the customer's name, the product ordered, and the quantity. 
# Your task is to unpack each tuple and print the order details in a user-friendly format.

orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Charlie", "TV", 1),
    ("Ana", "Video Game", 3)
]

#- Write a function to iterate over the list of orders. 
# - Unpack each tuple in the list and format the details for display.

for order in orders:
    name, item, quantity = order
    print(f"{name} ordered {quantity} {item}/s")