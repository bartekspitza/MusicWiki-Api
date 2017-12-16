from robobrowser import RoboBrowser
import re

def getImage(artist):
    modifiedString = artist.replace("_", " ")
    url = "https://www.bing.com/images/search?q=" + artist + "&go=S%C3%B6k&qs=ds&form=QBIR&scope=images"
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
