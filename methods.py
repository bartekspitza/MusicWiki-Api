from robobrowser import RoboBrowser
import urllib.request
from bs4 import BeautifulSoup as Soup
import re

def getImage(artist):
    modifiedString = artist.replace("_", "%20")
    url = "https://www.bing.com/images/search?q=" + modifiedString + "&qs=n&form=QBIR&sp=-1&pq=" + modifiedString.lower() + "&sc=8-11"
    br = RoboBrowser()
    br.open(url)

    html = str(br.parsed)

    result = re.findall(r'http([^\'" >]+)jpg', html)
    myList = []


    for i in range(len(result)):
        if i == 10:
            break
        myList.append("http" + result[i] + "jpg")

    return myList

def getDesc(artist):
    htmlBody = urllib.request.urlopen("https://en.wikipedia.org/wiki/ " + artist)
    soup = bs.BeautifulSoup(htmlBody, "html.parser")

    extract = [x for x in str(soup.find("p").text)]

    count = 0
    count1 = 0
    periodCount = 0
    stopIndex = len(extract)-1
    frenzyMode = False
    while count != len(extract)-1:
        if periodCount == 2:
            stopIndex = count
            break

        char = extract[count]

        if char == ".":
            periodCount += 1

        if char == "/":
            count1 += 1
            frenzyMode = True


        if char in "[":
            frenzyMode = True

        if frenzyMode:
            extract.pop(count)
        else:
            count += 1

        if char in "]":
            frenzyMode = False

        if char == "/":
            if count1 == 2:
                count1 = 0
                frenzyMode = False

    return ["".join(extract[0:stopIndex]), soup.find("span", "bday").text]

def getTopSongs(artist):
    modifiedArtistString = artist.replace("_", "-").lower()
    modifiedArtistString = modifiedArtistString[0].upper() + modifiedArtistString[1::]

    hdr = {'User-Agent':'Mozilla/5.0'}
    url = "https://genius.com/artists/" + modifiedArtistString

    req = urllib.request.Request(url, headers=hdr)
    html = urllib.request.urlopen(req)
    soup = Soup(html, "html.parser")

    extract = [x.text for x in soup.findAll("div", "mini_card-title")[0:5]]

    return extract
