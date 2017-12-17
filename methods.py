from robobrowser import RoboBrowser
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

def getDesc(sauce):

    extract = [x for x in str(sauce.find("p").text)]

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
