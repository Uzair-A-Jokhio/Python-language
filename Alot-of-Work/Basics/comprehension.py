print("---- List Comp ----")
# [ <expression> for x in <sequence> if <condition>] 
languages = ["Python","Ruby","Perl","Go","Java"]
lengths = [len(language) for language in languages]
print(lengths)

print("-----------------------------------------------------------------------------------------------------------")

z = [x for x in range(1,50) if x % 3 ==0 ]
print(z)

print("-----------------------------------------------------------------------------------------------------------")

def odd_numbers(n):
	return [x for x in range(1,n+1) if x % 2 == 1]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]


print("---- Dict Comp ----")
# dict = { key:value for key, value in <sequence> if <condition> }

# Using range() function and no input list
usingRange = {x:x*2 for x in range(12)}
print("Use range(): ",usingRange)

# Lists
months = ["Jan", "Feb", "Mar", "Apr", "May", "June", "July", "Aug", "Sept", "Oct", "Nov", "Dec"]
number = [1,2,3,4,5,6,7,8,9,10,11,12]

# Using one input List
num_dict = {x:x**2 for x in number} 
print("Using one list: ", num_dict)

month_dict = {key:value for (key, value) in zip(number, months)}
print("Using 2 list input: ", month_dict)

