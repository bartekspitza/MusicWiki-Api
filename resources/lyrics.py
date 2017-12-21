from flask_restful import Resource, reqparse
from flask import Flask, request
import methods

class Lyrics(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument("url", type=str, required=True, help="This field cannot be left blank!")

    def post(self):
        data = self.parser.parse_args()

        try:
            lyrics = methods.getLyricsFromGenius(data["url"])
            return {"lyrics": lyrics}, 200
        except:
            return {"message": "something went wrong"}, 500
