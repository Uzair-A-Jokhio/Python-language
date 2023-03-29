def main():
    y = get_int("what is y? ")
    print(f"y is {y}")




def get_int(prompt):
    while True:
        try:
            x = int(input(prompt))
        except ValueError:
            print("ERROR; not an intgear!")
        else:
            return x 


main()