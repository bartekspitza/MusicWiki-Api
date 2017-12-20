from flask_restful import Resource
from models.artistModel import ArtistModel
import bs4 as bs
import urllib
import methods

class Artist(Resource):

    def get(self, artist):
        newArtist = ""

        try:
            newArtist = ArtistModel(*methods.getArtist(artist))
        except:
            return 500

        return newArtist.json(), 201
