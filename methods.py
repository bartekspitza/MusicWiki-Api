from bs4 import BeautifulSoup as Soup
import re
from urllib.request import Request, urlopen

def makeUrl(artist):
    modifiedArtistString = artist.replace("_", "-").lower()
    modifiedArtistString = modifiedArtistString[0].upper() + modifiedArtistString[1::]
    return "https://genius.com/artists/" + modifiedArtistString

def getSoupHTML(url):
    header = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"}
    req = Request(url, headers=header)

    try:
        html = urlopen(req)
        return Soup(html, "html.parser")
    except:
        return None

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


def artistNameFromGenius(page):
    name = [x for x in page.find("h1").text]
    cleanName = ""
    for char in name:
        if char == "\n":
            break
        cleanName += char

    return cleanName

def getArtist(artist):
    url = makeUrl(artist)
    soup = getSoupHTML(url)

    if soup:
        name = artistNameFromGenius(soup)
        imageURL = imageFromGenius(soup)
        topSongs = getTopSongsFromGenius(soup)
        descriptionParagraphs = descFromGenius(soup)

        if descriptionParagraphs == None:
            descriptionParagraphs = [descFromWiki(artist)]

        return [name, descriptionParagraphs, imageURL, topSongs]

    return {"Message": "Not found"}

def getLyricsFromGenius(url):
    soup = getSoupHTML(url)
    extract = soup.find("div", "lyrics")

    result = [x.text for x in extract.findAll("p")]
    result = result[0].split("\n\n")
    result = [x.split("\n") for x in result]

    return result
