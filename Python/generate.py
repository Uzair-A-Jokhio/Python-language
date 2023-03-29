import random

def coin_tose():
    coin = random.choice(["head", "tails"])
    print(coin)

def shuffles():
    cards = ["king", "jack", "queen"]
    random.shuffle(cards)

    for card in cards:
        print(card)

import sys

def sys_argv():
    print("hello my name is ", sys.argv[0])
