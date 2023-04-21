def pig_latin(text):
    say = ""
    # Separate the text into words
    words = text.split()
    for word in words:
        # Create the pig latin word and add it to the list
        pig_word = word[1:] + word[0] + "ay"
        # Turn the list back into a phrase
        say += pig_word + " "
    return say


print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
print(pig_latin("programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"

print("-----------------------------------------------------------------------------------------------------------")



def group_list(group, users):
    members = ", ".join(users)
    return f"{group}: {members}"


print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
print(group_list("Users", "")) # Should be "Users:"


print("-----------------------------------------------------------------------------------------------------------")


def guest_list(guests):
	for index,(name, age, profesion) in enumerate(guests):
		print("{} is {} years old and works as {}".format(name,age,profesion))

guest_list([('Ken', 30, "Chef"), ("Pat", 35, 'Lawyer'), ('Amanda', 25, "Engineer")])



print("-----------------------------------------------------------------------------------------------------------")


def octal_to_string(octal):
    result = ""
    value_letters = [(4, "r"), (2, "w"), (1, "x")]
    # Iterate over each of the digits in octal
    for x in [int(n) for n in str(octal)]:
        # Check for each of the permissions values
        for value, letter in value_letters:
            if x >= value:
                result += letter
                x -= value
            else:
                result += "-"
    return result


print(octal_to_string(755))  # Should be rwxr-xr-x
print(octal_to_string(644))  # Should be rw-r--r--
print(octal_to_string(750))  # Should be rwxr-x---
print(octal_to_string(0))  # Should be rw-------

print("-----------------------------------------------------------------------------------------------------------")



