'''These Code were assigments of course '''


def soup():
    # To run this, download the BeautifulSoup zip file
    # http://www.py4e.com/code3/bs4.zip
    # and unzip it in the same directory as this file

    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    import ssl
    import re

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    
    url = input('Enter - ')
    html = urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup("span")
    sum = 0

    for tag in tags:
         sum += int(tag.contents[0])

    print(f"The total is: {sum}")
       


def link():
    import urllib.request, urllib.parse, urllib.error
    from bs4 import BeautifulSoup
    import ssl

    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    link = input("Enter URL -")
    count = int(input("Enter count:"))
    line = int(input("Enter the position:"))


    print(f"Retrieving: {link} ")
    for i in range(0, count):
        html = urllib.request.urlopen(link, context=ctx).read()
        soup = BeautifulSoup(html, "html.parser")
        tags = soup("a")
        con = 0
        pos = 0

        for tag in tags:
            pos += 1
            if pos == line:
                print("Retreveing: %s" % str(tag.get('href',None)))
                link = str(tag.get("href",None))
                pos = 0
                break

    