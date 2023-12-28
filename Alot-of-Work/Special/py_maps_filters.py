# # Define a function to square a number
# def square(x):
#     return x ** 2

# # Create a list of numbers
# numbers = [1, 2, 3, 4, 5]

# # Use map() to apply the square function to each element in the list
# squared_numbers = map(square, numbers)

# # Convert the result to a list (as map() returns an iterator)
# result_list = list(squared_numbers)

# # Print the result
# print(result_list)

menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def find_coffe(coffee):
    if coffee[0] == "c":
        return coffee

print("------MAP function------")
map_coffee = map(find_coffe, menu)

print(map_coffee)

for x in map_coffee:
    print(x)

print("------FILTER function------")
filter_coffee = filter(find_coffe, menu)

print(filter_coffee)

for x in filter_coffee:
    print(x)