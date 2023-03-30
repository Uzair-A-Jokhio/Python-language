print("Your are Using A Basic Calculator")  # introduction
num1 = float(input("Enter First number:"))   # first input
op = input("Enter a Operator:")  # operations
num2 = float(input("Enter Second number:"))
# these are the operation
if op == "+":
    print("YOUR ANSWER")
    print(num1 + num2)
    print("Thanks for using the first calculator ")
elif op == "*":
    print("YOUR ANSWER")
    print(num1 * num2)
    print("Thanks for using the first calculator ")
elif op == "-":
    print("YOUR ANSWER")
    print(num1 - num2)
    print("Thanks for using the first calculator ")
elif op == "/":
    print("YOUR ANSWER")
    print(num1 / num2)
    print("Thanks for using the first calculator  ")
else:
    print("MAN THIS IS A BASIC CALCULATOR NOT A SUPER COMPUTER TAKE IT EASY!!!")