def name_ask():

    while True:
        name = input("What is your name: ")
        if name.replace(" ","").isalpha() and len(name) > 3 :
            break
        else:
            print("Error Invaild Entry : (Enter the correct name)   ")
    return name


def age_ask():
    while True:
        age = input("Enter your age: ")
        if age.isnumeric() and len(age) < 4 :
            break
        else:
            print("Invalid age")
    return age


def main():
    entered_name = name_ask()
    entered_age = age_ask()
    print("====================================================")
    print(":Personal Details:")
    print("====================================================")
    print(f"Entered name: {entered_name}")
    print(f"Entered age: {entered_age}")

main()