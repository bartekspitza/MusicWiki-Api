from flask_restful import Resource
from models.artistModel import ArtistModel
import methods

class Artist(Resource):

    def get(self, artist):
        result = ""

        try:
            result = methods.getArtist(artist)
        except:
            return {"message": "Our Fault"}, 500

        if result == {"Message": "Not found"}:
            return {"message": "Not found"}, 400

        print(result)
        newArtist = ArtistModel(*result)
        return newArtist.json(), 200
