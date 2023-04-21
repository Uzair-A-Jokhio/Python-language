def first_program():
    name = input("What is your name: ")
    age = input("Tell me your age: ")
    color = input("And your favourite color is : ")
    print("lets do some maths ")
    num1 = input("Enter a number: ")
    num2 = input("Enter another number: ")
    print(":My Details: ")
    print("hello " + name + " and i am BEAUTIFUL")
    print("your so young just " + age)
    print("WOW! your favourite color is " + color + " mine too")
    result = int(num1) * float(num2)
    print("OK we did some addition and the answer is " + str(result))
    print("THANKS for being the first to use this Program ")

first_program()


def name_ask():

    while True:
        name = input("What is your name: ")
        if name.replace(" ","").isalpha() and len(name) > 3 :
            break
        else:
            print("Invalid name ")
    return name

def pyramid(build):
    for x in range(build+1):
        print("*"*x)


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
    print(":Personal Details:")
    print(f"Entered name: {entered_name}")
    print(f"Entered age: {entered_age}")

