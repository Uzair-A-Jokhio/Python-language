'''These Code were assigments of course '''
# 

def jon():

    import urllib.request, urllib.error, urllib.parse
    import json


    link = input("Enter location: ")
    print(f"Retreving: {link}")
    url = urllib.request.urlopen(link)
    data = url.read().decode()

    print(f"Recived {len(data)} characters ")
    js = json.loads(data)
    new_data = js["comments"]
    count = 0
    sum = 0

    for i in new_data:
        sum += int(i["count"])
        count += 1

    print(f"the count: {count}")    
    print(f"the sum: {sum}")





def web():
    import urllib.request, urllib.parse, urllib.error
    import json
    import ssl

    api_key = False
    # If you have a Google Places API key, enter it here
    # api_key = 'AIzaSy___IDByT70'
    # https://developers.google.com/maps/documentation/geocoding/intro

    if api_key is False:
        api_key = 42
        serviceurl = 'http://py4e-data.dr-chuck.net/json?'
    else :
        serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    while True:
        address = input('Enter location: ')
        if len(address) < 1: break

        parms = dict()
        parms['address'] = address
        if api_key is not False: parms['key'] = api_key
        url = serviceurl + urllib.parse.urlencode(parms)
        
        print('Retrieving', url)
        uh = urllib.request.urlopen(url, context=ctx)
        data = uh.read().decode()

        print('Retrieved', len(data), 'characters')
        js = json.loads(data)
        break
    
    place = js["results"][0]["place_id"]
    print(f"place_id: {place}")
       