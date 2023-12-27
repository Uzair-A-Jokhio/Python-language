def divide(a,b):
    return a / b

try:
    divide(2,0)
except ZeroDivisionError as e:
    print(e, "we cannot divide by zero")
    print(e.__class__)
except Exception as e:
    print(e, "Something went wrong")

