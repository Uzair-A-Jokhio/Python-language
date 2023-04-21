""" This program will entry vaild Details 
    Any invaild data will not be entrend    """


def name_ask():# this function only take name as input and 
               # only charcter are allowed no funky names 

    while True:
        name = input("What is your name: ")
        if name.replace(" ","").isalpha() and len(name) > 3 : # the line of code check wheter the input is alphabet and the lengh is greath than 3
            break   # if the name is correct the code will break                                                          
        else:
            print("Error Invaild Entry : (Enter the correct name)") #correction message
    return name      #returing the name value


def age_ask():  # checking uf the age entered is valid
    while True:
        age = input("Enter your age: ")
        if age.isnumeric() and int(age) < 100 : # check the input value is a number and the lenght is < 4 
            break                             # so the age is approiate 
        else:
            print("Invalid age") #correction message
    return age


def main():
    entered_name = name_ask() #this call the function of name_ask
    entered_age = age_ask()   #this call the function of age_ask
    print("====================================================")
    print(":Personal Details:")    # display of detail
    print("====================================================")
    print(f"Name: {entered_name}")
    print(f"Age: {entered_age}")

main()