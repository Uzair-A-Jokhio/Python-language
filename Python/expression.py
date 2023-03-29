def main():
    import re
    x = 'From: uzairarifjokhio@gmail.com.pk lol pok hello 5 30 2022'
    y = re.findall("\S+@\S+", x)
    print(y) 


def main2():
    import re
    x = 'from: uzairarifjokhio@gmail.com.pk lol pok hello 5 30 2022'
    y = re.findall("^from.+k", x)
    print(y)
