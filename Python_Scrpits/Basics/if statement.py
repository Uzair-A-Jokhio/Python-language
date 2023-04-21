# asking the age!!
def age():
    zain_age = int(input("what is Zain's age? "))
    anas_age = int(input("what is Anas's age? "))

    if zain_age > anas_age:
        print("Zain is older then Anas!")
    elif zain < anas_age:
        print("Zain is younger then Anas!")
    else:
        print("Zain and Anas are of the same age.")


# finding the value is equal or not!!
def values():
    x = int(input("what is x? "))
    y = int(input("what is y? "))

    if x != y:
        print("x is not equal to y")
    else:
        print("x and y both are equal")


def even_or_odd(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

