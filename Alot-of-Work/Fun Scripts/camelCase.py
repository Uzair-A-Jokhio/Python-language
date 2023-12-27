#get user input
camelCase = input("camelCase: ")

#print snake_case
print("snake_case: ", end="")

#loop through every letter
for letter in camelCase:

    #check if letter is in upper case
    if letter.isupper():
        print("_" + letter.lower(), end="")

    #otherwise print letter
    else:
        print(letter, end="")

print()