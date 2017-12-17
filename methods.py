from robobrowser import RoboBrowser
import re

def getImage(artist):
    modifiedString = artist.replace("_", "%20")
    url = "https://www.bing.com/images/search?q=" + modifiedString + "&qs=n&form=QBIR&sp=-1&pq=" + modifiedString.lower() + "&sc=8-11"
    br = RoboBrowser()
    br.open(url)

    html = str(br.parsed)

    result = re.findall(r'http([^\'" >]+)jpg', html)
    mydict = {}


    for i in range(len(result)):
        if i == 10:
            break
        mydict[i+1] = "http" + result[i] + "jpg"

    return mydict
