story1 = "--Darkness my old Friend--- \n this is a short story written \n by those whom lost the way \n in the wilderness in the Dark Forest "

try:
    with open("Files/newfile", "w") as file:
        file.writelines(story1)
except FileNotFoundError as e:
    print("Error", e)
except Exception as e:
    print("ERROR", e)