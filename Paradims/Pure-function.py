
"""A Pure fuction is a function that does not change/modify the global function """

cars = ["mercedes", "bmw", "volvo", "wolswagen"]
electric_cars = ["tesla", "nikola" , "Raven"]

def add_list(list, item_add):
    """This function is a example of Pure Funcation
    Take: takes Two items as args 
    return: a new list """
    try:
        list2 = list.copy()
        for i in item_add:
            list2.append(i)
        return list2
    except Exception as e:
        print("Error: ", e)


all_wheels = add_list(cars, electric_cars)

print(all_wheels)

