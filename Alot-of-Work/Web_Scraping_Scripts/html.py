def sock():
    import socket

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET https://www.linkedin.com/feed/ HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')

    mysock.close()

#URLLIB REQUEST AND RESPONCE
def newkid():

    import urllib.request, urllib.parse, urllib.error

    fhand = urllib.request.urlopen("https://www.coursera.org/learn/python-network-data/lecture/kWTYV/worked-example-using-urllib-chapter-12")
    for line in fhand:
        live = line.decode().strip()
        print(live)

newkid()
#xml extracting data
def xml():

    import urllib.request, urllib.parse, urllib.error
    import xml.etree.ElementTree as ET

    link = input("Enter url- ")
    html = urllib.request.urlopen(link).read().decode()
    print(f"Retreving: {link}")
    print((f"Retrived {len(html)} characters"))

    data = ET.fromstring(html)
    item = data.findall('comments/comment')
    count = 0
    sum = 0

    for x in item:
        count += 1
        sum += int(x.find('count').text)

    print(f"Count: {count}")
    print(f"sum: {sum}")
