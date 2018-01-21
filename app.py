from flask import Flask
from flask_restful import Api
from resources.artist import Artist
from resources.lyrics import Lyrics
app = Flask(__name__)
api = Api(app)


api.add_resource(Artist, "/artist/<string:artist>")
api.add_resource(Lyrics, "/lyrics")

if __name__ == "__main__":
    app.run(port=5000, debug=False)
