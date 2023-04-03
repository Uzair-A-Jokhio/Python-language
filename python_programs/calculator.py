print("Your are Using A Basic Calculator")  

# introduction
num1 = float(input("Enter First number: "))   # first input
op = input("Enter a Operator:")  # operations
num2 = float(input("Enter Second number: "))  
 
# these are the operation
if op == "+":
    result = num1 + num2
elif op == "*":
    result = num1 * num2
elif op == "-":
    result = num1 - num2
elif op == "/":
    result = num1 / num2
else:
    print("Error Invalid Operator")

if op in ["-","+","/","*"]:
    print(f"{num1} {op} {num2} = {result}")
else:
    print("-----------------------------")

