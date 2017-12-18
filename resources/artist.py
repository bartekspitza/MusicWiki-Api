from flask_restful import Resource
from models.artistModel import ArtistModel
import bs4 as bs
import urllib
from methods import getImage, getDesc, getTopSongs

class Artist(Resource):

    def get(self, artist):
        htmlBody = ""
        try:
            htmlBody = urllib.request.urlopen("https://en.wikipedia.org/wiki/ " + artist)
        except urllib.error.HTTPError as E:
            if E.code == 404:
                return 400


        soup = bs.BeautifulSoup(htmlBody, "html.parser")
        try:
            self.imageURL = getImage(artist)
            self.desc = getDesc(soup)
            self.bornDate = soup.find("span", "bday").text
            self.topSongs = getTopSongs(artist)
        except:
            return 500

        new_artist = ArtistModel(self.bornDate, self.desc, self.imageURL, self.topSongs)

        return new_artist.json(), 201
