from bs4 import BeautifulSoup as Soup
import re
from urllib.request import Request, urlopen

def makeUrl(artist):
    modifiedArtistString = artist.replace("_", "-").lower()
    modifiedArtistString = modifiedArtistString[0].upper() + modifiedArtistString[1::]
    return "https://genius.com/artists/" + modifiedArtistString

def getSoupHTML(query):
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
    req = Request(query, headers=header)
    html = urlopen(req)

    return Soup(html, "html.parser")

def imageFromGenius(page):
    divWithImage = page.find("div", "user_avatar")
    return re.search(r'http([^\'" >]+)', str(divWithImage)).group(0)

def descFromGenius(page):
    fromGenius = [x.text for x in page.findAll("p")]
    if fromGenius:
        return fromGenius

def descFromWiki(artist):
    req = Request("https://en.wikipedia.org/wiki/ " + artist)
    html = urlopen(req)
    soup = Soup(html, "html.parser")

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

    return "".join(extract[0:stopIndex])

def getTopSongsFromGenius(page):
    topSongsGrid = page.findAll("div", "mini_card_grid-song")
    topSongs = []

    for i in range(len(topSongsGrid)):
        section = topSongsGrid[i]

        topSongs.append([section.find("div", "mini_card-title").text.strip()])
        topSongs[i].append(section.find("div", "mini_card-subtitle").text.strip())
        topSongs[i].append(re.search(r'http([^\'" >]+)', str(section.find("div", "mini_card-thumbnail"))).group(0))
        topSongs[i].append(re.search(r'http([^\'" >]+)', str(section.find("a", "mini_card"))).group(0))
    return topSongs



def getArtist(artist):
    url = makeUrl(artist)
    soup = getSoupHTML(url)

    imageURL = imageFromGenius(soup)
    topSongs = getTopSongsFromGenius(soup)
    descriptionParagraphs = descFromGenius(soup)

    if descriptionParagraphs == None:
        descriptionParagraphs = [descFromWiki(artist)]

    return [descriptionParagraphs, imageURL, topSongs]

# def getArtist(artist):
#     modifiedArtistString = artist.replace("_", "-").lower()
#     modifiedArtistString = modifiedArtistString[0].upper() + modifiedArtistString[1::]
#
#     header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
#     url = "https://genius.com/artists/" + modifiedArtistString
#     print(url)
#     req = Request(url, headers=header)
#     html = urlopen(req)
#     soup = Soup(html, "html.parser")
#
#     divWithImage = soup.find("div", "user_avatar")
#     imageURL = re.search(r'http([^\'" >]+)jpg', str(divWithImage)).group(0)
#
#     descriptionParagraphs = [x.text for x in soup.findAll("p")]
#
#     topSongsGrid = soup.findAll("div", "mini_card_grid-song")[0:5]
#     topSongs = []
#
#     for i in range(len(topSongsGrid)):
#         section = topSongsGrid[i]
#
#         topSongs.append([section.find("div", "mini_card-title").text.strip()])
#         topSongs[i].append(section.find("div", "mini_card-subtitle").text.strip())
#         topSongs[i].append(re.search(r'http([^\'" >]+)', str(section.find("div", "mini_card-thumbnail"))).group(0))
#         topSongs[i].append(re.search(r'http([^\'" >]+)lyrics', str(section.find("a", "mini_card"))).group(0))
#
#     for p in descriptionParagraphs:
#         print("\n")
#         print(p)
#
#     print(imageURL)
#
#     for section in topSongs:
#         print("\n")
#         for s in section:
#             print(s)
#
#     return [descriptionParagraphs, imageURL, topSongs]
#
# def getImage(artist):
#     modifiedString = artist.replace("_", "%20")
#     url = "https://www.bing.com/images/search?q=" + modifiedString + "&qs=n&form=QBIR&sp=-1&pq=" + modifiedString.lower() + "&sc=8-11"
#     br = RoboBrowser()
#     br.open(url)
#
#     html = str(br.parsed)
#
#     result = re.findall(r'http([^\'" >]+)jpg', html)
#     myList = []
#
#
#     for i in range(len(result)):
#         if i == 10:
#             break
#         myList.append("http" + result[i] + "jpg")
#
#     return myList
#
# def getDesc(artist):
#     htmlBody = urllib.request.urlopen("https://en.wikipedia.org/wiki/ " + artist)
#     soup = Soup(htmlBody, "html.parser")
#
#     extract = [x for x in str(soup.find("p").text)]
#
#     count = 0
#     count1 = 0
#     periodCount = 0
#     stopIndex = len(extract)-1
#     frenzyMode = False
#     while count != len(extract)-1:
#         if periodCount == 2:
#             stopIndex = count
#             break
#
#         char = extract[count]
#
#         if char == ".":
#             periodCount += 1
#
#         if char == "/":
#             count1 += 1
#             frenzyMode = True
#
#
#         if char in "[":
#             frenzyMode = True
#
#         if frenzyMode:
#             extract.pop(count)
#         else:
#             count += 1
#
#         if char in "]":
#             frenzyMode = False
#
#         if char == "/":
#             if count1 == 2:
#                 count1 = 0
#                 frenzyMode = False
#
#     return ["".join(extract[0:stopIndex]), soup.find("span", "bday").text]
#
# def getTopSongs(artist):
#     modifiedArtistString = artist.replace("_", "-").lower()
#     modifiedArtistString = modifiedArtistString[0].upper() + modifiedArtistString[1::]
#
#     hdr = {'User-Agent':'Mozilla/5.0'}
#     url = "https://genius.com/artists/" + modifiedArtistString
#
#     req = urllib.request.Request(url, headers=hdr)
#     html = urllib.request.urlopen(req)
#     soup = Soup(html, "html.parser")
#
#     extract = [x.text for x in soup.findAll("div", "mini_card-title")[0:5]]
#
#     return extract
