from robobrowser import RoboBrowser
import re

def getImage(artist):
    modifiedString = artist.replace("_", "%20")
    url = "https://www.bing.com/images/search?q=" + modifiedString + "&qs=n&form=QBIR&sp=-1&pq=" + modifiedString.lower() + "&sc=8-11&sk=&cvid=00C85EE4272C43C8930DE4F431A3922E"
    br = RoboBrowser()
    br.open(url)

    html = str(br.parsed)

    result = re.findall(r'http([^\'" >]+)jpg', html)
    mydict = {}

    count = 1
    for u in result:
        mydict[count] = u
        count += 1

    return mydict
