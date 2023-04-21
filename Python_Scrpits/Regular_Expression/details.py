import re


def emails():
    #opening the file and looking through it
    line = open("practice").read()
    #method to find email
    info = re.findall("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+", line)
    for _ in info:
        print(f"the emails: {_}")

def num():
    # opening the file and looking through it
    line = open("practice").read()
    #let find a word/sentences # NOT UNIVERSAL
    info = re.findall(r".\d{3}.{3}.{5}\d.", line)

    for number in info:
        print(f"the contact info: {number}")

def names():
    # opening the file and looking through it
    line = open("practice").read()
    #names in the list:
    info = re.findall(f'(Mr|Ms)\.?\s[A-Z]\w*',line)
    print(info)



names()