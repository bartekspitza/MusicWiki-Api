from flask_restful import Resource
from models.artistModel import ArtistModel
import bs4 as bs
import urllib
from methods import getImage, getDesc, getTopSongs

class Artist(Resource):

    def get(self, artist):
        newArtist = ""

        try:
            fromWiki = getDesc(artist)
            newArtist = ArtistModel(getImage(artist), fromWiki[0], fromWiki[1], getTopSongs(artist))
        except:
            return 500

        return newArtist.json(), 201
