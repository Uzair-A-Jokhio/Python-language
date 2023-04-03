import random

dice_art = {

    1: (

        "┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘",

    ),

    2: (

        "┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘",

    ),

    3: (

        "┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘",

    ),

    4: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘",

    ),

    5: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘",

    ),

    6: (

        "┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘",

    ),

}


def roll_dice(num_dice):
    """return a list of intergers
    Each returned integer is a random number btw 1 and 6 """

    roll_result = []
    for i in range(num_dice):
        roll = random.randint(1,6)
        roll_result.append(roll)
    return roll_result



def parse_input(input_string):
    """return the input as an integer btw 1 and 6.
    
    check the input value is an integer btw 1 and 6
    if so return the interger with same value othrwise tell the user 
    to enter a vaild number 
    """
    if input_string.strip() in {"1","2","3","4","5","6"}:
        return int(input_string)
    else:
        print("Please enter a number btw 1 to 6 ")
        raise SystemExit(1)

#---------main code block---------------

# 1 get user input 
num_dice_input = input("how many dice you want to roll? (Select [1-6]): ")
num_dice = parse_input(num_dice_input)

# 2 roll the dice
roll_result = roll_dice(num_dice)



