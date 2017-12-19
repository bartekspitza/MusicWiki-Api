from flask_restful import Resource
from models.artistModel import ArtistModel
import bs4 as bs
import urllib
from methods import getArtist

class Artist(Resource):

    def get(self, artist):
        newArtist = ""

        try:
            newArtist = ArtistModel(*getArtist(artist))
        except:
            return 500

        return newArtist.json(), 201
