import re


def main():
    x = 'From: uzairarifjokhio@gmail.com.pk lol pok hello 5 30 2022'
    y = re.findall("\S+@\S+", x)
    print(y) 


def main2():
    
    x = 'from: uzairarifjokhio@gmail.com.pk lol pok hello 5 30 2022'
    y = re.findall("^from.+k", x)
    print(y)


def regex():
    new_line = open("regex_sum_1709225.txt")
    line = new_line.read()

    format = re.findall("[0-9]+", line)

    #converts_string_into_integer
    conversion = [int(i) for i in format]

    #output the data
    print(f"the total number are: {len(conversion)}")
    print(f"The sum is: {sum(conversion)}")
    print(f"the avg per length: {sum(conversion)/len(conversion)}")
    print(conversion)




def emails():
    #opening the file and looking through it
    line = open("practice").read()
    #method to find email
    info = re.findall("[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]+", line)
    print(info)


def num():
    # opening the file and looking through it
    line = open("practice").read()
    #let find a word/sentences # NOT UNIVERSAL
    info = re.findall(r".\d{3}.{3}.{5}\d.", line)

    for number in info:
        print(f"the contact info: {number}")
