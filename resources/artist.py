from flask_restful import Resource
from models.artistModel import ArtistModel
import bs4 as bs
import urllib
import methods

class Artist(Resource):

    def get(self, artist):
        newArtist = ""
        result = ""

        try:
            results = methods.getArtist(artist)
        except:
            return {"message": "Our Fault"}, 500

        if result == {"Message": "Not found"}:
            return {"message": "Not found"}, 400

        newArtist = ArtistModel(*result)
        return newArtist.json(), 200
